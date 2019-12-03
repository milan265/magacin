from plugin_framework.plugin import Plugin
from .widgets.magacin import Magacin

class Main(Plugin):

    def __init__(self, spec):
        self._spec = spec

    def get_widget(self, parent=None):
        return Magacin(parent), None, None