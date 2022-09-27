from flask_app import app

@app.route('/')
def server_test():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)