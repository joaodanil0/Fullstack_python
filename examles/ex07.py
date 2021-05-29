import random
import string

import cherrypy


@cherrypy.expose
class StringGeneratorWebService(object):

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def GET(self):
        return cherrypy.session['mystring']

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
      data = cherrypy.request.json
      some_string = ''.join(random.sample(string.hexdigits, int(data["length"])))
      cherrypy.session['mystring'] = some_string
      return {"value": some_string}

    def PUT(self, another_string):
        cherrypy.session['mystring'] = another_string

    def DELETE(self):
        cherrypy.session.pop('mystring', None)