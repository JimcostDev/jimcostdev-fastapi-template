import pytest

from core.database import MongoDB
from core.config import settings

# Clases dummy para simular el comportamiento de Motor
class DummyClient:
    def __init__(self, uri):
        self.uri = uri
        self.admin = self
        self.closed = False
        self._dbs = {}

    async def command(self, cmd):
        # Simula un ping exitoso
        if cmd == 'ping':
            return {'ok': 1}
        raise Exception(f"Comando inesperado: {cmd}")

    def __getitem__(self, name):
        # Devuelve un objeto de base de datos dummy
        db = self._dbs.get(name)
        if not db:
            db = DummyDB(name)
            self._dbs[name] = db
        return db

    def close(self):
        # Marca como cerrado
        self.closed = True

class DummyDB:
    def __init__(self, name):
        self.name = name
        self._cols = {}

    def __getitem__(self, collection_name):
        # Devuelve una colección dummy
        col = self._cols.get(collection_name)
        if not col:
            col = object()
            self._cols[collection_name] = col
        return col

# Fixture que parchea AsyncIOMotorClient de Motor para usar DummyClient
@pytest.fixture(autouse=True)
def patch_motor(monkeypatch):
    monkeypatch.setattr('core.database.AsyncIOMotorClient', DummyClient)

@pytest.mark.asyncio
async def test_connect_and_disconnect():
    mdb = MongoDB()
    # Inicialmente no está conectado
    assert not mdb.is_connected

    # Al conectar, se crea el cliente y la base de datos, y se marca como conectado
    await mdb.connect()
    assert mdb.is_connected
    assert isinstance(mdb.client, DummyClient)
    assert mdb.db.name == settings.MONGODB_NAME

    # Conexiones repetidas deben ser idempotentes
    await mdb.connect()
    assert mdb.is_connected

    # Al desconectar, se cierra el cliente y se reinicia el estado
    await mdb.disconnect()
    assert not mdb.is_connected
    assert mdb.client.closed

@pytest.mark.asyncio
async def test_get_collection_auto_connect():
    mdb = MongoDB()
    # get_collection debe auto-conectar si no hay conexión
    col = await mdb.get_collection('testcol')
    assert mdb.is_connected
    assert hasattr(mdb.db, '__getitem__')
    # Llamadas posteriores a la misma colección devuelven el mismo objeto
    col2 = await mdb.get_collection('testcol')
    assert col2 is col
