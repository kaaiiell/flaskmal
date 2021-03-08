from flask import Flask
from flask import render_template
from flask import request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import test
import youtube

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)
y = test.get_current_year()
s = test.get_current_season()

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200),nullable=False)
    content = db.Column(db.Text,nullable = False)
    author = db.Column(db.String(20),nullable = False,default = "N/A")
    date_post = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)

    def __repr__(self):
        return 'Blog Post ' + str(self.id)

@app.route('/') ##on local host for now
def index():
    #return "</h1>Home Page</h1>"
    return render_template('index.html')

##test data
all_posts = [
    {
        'title': 'Post 1',
        'content': 'content of post 1',
        'author':'asdfasdf'
    },
    {
        'title': 'Post 2',
        'content': 'content of post 2'
    }
]

@app.route('/posts',methods=['GET','POST'])
def anime():
#    if request.method == 'POST':
#        post_title = request.form['title']
#        post_content = request.form['content']
#        post_author = request.form['author']
#        new_post = BlogPost(title = post_title,content = post_content,author=post_author)
#        try:
#            db.session.add(new_post)
#            db.session.commit()
#            return redirect('/posts')
#        except:
#            return "There was an error"
#    else:
    option = "Title"
    alldb_posts = BlogPost.query.order_by(BlogPost.date_post).all()
    return render_template('posts.html',posts = alldb_posts,anime=test.seasonal(option),year=y,season=s,today=test.get_current_day(),option=option,allyear=y)

@app.route('/posts/delete/<int:id>')
def delete(id):
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts')


@app.route('/posts/edit/<int:id>',methods=['GET','POST'])
def edit(id):
    post = BlogPost.query.get_or_404(id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        post.author = request.form['author']
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('edit.html',post = post)

@app.route('/posts/new_post',methods=['GET','POST'])
def add_post():
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        new_post = BlogPost(title = post_title,content = post_content,author=post_author)
        try:
            db.session.add(new_post)
            db.session.commit()
            return redirect('/posts')
        except:
            return "There was an error"

    else: 
        return render_template('new_post.html')

@app.route('/posts/more_info/<int:mal_id>',methods=['GET','POST'])
def get_info(mal_id):
    url = "https://www.youtube.com/results?search_query="
    anime_info = test.animeinfo(mal_id)
    return render_template('more_info.html',info = anime_info,songs = url)
        
@app.route('/posts/season',methods=['GET','POST'])
def season_update():
    year = request.form['year']
    season = request.form['season']
    option = request.form['option']
    anime = test.seasonal_input(year,season,option)
    alldb_posts = BlogPost.query.order_by(BlogPost.date_post).all()
    return render_template('posts.html',posts = alldb_posts,anime=anime,year=year,season=season,today=test.get_current_day(),option=option,allyear=y)

#@app.route('/posts/schedule/<string:option>',methods=['GET','POST'])
#def schedule(option):
#    anime = test.seasonal(option)
#    return render_template('schedule.html',anime=anime)

@app.route('/posts/schedule',methods=['GET','POST'])
def schedule():
    year = request.form['year1']
    season = request.form['season1']
    option = request.form['option1']
    anime = test.seasonal_input(year,season,option)
    return render_template('schedule.html',anime=anime)




 
@app.route('/home')
def hello():
    return "Hello world "

@app.route('/home/<string:ans>') ##dynamic urls having differnet images with dif ids
def answer(ans):
    return "Hello world " + ans

@app.route('/home/users/<string:name>/posts/<int:id>')
def posts(name,id):
    return "Hello "+name+" post id: "+str(id)

@app.route('/onlyget',methods=['GET','POST'])
def get_req():
    return "You can only get this webpage"

if (__name__) == "__main__":
    app.run(debug=True)