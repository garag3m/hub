from django.apps import AppConfig


class CtrlPConfig(AppConfig):
    name = 'app.ctrl_p'

    def ready(self):
        from . import signals