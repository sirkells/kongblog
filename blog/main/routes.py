from flask import Blueprint, render_template, request
from flask_login import login_user, current_user, logout_user, login_required
from blog.models import User, Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
@login_required #decorator that allows only login users to access the account page
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)#page sorted by date added
    return render_template('home.html', posts=posts)


@main.route("/about")
@login_required
def about():
    return render_template('about.html', title='About')