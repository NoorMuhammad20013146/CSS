from flask import Flask, request, jsonify, render_template
import queue

app = Flask(__name__)
key_queue = queue.Queue() # for key exchange
message_queue = queue.Queue() #forencrypted  message exchange


# Serve the index.html file
@app.route('/')
def home():
    return render_template('index.html')
