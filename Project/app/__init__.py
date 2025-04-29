from flask import Flask
def create_app():
    app = Flask(name)
    app.config['SECRET_KEY'] = 'dev-key-123' 

    @app.route('/')
    def home():
        return"Hello World!"
    
    return app
