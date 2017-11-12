from flask import Flask;
import flask;
from flask import request;
import mysql.connector;

app = Flask(__name__)

@app.route('/')
def renderArticle():
    cnx = mysql.connector.connect(user='root', password='drwssp',
                              host='localhost',
                              database='ruoblog')
    cur = cnx.cursor()
    query="SELECT title, body FROM ARTICLE"
    cur.execute(query)
    row=cur.fetchone()
    title=row[0]
    body=row[1]


    cnx.close()
    return flask.render_template('article.html',title=title, body=body)

@app.route('/comment')
def comment():
    pass