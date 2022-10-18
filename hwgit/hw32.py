from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def rand():
    rand1 = random.randint(1, 1000)

    return f' Random number:{rand1}'


if __name__ == '__main__':
    app.run()