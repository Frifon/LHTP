from datetime import timedelta
import os


basedir = os.path.abspath(os.path.dirname(__file__))


WEATHER_DEFAULT_CITY = "Moscow,Russia"
WEATHER_API_KEY = "793f173c7ad34aabbad214324201401"
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')

SECRET_KEY = 'owljkfw4th34o34iwoeifjef9000woeof'

REMEMBER_TIME_DURATION = timedelta(days = 5)

SQLALCHEMY_TRACK_MODIFICATIONS = False