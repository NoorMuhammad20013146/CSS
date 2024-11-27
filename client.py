import requests

SERVER_URL = "http://127.0.0.1:5000"
#send key function
def send_key(public_key):
    try:
        response = requests.post(f"{SERVER_URL}/exchange_key", json={"key": public_key})
        print("Send Key Response:", response.json())
    except Exception as e:
        print("Error sending key:", str(e))

#fecth key function
def fetch_key():
    try:
        response = requests.get(f"{SERVER_URL}/get_key")
        print("Fetch Key Response:", response.json())
    except Exception as e:
        print("Error fetching key:", str(e))

if __name__ == "__main__":