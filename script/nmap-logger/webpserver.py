import cherrypy

class Gui:

    @cherrypy.expose
    def index(self):
        return 'Ciao mondo!'


cherrypy.quickstart(Gui())
