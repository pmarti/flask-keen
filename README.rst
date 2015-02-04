==========
flask-keen
==========

Flask-Keen is a thin wrapper around `KeenClient`. Just add the project id, write read keys
to the config and you're good to go!


Example::


    from flask import (
        Flask,
        request,
    )
    from flask.ext.keen import Keen
    
    app = Flask(__name__)
    app.config['KEEN_PROJECT_ID'] = ''
    app.config['KEEN_READ_KEY'] = ''
    app.config['KEEN_WRITE_KEY'] = ''
    keen = Keen(app)
    
    @app.route('/')
    def index():
        keen.add_event('hit', {
            'ip': request.remote_addr
        })
        return 'Hit logged', 200
    
    if __name__ == '__main__':
        app.run()
