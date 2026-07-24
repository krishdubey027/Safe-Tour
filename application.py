# AWS Elastic Beanstalk entry point
# EB requires a file named application.py with a variable named 'application'
from app import app as application

if __name__ == '__main__':
    application.run()
