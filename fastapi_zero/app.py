from fastapi import FastAPI, status

from fastapi_zero.schemas import Message

app = FastAPI()


@app.get('/', response_model=Message, status_code=status.HTTP_200_OK)
def read_root():
    return {'Hello': 'World'}
