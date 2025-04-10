from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    try:
        luku = float(luku)

        tilakoodi = 200
        alkuluku = True

        if luku % 1:
            alkuluku = False
            for i in range(2, luku):
                if luku % i == 0:
                    alkuluku = False

        return jsonify({"luku":luku, "alkuluku": alkuluku})

    if __name__ == '__main__':
        app.run(port=3000)