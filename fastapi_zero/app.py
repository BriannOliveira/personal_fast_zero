from fastapi import FastAPI, HTTPException, status

from fastapi_zero.schemas import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI()

database = []


@app.get('/', response_model=Message, status_code=status.HTTP_200_OK)
def read_root():
    return {'message': 'Hello World'}


@app.post('/users/', response_model=UserPublic, status_code=status.HTTP_201_CREATED)
def create_user(user: UserSchema):
    new_user = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(new_user)
    return new_user


@app.get('/users/', response_model=UserList, status_code=status.HTTP_200_OK)
def list_users():
    return {'users': database}


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='User not found'
        )

    user_with_id = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id

    return user_with_id


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='User not found'
        )

    del database[user_id - 1]

    return {'message': 'User deleted'}
