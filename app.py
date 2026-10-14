from flask import Flask

# kita inisialisasi Flask dan kita butuh simpan ke suatu variable (bebas tapi kita bakal pakai variabel app)
app = Flask(__name__)

@app.route("/")
def home():
    return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <button>Click Me</button>
        </body>
        </html>
    """

if __name__ == "__main__":
    app.run(debug=True, port=5001)