import unittest
from todo_project import app, db, bcrypt
from todo_project.models import User

class BasicTests(unittest.TestCase):

    # Configuração antes de cada teste
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Banco em memória
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    # Teste de rota principal
    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    # Teste de criação de usuário
    def test_create_user(self):
        with app.app_context():
            # user = User(username="testuser", password="hashedpassword")
            hashed_password = bcrypt.generate_password_hash("testpassword").decode("utf-8")
            user = User(username="testuser", password=hashed_password)
            db.session.add(user)
            db.session.commit()

            saved_user = User.query.filter_by(username="testuser").first()
            self.assertIsNotNone(saved_user)

    # Cleanup após cada teste
    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

if __name__ == "__main__":
    unittest.main()
