from distutils.core import setup

setup(name='contactsapi',
      version='1.0',
      author='Richard Jarvis',
      description='''Simple RESTful API to manage Contacts DB. Uses SqlAlchemy, CherryPy
      and Postgresql DB backend.''',
      package_dir={ 'contactsapi': 'src' },
      packages=['contactsapi',
                'contactsapi.controllers',
                'contactsapi.models',
                'contactsapi.helpers'],
      py_modules=['contactsapi.controllers.personcontroller',
                  'contactsapi.helpers.tools',
                  'contactsapi.models.models'],
      requires=['cherrypy', 'sqlalchemy']
)