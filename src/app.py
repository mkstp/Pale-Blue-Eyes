from flask import Flask, render_template, request
import analyzer

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    submitted_text = 'test'
    score = 'test'
    if request.method == "POST":
        submitted_text = request.form["user_input"]
        score = analyzer.affect_detector(submitted_text)
        analyzer.send_osc_message("127.0.0.1", 2390, "/affect", score[0], score[1])
    return f"""
        <html>
        <head>
            <title>Text Input Page</title>
        </head>
        <body>
            <h2>Enter Text Below:</h2>
            <form method="POST">
                <input type="text" name="user_input" required>
                <button type="submit">Submit</button>
            </form>
            <p><strong>You Entered:</strong> {submitted_text, score[0]}</p>
        </body>
        </html>
    """

if __name__ == "__main__":
    app.run(debug=True)