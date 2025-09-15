import requests

BASE_URL = "https://app.tensor.cl/apiuser"  

def api_login(email, password):
    url = f"{BASE_URL}/auth/login"
    data = {"email": email, "password": password}
    try:
        response = requests.post(url, data=data)
        print("Status code API:", response.status_code, flush=True)  
        print("Respuesta API:", response.text, flush=True)           
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        print("Error conexión API:", e, flush=True)
        return None


def api_get_user(access_token):
    url = f"{BASE_URL}/auth/user"
    headers = {"Authorization": f"Bearer {access_token}"}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        print("Error conexión API:", e)
        return None
