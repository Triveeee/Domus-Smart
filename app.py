from flask import Flask , render_template
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config[MYSQL_DATABASE_USER] = '5ai-trivellato'
app.config[MYSQL_DATABASE_PASSWORD] = '5ai-trivellato'
app.config[MYSQL_DATABASE_HOST] = '192.168'

mysql = MySQL()

mysql.init_app(app)