import os
import unittest

from views import app, db
from _config import basedir
from model import User

TEST_DB = 'test.db'


class AllTests(unittest.TestCase):

    # Setup

    # exec prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, TEST_DB)
        self.app = app.test_client()
        db.create_all()

    # exec after each test
    def tearDown(self):
        db.drop_all()

    # start each test with 'test'
    def test_user_setup(self):
        new_user = User("cleon", "cleon@cleon.com", "cleonmarx")
        db.session.add(new_user)
        db.session.commit()
        test = db.session.query(User).all()
        for t in test:
            t.name
        assert t.name == "cleon"

    def test_form_is_present_on_login_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Please login to access your task list', response.data)

    # login helper method
    def login(self, name, password):
        return self.app.post('/', data=dict(name=name, password=password), follow_redirects=True)

    def test_users_cannot_login_unless_registered(self):
        response = self.login('foo', 'bar')
        self.assertIn(b'Invalid username or password.', response.data)

    # registration helper method
    def register(self, name, email, password, confirm):
        return self.app.post(
            'register/',
            data=dict(name=name, email=email, password=password, confirm=confirm),
            follow_redirects=True
        )

    def test_users_can_login(self):
        self.register('Cleones', 'cleon@trantor.com', 'etodemer', 'etodemer')
        response = self.login('Cleon', 'etodemer')
        self.assertIn('Welcome', response.data)

    def test_invalid_form_data(self):
        self.register('Cleones', 'cleon@realpython.com', 'etodemer', 'etodemer')
        response = self.login('alert("alert box!");', 'foo')
        self.assertIn(b'Invalid username or password', response.data)

    def test_form_is_present_on_register_page(self):
        response = self.app.get('register/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Please register to access the task list', response.data)

    def test_under_registration(self):
        response = self.app.get('register/', follow_redirects=True)
        response = self.register('Cleones', 'cleon@trantor.com', 'etodemer', 'etodemer')
        self.assertIn(b'Thanks for registering. Please login.', response.data)

    def test_user_registration_error(self):
        self.app.get('register/', follow_redirects=True)
        self.register('Cleones', 'cleon@trantor.com', 'etodemer', 'etodemer')
        self.app.get('register/', follow_redirects=True)
        response = self.register('Cleones', 'cleon@trantor.com', 'etodemer', 'etodemer')
        self.assertIn(b'That usersame is already taken. Please choose a different username.', response.data)

if __name__ == "__main__":
    unittest.main()
