import requests

BASE_URL = "http://app.tensor.cl/p8080/apiuser"  # Cambia TU_DOMINIO por tu dominio real

def api_login(email, password):
    url = f"{BASE_URL}/auth/login"
    data = {"email": email, "password": password}
    try:
        response = requests.post(url, data=data)
        print("Status code API:", response.status_code, flush=True)  # <--- print
        print("Respuesta API:", response.text, flush=True)           # <--- print
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        print("Error conexión API:", e, flush=True)
        return None


def api_get_user(access_token):
    """Hace GET a /auth/user para obtener info del usuario"""
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
