import base64
import sys
from flask import Flask, jsonify


def encode_url(url):
    return base64.b64encode(url.encode("utf-8"))

def test_log_output(event=None, context=None):
    print(event)
    return 0



app = Flask(__name__)

# Sample task data (in-memory data store)
tasks = [
    {"id": 1, "title": "Task 1", "description": "Do something important.", "completed": False},
    {"id": 2, "title": "Task 2", "description": "Do something else.", "completed": True},
    # Add more tasks here...
]

@app.route('/api/tasks', methods=['GET'])
def get_all_tasks():
    try:
        return jsonify(tasks)
    except Exception as e:
        return jsonify({"message": "Something went wrong"+str(e)}), 500

@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    try:
        task = next((task for task in tasks if task['id'] == task_id), None)
        if task:
            return jsonify(task)
        else:
            return jsonify({"message": "Task not found"}), 404
    except Exception as e:
        return jsonify({"message": "Something went wrong"+str(e)}), 500

if __name__ == "__main__":
    # URL = sys.argv[1]
    # encoded_url = encode_url(URL)
    # event = {"data": encoded_url}
    # test_log_output(event, None)
    app.run(debug=True)