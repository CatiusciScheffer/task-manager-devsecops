from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import logging
import sys
import os



app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "default-secret-key")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Configurar logging para syslog
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("security.log"),  # Log em arquivo local
                        logging.StreamHandler(sys.stdout)  # Exibir logs no console
                    ])

logger = logging.getLogger() # Criando o objeto logger


db = SQLAlchemy(app)


login_manager = LoginManager(app)
login_manager.login_view = 'login' 
login_manager.login_message_category = 'danger'

bcrypt = Bcrypt(app)

# Always put Routes at end
from todo_project import routes