from flask import Flask, render_template
import requests

BLOG_URL = 'https://api.npoint.io/cd9e64089b1d214c3a20'
ALL_POSTS = requests.get(BLOG_URL).json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=ALL_POSTS)

@app.route('/blog/<int:blog_id>')
def get_blog(blog_id):
    # error handling
    if blog_id > (len(ALL_POSTS) - 1):
        return "Error: No posts that high yet!\n" \
               "Try a lower post id!"

    return render_template('post.html', post=ALL_POSTS[blog_id])

if __name__ == "__main__":
    app.run(debug=True)
