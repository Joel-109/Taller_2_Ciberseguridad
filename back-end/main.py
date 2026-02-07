from fastapi import FastAPI
from models import (CesarMessage,ViregeneMessage,CipheredCesarResponse,
                    DecipheredCesarResponse,DecipheredViregeneResponse,
                    CipheredViregeneResponse)
from controller import cesar_cipher,cesar_decipher,cipher_vigerene,decipher_vigerene
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/cesar/cipher/",response_model=CipheredCesarResponse)
async def cipher_cesar_process(cesar_message : CesarMessage):
    message = cesar_message.content
    password = cesar_message.password    
    response = cesar_cipher(message,password)

    return {
        "ciphered_message": response
    }

@app.post("/cesar/decipher/",response_model=DecipheredCesarResponse)
async def decipher_cesar_process(cesar_message : CesarMessage):
    message = cesar_message.content
    password = cesar_message.password  
    
    response = cesar_decipher(message,password)
    print(response)
    return {
        "deciphered_message": response['message'],
        "deciphered_password": response['password']
    }


@app.post("/vigerene/cipher/",response_model=CipheredViregeneResponse)
async def cipher_vigerene_process(viregene_message : ViregeneMessage):
    message = viregene_message.content
    password = viregene_message.password 
    
    response = cipher_vigerene(message,password)

    return {
        "ciphered_message": response
    }


@app.post("/vigerene/decipher/",response_model=DecipheredViregeneResponse)
async def decipher_vigerene_process(viregene_message : ViregeneMessage):
    message = viregene_message.content.lower()
    password = viregene_message.password
    
    response = decipher_vigerene(message,password)
    print(response)

    return {
        "deciphered_message": response['message'],
        "deciphered_password": response['password']
    }