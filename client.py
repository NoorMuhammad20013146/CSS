import requests

SERVER_URL = "http://127.0.0.1:5000"

def test_connection():
    try:
        response = response.get(SERVER_URL)
        print("Server Response", response.text)
    except Exception as e:
        print("Error to connecting the server")

if __name__ == "__main__":
    test_connection()