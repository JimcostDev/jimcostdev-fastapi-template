import pytest
from database.conn_db import get_database_instance

@pytest.fixture
def database_name():
    return "football"

@pytest.fixture
def collection_name():
    return "players" 

@pytest.fixture
def document_query():
    return {"name": "Robert Lewandowski"}

def test_connect_to_database(database_name, collection_name, document_query):
    """
    Prueba la conexión a una base de datos y la búsqueda de un documento.

    Args:
        database_name (str): Nombre de la base de datos.
        collection_name (str): Nombre de la colección.
        document_query (dict): Diccionario con el criterio de búsqueda.
    """

    with get_database_instance(database_name) as db:
        collection = db[collection_name]
        found_document = collection.find_one(document_query)

        assert found_document is not None, f"No se encontró el documento en la colección {collection_name}"

# Ejemplos de uso:
def test_connect_to_football_database():
    test_connect_to_database("football", "players", {"name": "Robert Lewandowski"})

def test_connect_to_other_database():
    test_connect_to_database("football", "players", {"country": "ColombiaA"})
    
