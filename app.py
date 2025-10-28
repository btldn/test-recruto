from flask import Flask, request, Response

app = Flask(__name__)

@app.get("/")
def hello():
    name = request.args.get("name", "Гость").strip()
    message = request.args.get("message", "Здравствуй").strip()
    text = f"Hello {name}! {message}!"
    return Response(text, mimetype="text/plain; charset=utf-8")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)