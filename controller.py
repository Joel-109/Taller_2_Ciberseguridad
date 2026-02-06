import string
import numpy as np
from utils import get_vigerene_cipher_dict,transform_password,get_vigerene_decipher_dict, find_password_vigerene

alphabet = list(string.ascii_lowercase)
alphabet_lenght = len(alphabet)

def cesar_cipher(message,password):
    message = message.lower()
    ciphered_password = ""

    cesar =  alphabet[:password]
    cesar = alphabet[password:]+cesar

    cesar_dict = dict(zip(alphabet,cesar))

    print("El mensaje ingresado fue: ", message)
    print("La clave ingresada fue: ", password)
    
    for char in message:
        ciphered_password  += cesar_dict[char]

    return ciphered_password

def cesar_decipher(message,password):
    message = message.lower()
    final_message = ""
    
    if password is not None:
        print("Paso aca")
        cesar =  alphabet[:password]
        cesar = alphabet[password:]+cesar
        cesar_dict = dict(zip(cesar,alphabet))

        for char in message:
            final_message+=cesar_dict[char]

        return {
            "message":final_message,
            "password":password
        }
    
    common_syllables =  [
        "ma", "me", "mi", "mo", "mu",
        "pa", "pe", "pi", "po",
        "ta", "te", "ti", "to",
        "na", "ne", "no",
        "la", "le", "lo",
        "ra", "re", "ri", "ro",
        "sa", "se", "si", "so",
        "pan", "sol", "mal", "bien", "tan",
        "del", "por", "con", "las", "res",
        "que", "para", "como", "pero",
        "ción", "mente", "dad", "esta", "sobre"
    ]

    password = 0
    syllable_counter = {}

    for i in range(25):
        final_message = ""
        password = i
        cesar =  alphabet[:password]
        cesar = alphabet[password:]+cesar
        cesar_dict = dict(zip(cesar,alphabet))

        for letra in message:
            final_message+=cesar_dict[letra]

        syllable_counter[final_message] = 0

        for silaba in common_syllables:
            if silaba in final_message :
                syllable_counter[final_message] += 1
    
    final_message = max(syllable_counter,key=syllable_counter.get)
    counter_array = list(syllable_counter.values())
    password = np.argmax(counter_array)

    return {
        "message":final_message,
        "password":password
    }

def cipher_vigerene(message,password):
    vigerene_dict = get_vigerene_cipher_dict()
    vigerene_message = ""

    new_password = password
    if len(password) < len(message):
        new_password = transform_password(message,password)


    for charm, charp in zip(message,new_password):
        vigerene_message+=vigerene_dict[(charm, charp)]

    print("La palabra cifrada con el vigérene es: ",vigerene_message)

    return vigerene_message

def decipher_vigerene(message, password):
    vigerene_dict = get_vigerene_decipher_dict()
    vigerene_message = ""

    if password is None:
        return find_password_vigerene(vigerene_dict,message,password)
    
    new_password = password

    if len(password) < len(message):
        new_password = transform_password(message,password)

    for char_m, char_p in zip(message,new_password):
        vigerene_message+=vigerene_dict[(char_m,char_p)]

    return {
        "message":vigerene_message, 
        "password":password
    }
    
   