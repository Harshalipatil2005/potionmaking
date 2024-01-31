from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rest/potions', methods=['POST'])
def check_potion():
    potion_name = request.form.get('potionName', '')

    if potion_name.lower() == 'secretpotion':
        return 'You found the flag! VishwaCTF{pr3^@r!c@t3_3l!x!r}'
    else:
        return 'Not a secret potion!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)