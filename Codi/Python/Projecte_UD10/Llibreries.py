import requests
import hashlib
import time
# consulta que funciona: http://gateway.marvel.com/v1/public/comics?ts=1&apikey=74fa62381ab90791437b2c1da6003dfc&hash=d92cc884b914834ee8690f75b34e7ac1
def obtener_personaje_marvel(ts, public_key, hash1, character_name):
    base_url = "https://gateway.marvel.com/v1/public/characters"
    params = {
        "ts": ts,
        "apikey": public_key,
        "hash": hash1,
        "name": character_name
    }
    results=[]
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if response.status_code == 200:
            results = data["data"]["results"]
            if results:
                return results
            else:
                return None
        else:
            error_message = data["message"]
            print(f"Error en la solicitud: {error_message}")
            return None
    
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {str(e)}")
        return None
