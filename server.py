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
  

if __name__ == "__main__":
    app.run(port=5000)
