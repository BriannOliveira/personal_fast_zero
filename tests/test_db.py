from sqlalchemy import select

from fastapi_zero.models import User


def test_create_user(session):
    new_user = User(
        username='John Doe', email='john@doe.com', password='secret_pass-word'
    )

    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).filter(User.username == 'John Doe'))
    assert user.username == 'John Doe'
