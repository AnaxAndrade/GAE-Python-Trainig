# -*- coding: utf-8 -*-

import webapp2

class PaginaInicial(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('App Engine, pa fronta!, Moo nu ta fossi?!!')


app = webapp2.WSGIApplication([
    ('/', PaginaInicial),
], debug=True)
