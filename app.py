from flask import Flask

app = Flask(__name__)


@app.get("/")
def hello():
    return {"message": "Hello from Instana (profiling) World"}


if __name__ == "__main__":
    app.run()
