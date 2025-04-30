# vercel_app.py
from mycollection.mycollection.wsgi import application

# This is needed for Vercel deployment
app = application
