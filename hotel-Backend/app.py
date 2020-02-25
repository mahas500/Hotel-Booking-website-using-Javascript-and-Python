from flask import Flask
from flask_mail import Mail, Message
from flask_bootstrap import Bootstrap
from flask_cors import CORS

app = Flask(__name__)
mail=Mail(app)
Bootstrap(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'mahashabdemanik@gmail.com'
app.config['MAIL_PASSWORD'] = 'evrdwyscgmtllqad'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
CORS(app)



