#!/usr/bin/env python
#
import webapp2
from google.appengine.ext.webapp import template
import os

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.write('Hello world!')

        path = os.path.join(os.path.dirname(__file__), 'templates/test.html')
        print path
        template_values ={}
        html=template.render(path,template_values)

        print(html)
        self.response.write(html)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
