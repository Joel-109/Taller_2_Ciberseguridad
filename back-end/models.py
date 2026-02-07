from pydantic import BaseModel

class ViregeneMessage(BaseModel):
    content : str
    password : str | None = None

class CesarMessage(BaseModel):
    content : str
    password : int | None = None

class CipheredCesarResponse(BaseModel):
    ciphered_message: str

class DecipheredCesarResponse(BaseModel):
    deciphered_message : str
    deciphered_password : int 

class CipheredViregeneResponse(BaseModel):
    ciphered_message : str


class DecipheredViregeneResponse(BaseModel):
    deciphered_message : str
    deciphered_password : str

