from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/process_audio', methods=['POST'])
def process_audio():
    data = request.json
    if not data or 'url' not in data:
        return jsonify({"error": "No URL provided"}), 400
    
    url = data['url']
    script_dir = os.path.dirname(os.path.abspath(__file__))
    download_script = os.path.join(script_dir, 'download.py')
    
    result = subprocess.run(['python', download_script, url], capture_output=True, text=True)
    
    if result.returncode == 0:
        return jsonify({"message": "Audio processed successfully", "output": result.stdout})
    else:
        return jsonify({"error": "Audio processing failed", "output": result.stderr}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
