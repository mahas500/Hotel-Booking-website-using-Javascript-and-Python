from flask import Flask
from flask_mail import Mail, Message
from flask_bootstrap import Bootstrap
from flask_cors import CORS
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'F:\GitHub\Web-Development-CA\hotel-Backend\static\images'

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
mail = Mail(app)
Bootstrap(app)
app.secret_key = "manik123"

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'mahashabdemanik@gmail.com'
app.config['MAIL_PASSWORD'] = 'evrdwyscgmtllqad'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
CORS(app)
