import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'EEbh%ScF#m6omWe4a*jFuvJMi%nLrCRYBSSXC*L!Z7MqaAa@wUnY5VJ%!ci6YcnEGnwBo6kvpB!e!7aCegSPo!&&fjso5z4rG4XJR5#AT^RHvoBRTNkK%^7HnXZ29cLF4^iE6LnYVFqu%vD7#y3twW7L6h8Zc43!%YxkGDwYtrg$SCQjjMB5czYrBS6f!foT@yZ$XGcXR#mPX!s6xV@B4PzGtSgy@4W3caVWxcToyrJ@zLodLngp$%VrrDn#3U@o'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:////var/lib/cycleflask/data/app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
