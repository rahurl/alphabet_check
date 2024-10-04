# Using flask framework to create a simple alphabet check
from flask import Flask, request, jsonify
import string

app = Flask(__name__)

@app.route('/check_alphabet', methods=['POST'])
def check_alphabet():
    # Pass input string as request body in json
    data = request.json
    if 'input_string' not in data:
        return jsonify({"error": "input string not provided"}), 400

    input_string = data['input_string']
    # Storing the all alphabets in lowercase to compare with the string
    alphabet_set = set(string.ascii_lowercase)

    # Create a set of characters in the input string, ignoring case
    input_set = set(input_string.lower())

    # Check if all alphabet characters are present
    contains_all = alphabet_set.issubset(input_set)

    return jsonify({"contains_all_alphabet": contains_all})

if __name__ == '__main__':
    app.run(debug=True)
