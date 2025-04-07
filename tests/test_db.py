import pytest
from core.database import mongodb, MongoDB

@pytest.mark.asyncio
async def test_connect_and_disconnect():
    # Conecta a la base de datos
    await mongodb.connect()
    
    # Verifica que el cliente y la base de datos se hayan inicializado
    assert mongodb.client is not None, "El cliente no se inicializó correctamente."
    assert mongodb.db is not None, "La base de datos no se inicializó correctamente."
    
    # Intenta obtener una colección 
    collection = mongodb.get_collection("test_collection")
    assert collection is not None, "No se pudo obtener la colección."
    
    # Desconecta de la base de datos
    await mongodb.disconnect()
    # Nota: mongodb.client no se pone a None al cerrar la conexión, por lo que no se realiza una aserción adicional

@pytest.mark.asyncio
async def test_get_collection_without_connect():
    # Crea una nueva instancia para simular que no se ha conectado aún
    mongo = MongoDB()
    
    # Verifica que al intentar obtener una colección sin conexión se lance un RuntimeError
    with pytest.raises(RuntimeError) as excinfo:
        mongo.get_collection("test_collection")
    
    assert "Base de datos no conectada" in str(excinfo.value)
