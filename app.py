from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <html>
    <head>
        <title>Final Learning Task</title>
    </head>

    <body style="font-family: Arial; text-align: center; margin-top: 100px;">

        <div style="border: 2px solid black; padding: 20px; width: 300px; margin: auto; border-radius: 10px;">
            <h2>🚀 CI/CD PIPELINE</h2>
            <h1 style="color: green;">Hello, World! by Joshua</h1>
            <p>Flask • Docker • GitHub Actions</p>
        </div>

    </body>
    </html>
    """
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
