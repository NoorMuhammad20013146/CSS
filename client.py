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

#add send message function
def send_message(message):
    try:
        response = requests.post(f"{SERVER_URL}/send_message", json={"message": message})
        print("Send Message Response:", response.json())
    except Exception as e:
        print("Error sending message:", str(e))

if __name__ == "__main__":
    send_key("dummy_public_key")
    fetch_key()