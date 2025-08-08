import requests
import time

API_KEY_SANDBOX = "8514b26baac776b19b922036f1e9a8186069b2443ac4afc9f06935eccf051791a887ee1bbaf7889ad125fe51a9dcda7d"  # <--- Pega aquí tu API KEY
CLIENT_ID_SANDBOX = "MNhRftQ9Qui2raCjqnN5wA"  # <--- Pega aquí tu CLIENT ID

def crear_payment_link_sandbox(correo, descripcion, monto):
    url = "https://api.sandbox.airwallex.com/api/v1/pa/payment_links/create"
    merchant_order_id = f"{correo}_{int(time.time())}"
    headers = {
        "Authorization": f"Bearer {API_KEY_SANDBOX}",
        "x-client-id": CLIENT_ID_SANDBOX,
        "Content-Type": "application/json"
    }
    payload = {
        "amount": int(monto * 10),  # Monto en centavos
        "currency": "USD",
        "merchant_order_id": merchant_order_id,
        "customer": {
            "email": correo
        },
        "description": descripcion,
        "return_url": "https://bizplandev.com/thankyou"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

# PRUEBA:
respuesta = crear_payment_link_sandbox("prueba@correo.com", "100 Tokens BPDev", 20)
print(respuesta)
