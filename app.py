from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)


def create_password(length=12, uppercase=True, lowercase=True, numbers=True, special=True):
    chars = ''

    if uppercase:
        chars += string.ascii_uppercase
    if lowercase:
        chars += string.ascii_lowercase
    if numbers:
        chars += string.digits
    if special:
        chars += '!@#$%^&*()_+-=[]{}|;:,.<>?'

    if not chars:
        chars = string.ascii_letters + string.digits

    pwd = ''.join(random.choice(chars) for _ in range(length))
    return pwd


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    try:
        length = int(data.get('length', 12))
        if length < 4:
            length = 4
        elif length > 50:
            length = 50

        # настройки
        uppercase = data.get('uppercase', True)
        lowercase = data.get('lowercase', True)
        numbers = data.get('numbers', True)
        special = data.get('special', True)

        password = create_password(length, uppercase, lowercase, numbers, special)
        return jsonify({'password': password})

    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
