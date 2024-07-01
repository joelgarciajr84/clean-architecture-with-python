import pytest
from .connection import DBConnectionHandler

@pytest.mark.skip(reason="Sensive Test")
def test_create_database_engine():
    db_connection_handler = DBConnectionHandler()

    engine = db_connection_handler.get_engine()

    print(engine)

    assert engine is not None
