Example harness to run a pipe2py generated pipe on Google App Engine
====================================================================

Installation
------------

  * git clone git@github.com:ggaughan/testpipe.git

  * cd testpipe

  * git clone git@github.com:ggaughan/pipe2py.git

Include your pipe module
------------------------
Use `pipe2py` to compile your Yahoo pipe into a Python module

Copy the pipe module into `testpipe/`

Replace references to the example pipe (UuvYtuMe3hGDsmRgPm7D0g) 
in `main.py` with your pipe id

Run via the App Engine develpment web server
--------------------------------------------
google_appengine/dev_appserver.py testpipe/

Test in the browser
-------------------
http://localhost:8080/?name=Steen

Upload to Google App Engine
---------------------------
See http://code.google.com/appengine/docs/python/gettingstarted/uploading.html
