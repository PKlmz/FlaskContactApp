import os
#import random, string
#random_string = "".join([random.choice(string.printable) for _ in range(24)])
#print(random_string)

SECRET_KEY = "trs3HE|HIQjT=g*x$a]f<:Nn"

FB_APP_ID = 819775606968457

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
