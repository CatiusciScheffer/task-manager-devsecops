from todo_project import app, db

with app.app_context():
    db.create_all()
    print("Banco de dados criado com sucesso!")
