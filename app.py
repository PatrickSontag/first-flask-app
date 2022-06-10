from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home_page():
    html = """
    <html>
        <body>
            <h1>Wilkommen!!</h1>
            <p>You have landed</p>
            <a href='/hello'>Go to Hello page</a>
        </body>
    </html>
    """
    return html

@app.route('/hello')
def say_hello():
    html = """
    <html>
        <body>
            <h1>Hello!</h1>
            <p>This is the hello page</p>
        </body>
    </html>
    """
    return html

@app.route('/goodbye')
def say_goodbye():
    return "goodbye"

@app.route('/search')
def search():
    print(request.args)
    return "SEARCH PAGE"

@app.route("/add-comment")
def add_comment_form():
    return """
    <h1>Add Comment</h1>
    <form method="POST">
        <input type='text' placeholder='comment' name='comment'/>
        <input type='text' placeholder='username' name='username'/>
        <button>Submit</button>
    </form>
    """

@app.route("/add-comment", methods=["POST"])
def save_comment():
    comment = request.form["comment"]
    username = request.form["username"]
    return f"""
        <h1>Wanted to save comment</h1>
        <ul>
            <li>Username: {username} </li>
            <li>Comment: {comment} </li>
        </ul>
    """

@app.route("/r/<subreddit>")
def visit_subreddit(subreddit):
    return f"<h1>Here you are, at the {subreddit} subreddit!</h1>"

POSTS = {
    1: "Taco time!",
    2: "Shallow, by Lady Gaga",
    3: "vanlife",
    4: "Toastmasters"
}

@app.route("/posts/<int:id>")
def find_post(id):
    post = POSTS.get(id, "Post not found")
    return f"<h1>{post}</h1>"