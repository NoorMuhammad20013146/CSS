from flask import Flask, request, jsonify, render_template
import queue
import os

app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'template'))
key_queue = queue.Queue() # for key exchange
message_queue = queue.Queue() #forencrypted  message exchange


# Serve the index.html file
@app.route('/')
def home():
    return render_template('index.html')
  
@app.route('/exchange_key', methods=['POST'])
def exchange_key():
    data = request.json
    if 'key' not in data:
        return jsonify({"error": "No key provided"}), 400
    key_queue.put(data['key'])
    return jsonify({"status": "Key received"}), 200

@app.route('/get_key', methods=['GET'])
def get_key():
    if not key_queue.empty():
        return jsonify({"key": key_queue.get()}), 200
    return jsonify({"status": "No keys available"}), 200

@app.route('/send_message', methods=['POST'])
def send_message():
    
if __name__ == "__main__":
    app.run(port=5000)
