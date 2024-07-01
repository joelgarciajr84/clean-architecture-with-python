import pytest
from sqlalchemy import text
from src.infra.db.settings.connection import DBConnectionHandler
from .users_repository import UsersRepository

connection = DBConnectionHandler().get_engine().connect()


@pytest.mark.skip(reason='Sensive Test')
def test_insert_user():
    mocked_first_name = 'first_name'
    mocked_last_name = 'last_name'
    mocked_age = 30
    users_repository = UsersRepository()

    users_repository.insert_user(
        first_name=mocked_first_name,
        last_name=mocked_last_name,
        age=mocked_age
    )

    sql = '''
        SELECT * FROM users
        WHERE first_name='{}'
        AND last_name='{}'
        AND age={}
    '''.format(mocked_first_name, mocked_last_name, mocked_age)

    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.first_name == mocked_first_name
    assert registry.last_name == mocked_last_name
    assert registry.age == mocked_age


@pytest.mark.skip(reason='Sensive Test')
def test_select_user():
    mocked_first_name = 'Bruce'
    mocked_last_name = 'Wayne'
    mocked_age = 35

    sql = '''
        INSERT INTO users(first_name, last_name, age)
        VALUES('{}', '{}', {})'''.format(mocked_first_name, mocked_last_name, mocked_age)

    connection.execute(text(sql))
    connection.commit()

    users_repository = UsersRepository()
    response = users_repository.select_user(first_name=mocked_first_name)

    assert response[0].first_name == mocked_first_name
    assert response[0].last_name == mocked_last_name
    assert response[0].age == mocked_age

    delete_sql = text(F'''
                      DELETE FROM users WHERE id = {response[0].id}''')
    connection.execute(delete_sql)
    connection.commit()
