from decouple import config

class Config:
    FLASK_ENV = config('FLASK_ENV', default='development')
    
class Config:
    SECRET_KEY=config('SECRET_KEY')

class DevelopmentConfig(Config):
    DEBUG= True

config ={
    'development' : DevelopmentConfig
}