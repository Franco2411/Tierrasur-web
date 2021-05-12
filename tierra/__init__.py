from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        MI_KEY='mi_llave'
    )

    from . import main
    app.register_blueprint(main.bp)

    @app.route('/prueba')
    def prueba():
        return 'Server funcionando'
    
    return app