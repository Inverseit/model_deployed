from flask import Flask, request, jsonify
from predict import predict # importing

app = Flask(__name__)
app.config['DEBUG'] = False

@app.route('/predict', methods=['POST'])
def predict_route():
    if request.is_json:
        try:
            request_data = request.get_json()
            result = predict(request_data)

            # Return the result
            return jsonify(result), 200
        except Exception as e:
            # If an error occurs, return an error message
            return jsonify({'error': str(e)}), 400
    else:
        return jsonify({'error': 'Request must be JSON'}), 400

if __name__ == '__main__':
    app.run(debug=True)  # Starts the Flask web server
