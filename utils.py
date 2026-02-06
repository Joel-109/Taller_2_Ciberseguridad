import string
import pandas as pd

def get_vigerene_cipher_dict():
    vigerene_dict = {}
    alphabet = list(string.ascii_lowercase)
    alphabet_lenght = len(alphabet)

    for i in range(alphabet_lenght):
        for j in range(alphabet_lenght):
            a,b = alphabet[i],alphabet[j]
            index = (i+j) % alphabet_lenght
            vigerene_dict[(a,b)] = alphabet[index]

    return vigerene_dict

def get_vigerene_decipher_dict():
    vigerene_dict = {}
    alphabet = list(string.ascii_lowercase)
    alphabet_lenght = len(alphabet)

    for i in range(alphabet_lenght):
        for j in range(alphabet_lenght):
            a,b = alphabet[i],alphabet[j]
            index = (i-j) % alphabet_lenght
            vigerene_dict[(a,b)] = alphabet[index]

    return vigerene_dict



def transform_password(message,password):
    password_len = len(password)
    message_len = len(message)
    counter = 0

    new_password = password

    if password_len != message_len:
        for i in range(password_len,message_len):
            if len(password) == counter:
                counter = 0
            new_password+=password[counter]
            counter+=1

    return new_password


def find_password_vigerene(vigerene_dict, message, password : str):
    syllable_counter_dict = {}
    password_dict = {}
    common_syllables = [
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
            
    df_rockyou = pd.read_csv("../rockyou-top100.txt",encoding="latin-1",sep="\t",header=None,names=['contraseñas'])

    def check_password(passw : str):
        
        for char in passw:
            if char.isdigit():
                return 

        new_password = passw
        if len(passw) < len(message):
            new_password = transform_password(message,passw)

        vigerene_message = ""
        
        for char_m, char_p in zip(message,new_password):
            vigerene_message+=vigerene_dict[(char_m,char_p)]

        syllable_counter_dict[vigerene_message] = 0
        password_dict[vigerene_message] = passw
        
        for sil in common_syllables:
            if sil in vigerene_message:
                syllable_counter_dict[vigerene_message]+=1

    df_rockyou['contraseñas'].apply(check_password)


    vigerene_message= max(syllable_counter_dict, key=syllable_counter_dict.get)
    correct_password = password_dict[vigerene_message]
    print(f"La palabra cifrada con el vigérene es: {vigerene_message}, con la contraseña : {correct_password}") 
    
    return {
        "message": vigerene_message,
        "password":correct_password
    }
