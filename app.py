from flask import Flask, render_template, request
from models import create_post, get_posts

# SERVER OBJECT
app = Flask(__name__)

# ROUTE - TELLS WHAT DATA NEEDS TO BE SEND BACK TO THE USER BASED ON INFO SENT TO THE SERVER
@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        name = request.form.get('name')
        post = request.form.get('post')
        create_post(name, post)
    
    posts = get_posts()
    
    return render_template('index.html', post=posts)

if __name__ == '__main__':
    app.run(debug=True)
