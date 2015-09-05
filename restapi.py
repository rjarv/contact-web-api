from contactsapi.controllers.personcontroller import Person
import cherrypy
import os, os.path


def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"


class Api(object):
    def __init__(self):
        self.contacts = Person()

    def _cp_dispatch(self, vpath):
        if len(vpath) == 2:
            vpath.pop(0)
            controller = vpath.pop(0)
            return getattr(self, controller)

        if len(vpath) == 4:
            vpath.pop(0)
            controller = vpath.pop(0)
            cherrypy.request.params['key'] = vpath.pop(0)
            cherrypy.request.params['value'] = vpath.pop(0)
            return getattr(self, controller)

        return vpath


if __name__ == '__main__':
    cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
    cherrypy.config.update("server.conf")

    cherrypy.quickstart(Api(), '/', config="app.conf")