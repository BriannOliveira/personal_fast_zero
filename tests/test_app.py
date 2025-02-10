from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app

client = TestClient(app)


def test_hello():
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World'}


def test_create_user():
    response = client.post(
        '/users/',
        json={
            'username': 'John Doe',
            'email': 'johndoe@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'John Doe',
        'email': 'johndoe@example.com',
        'id': 1,
    }


def test_list_users():
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'John Doe',
                'email': 'johndoe@example.com',
                'id': 1,
            }
        ]
    }


def test_update_user():
    response = client.put(
        '/users/1',
        json={
            'username': 'Jane Doe',
            'email': 'johndoe1@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'Jane Doe',
        'email': 'johndoe1@example.com',
        'id': 1,
    }


def test_delete_user():
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}
