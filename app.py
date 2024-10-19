from flask import Flask
import os
from datetime import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get server time in IST
    ist_time = datetime.now().astimezone().isoformat()
    # Get top output
    top_output = subprocess.check_output(['top', '-bn1']).decode('utf-8')

    return f"""
    <h1>HTOP</h1>
    <p>Name: Your Full Name</p>
    <p>Username: {os.getlogin()}</p>
    <p>Server Time (IST): {ist_time}</p>
    <h2>TOP Output</h2>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
