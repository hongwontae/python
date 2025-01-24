from flask import Flask

app = Flask(__name__)

@app.route("/")
def bye():
    return """
    <center>
        <h1>Bye!</h1>
        <p>Hello-world</p>
        <h2>Funcking</h2>
        <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTJ2NmR3dDk5YnpvZ2t3MGVtZmxhcHNubGlvMzdyZjM4OHJ6YmVwYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/EZICHGrSD5QEFCxMiC/giphy.gif" />
    </center>
    """

if __name__ == "__main__":
    app.run()