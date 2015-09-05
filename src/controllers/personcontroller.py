# import sqlalchemy necessities
from sqlalchemy import create_engine as _sa_create_engine
from sqlalchemy.orm import sessionmaker as _sa_session_maker
# import local package modules
from ..models.models import Contact as _Contact
from ..helpers import tools as _tools

# this is a cherrypy controller routed to from a cherrypy root
import cherrypy


# meat and bones of the Person controller
class Person(object):
    exposed = True

    def __init__(self):
        self._engine = None
        self._Session = None

    def connect_db(self):
        if self._Session is None:
            # setup connection to the DB
            cherrypy.log('Initializing Database...')
            try:
                self._engine = \
                    _sa_create_engine(cherrypy.request.app.config['Database']['connection_string'], echo=False)
                self._Session = _sa_session_maker(bind=self._engine)
                cherrypy.log('Database connection established.')
            except Exception as e:
                cherrypy.log('Database connection failed to initialize. \r\n %s' % e.message, traceback=True)

    def OPTIONS(self, *args, **kwargs):
        cherrypy.response.headers['Access-Control-Allow-Headers'] = "Content-Type"
        cherrypy.response.headers['Access-Control-Allow-Methods'] = "GET, POST, PUT, DELETE, OPTIONS"
        return

    @cherrypy.tools.json_out()
    def GET(self, **kwargs):
        """
        GETs the contacts based on the query string parameters
        :param kwargs: Model query parameters
        :return: JSON serialized response for RESTful interface
        """
        self.connect_db()
        if len(kwargs) == 0:
            session = self._Session()

            r = session.query(_Contact).all()
            contact_list = _tools.results_to_array(r)

            return {'Contacts': contact_list}

        if kwargs.has_key('key'):
            session = self._Session()
            r = session.query(_Contact).\
                filter(getattr(_Contact, kwargs['key']) == kwargs['value']).\
                all()
            contact_list = _tools.results_to_array(r)

            return {'Contacts': contact_list}

        if ~kwargs.has_key('key'):
            session = self._Session()
            r = session.query(_Contact).filter_by(**kwargs).all()
            contact_list = _tools.results_to_array(r)

            return {'Contacts': contact_list}

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self, *args, **kwargs):
        self.connect_db()
        try:
            session = self._Session()
            new_person_json = cherrypy.request.json
            new_contact = _Contact()
            [setattr(new_contact, a, new_person_json[a]) for a in new_person_json]
            cherrypy.log("Adding %s" % new_person_json)
            session.add(new_contact)
            session.commit()
        except Exception as e:
            cherrypy.log(e.message, traceback=True)
            return {"success": False, "error_message": "%s" % e.message}
        return {"success": True, "data": "%s" % cherrypy.request.json}

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def PUT(self, *args, **kwargs):
        self.connect_db()
        try:
            session = self._Session()
            updated_person_json = cherrypy.request.json
            updated_contact = session.query(_Contact).filter_by(**kwargs).first()
            cherrypy.log("Updating %s with %s" % (updated_contact, updated_person_json))
            [setattr(updated_contact, a, updated_person_json[a]) for a in updated_person_json]
            session.commit()
        except Exception as e:
            cherrypy.log(e.message, traceback=True)
            return {"success": False, "error_message": "%s" % e.message}
        return {"success": True, "data": "%s" % cherrypy.request.json}

    @cherrypy.tools.json_out()
    def DELETE(self, *args, **kwargs):
        self.connect_db()
        try:
            session = self._Session()
            person_to_remove = session.query(_Contact).filter_by(**kwargs).first()
            cherrypy.log("Deleting %s" % person_to_remove)
            session.delete(person_to_remove)
            session.commit()
        except Exception as e:
            cherrypy.log(e.message, traceback=True)
            return {"success": False, "error_message": "%s" % e.message}
        return {"success": True}