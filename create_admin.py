from getpass import getpass
import sys

from webapp import create_app
from webapp.model import User, db

app = create_app()

with app.app_context():
    username = input('your name user : ')

    if User.query.filter(User.username == username).count():
        print('ups already taken')
        sys.exit(0)

    password1 = getpass('your pass : ')
    password2 = getpass('just in case .. your pass again : ')
    if not password2 == password2:
    	print ('ups !!!')
    	sys.exit(0)

    new_user = User(username=username, role='admin')
    new_user.set_password(password1)

    db.session.add(new_user)
    db.session.commit()
    print('wow new awesome user with id {} added'.format(new_user.id))