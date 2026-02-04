from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the home page ("/")
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Optional: Run the app directly if the script is executed
if __name__ == '__main__':
    app.run(debug=True)
