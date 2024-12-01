from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Util.Padding import pad, unpad
import requests
import base64

# Constants
SERVER_URL = "http://127.0.0.1:5000"
# Symmetric key for AES
AES_KEY = b'secretkey1234567'

# Add RSA key pair genration function
def generate_rsa_keypair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# Add RSA key pair Encryption functioin
def rsa_encrypt(public_key, data):
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    return cipher.encrypt(data)

# Add RSA Decryption key pair function
def rsa_decrypt(private_key, encrypted_data):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    return cipher.decrypt(encrypted_data)


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

#Fetch Message Function
def fetch_message():
    try:
        response = requests.get(f"{SERVER_URL}/get_message")
        print("Fetch Message Response:", response.json())
    except Exception as e:
        print("Error fetching message:", str(e))


if __name__ == "__main__":
    send_key("Hello, Secure world")
    fetch_key()