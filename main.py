"""Example harness to run a pipe2py generated pipe on Google App Engine

   Author: Greg Gaughan (http://www.wordloosed.com) 
"""

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import logging

import cgi

import json

from pipe2py import Context

#The compiled pipe module goes here:
from pipe_UuvYtuMe3hGDsmRgPm7D0g import pipe_UuvYtuMe3hGDsmRgPm7D0g
#in future these should be available from the compiled pipe:
pipe_id='UuvYtuMe3hGDsmRgPm7D0g'
pipe_title = "MP expenses by name"

class PipesEncoder(json.JSONEncoder): 
    """Extends JSONEncoder to add support for date and time properties. 
    """ 
    def default(self, obj): 
        """Tests the input object, obj, to encode as JSON.""" 
        if hasattr(obj, '__json__'): 
            return getattr(obj, '__json__')() 

        if isinstance(obj, datetime.datetime): 
            output = obj.strftime("%Y-%m-%dT%H:%M:%SZ")
            return output   
        elif isinstance(obj, time.struct_time): 
            dt = datetime.datetime.fromtimestamp(time.mktime(obj))
            output = dt.strftime("%Y-%m-%dT%H:%M:%SZ")
            return output
  
        return json.JSONEncoder.default(self, obj) 

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "application/json"
        params = dict([(arg, self.request.get(arg)) for arg in self.request.arguments()])
        context = Context(console=False, inputs=params)
        
        #p = pipe_9420a757a49ddf11d8b98349abb5bcf4(context, None)
        p = pipe_UuvYtuMe3hGDsmRgPm7D0g(context, None)
        
        #Output header (for json) - perhaps push this into the output module - or an app-engine output wrapper module
        self.response.out.write("""{"value":{"title":"%(title)s",
        "description":"Pipes Output",
        "link":"http:\/\/github.com\/ggaughan\/pipe2py",
        "generator":"pipe2py",
        "items":[
        """ % {'title':pipe_title, 'id': pipe_id})
        #todo add: "pubDate":"Fri, 03 Dec 2010 20:46:30 +0000",
        #todo add: "callback":"",

        #Output results
        count = 0
        try:
            for i in p:
                si = json.dumps(i, cls=PipesEncoder)
                if count:
                    self.response.out.write(",")
                self.response.out.write(si)
                count += 1
        except Exception, e:
            logging.error(e)
            self.response.out.write("Error running: %s : " % pipe_id)
            self.response.out.write(e)
            #todo print trace?
            
        #Output footer
        self.response.out.write("""]}, "count":%(count)s}""" % {'count':count})
        

application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()