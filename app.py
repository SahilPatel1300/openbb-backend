from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/run-script', methods=['POST'])
def run_script():
    data = request.get_json()
    stock_symbol = data.get('stockSymbol')
    app.logger.info(f"Received request for stock symbol: {stock_symbol}")

    try:
        # Run the Python script with the stock symbol as an argument
        result = subprocess.run(['python', 'main.py', stock_symbol], capture_output=True, text=True)

        if result.returncode != 0:
            raise Exception(f"Python script error: {result.stderr}")

        # Parse the JSON output from the script
        output_data = json.loads(result.stdout)

        app.logger.info(f"Script output: {output_data}")
        return jsonify(output_data)

    except Exception as e:
        app.logger.error(f"Error running script: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)

# Add a route for health checks
@app.route('/healthz')
def health_check():
    return "OK", 200
