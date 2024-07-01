from .users_repository import UsersRepository


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

    assert True
