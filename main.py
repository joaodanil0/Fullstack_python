import cherrypy
import os, os.path
from examles import ex01, ex02, ex03, ex04, ex05, ex06, ex07


conf = {'/':{'tools.sessions.on':True, 'tools.staticdir.root': os.path.abspath(os.getcwd())},
        '/static':{'tools.staticdir.on': True, 'tools.staticdir.dir': './public'}
 }

# cherrypy.quickstart(ex04.HelloWorld())
# cherrypy.quickstart(ex06 .HelloWorld(), '/', conf)

conf2 = {'/': {
              'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
              'tools.sessions.on': True,
              'tools.response_headers.on': True,
              'tools.response_headers.headers': [('Content-Type', 'text/plain')],
              }
        }

cherrypy.quickstart(ex07.StringGeneratorWebService(), '/', conf2)