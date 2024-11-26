from flask import Flask, request, jsonify, render_template
import queue

app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'templates'))
key_queue = queue.Queue() # for key exchange
message_queue = queue.Queue() #forencrypted  message exchange


# Serve the index.html file
@app.route('/')
def home():
    try:
        return render_template('index.html')
    except Exception as e:
        return jsonify({"error":str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
