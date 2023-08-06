import base64
import sys
from flask import Flask, jsonify

app = Flask(__name__)

# Sample task data (in-memory data store)
tasks = [
    {"id": 1, "title": "Task 1", "description": "Do something important.", "completed": False},
    {"id": 2, "title": "Task 2", "description": "Do something else.", "completed": True},
    # Add more tasks here...
]

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)


def encode_url(url):
    return base64.b64encode(url.encode("utf-8"))

def test_log_output(event=None, context=None):
    print(event)
    return 0

if __name__ == "__main__":
    # URL = sys.argv[1]
    # encoded_url = encode_url(URL)
    # event = {"data": encoded_url}
    # test_log_output(event, None)
    app.run(debug=True)