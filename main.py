from flask import Flask, jsonify, request

app = Flask("__name__")


@app.route('/')
def func():
    return "Use / predict"


@app.route('/predict', methods=['POST'])
def home():
    input = request.form.get('encoded_image')
    flag = 0
    if flag == 0:
        result = 'BENIGN'
        flag = 1
    else:
        result = 'MALIGNANT'
        flag = 0

    return jsonify({'result': str(result)})


if __name__ == "__main__":
    app.run(debug=True)
