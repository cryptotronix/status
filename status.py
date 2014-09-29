from google.appengine.api import users

import webapp2
import json
import urllib2


class MainPage(webapp2.RequestHandler):

    def get(self):
        # Checks for active Google account session
        user = users.get_current_user()

        if user:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Number of CryptoCapes: ' + self.get_num_cryptocapes())
        else:
            self.redirect(users.create_login_url(self.request.uri))

    def get_num_cryptocapes(self):
        rsp = urllib2.urlopen('https://www.sparkfun.com/products/12773.json')
        html = rsp.read()
        j = json.loads(html)

        return j['quantity']



application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
