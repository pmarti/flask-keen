from keen.client import KeenClient


class Keen(object):
    """Thin wrapper around KeenClient"""
    def __init__(self, app=None):
        # self.app = app
        self.client = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        # self.app = app
        self.client = KeenClient(
            project_id=app.config.get('KEEN_PROJECT_ID'),
            read_key=app.config.get('KEEN_READ_KEY'),
            write_key=app.config.get('KEEN_WRITE_KEY'),
        )

    def __getattr__(self, item):
        return getattr(self.client, item)
