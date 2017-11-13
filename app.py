from flask import Flask;
import flask;
from flask import request;
import mysql.connector;
import datetime
app = Flask(__name__)

def trackUser(addr):
    addr=request.environ['REMOTE_ADDR']
    cnx = mysql.connector.connect(user='root', password='drwssp',
                              host='localhost',
                              database='ruoblog')
    addVisit=("INSERT INTO visit (ipv4, time) \
        VALUES(%s, %s)")

    data_visit=(addr, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    cur=cnx.cursor()
    cur.execute(addVisit, data_visit)
    cnx.commit()
    cnx.close()
def getArticle():
    cnx = mysql.connector.connect(user='root', password='drwssp',
                              host='localhost',
                              database='ruoblog')
    cur = cnx.cursor()
    query="SELECT title, body FROM article"
    cur.execute(query)
    row=cur.fetchone()
    title=row[0]
    body=row[1]


    cnx.close()
    return [title, body]

def getComments():
    cnx = mysql.connector.connect(user='root', password='drwssp',
                              host='localhost',
                              database='ruoblog')
    cur = cnx.cursor()
    query="SELECT comment, time FROM comment"
    cur.execute(query)
    comments=[]
    for (comment, time) in cur:
        comments.append({'comment': comment, 'time': time})

    cnx.close()
    return comments;

@app.route('/', methods=['GET', 'POST'])
def renderArticle():
    addr=request.environ['REMOTE_ADDR']
    trackUser(addr)
    article=getArticle()
    comments=getComments()
    return flask.render_template('article.html',title=article[0], body=article[1], comments=comments)

@app.route('/comment', methods=['GET', 'POST'])
def comment():
    cnx = mysql.connector.connect(user='root', password='drwssp',
                              host='localhost',
                              database='ruoblog')
    cur = cnx.cursor()
    queryComment=("INSERT INTO comment (ipv4, time, comment) \
        VALUES(%s, %s, %s)")
    comment_data=(request.environ['REMOTE_ADDR']\
        , datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')\
        , request.form['comment'])
    cur.execute(queryComment, comment_data)
    cnx.commit()
    cnx.close()
    
    return request.form['comment']+"<br>"+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')






