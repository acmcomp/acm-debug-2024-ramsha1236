from flask import Flask, jsonify
from dataclasses import dataclass


class User:
    x={
   "name": "str"
    "age": "int"
    } #declared a variable
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


app = Flask(__name__)


@app.route("/data", methods=["GET"])
def get_data():
    user = User(name="Alice", age=30)
    return user


if __name__ == "__main__":
    app.run(debug=True)
