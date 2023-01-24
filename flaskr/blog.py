from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required

from flaskr.post import Post
from bson import ObjectId

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    cursor = Post.objects()
    posts = []
    for document in cursor:
        posts.append(document)
    return render_template('blog/index.html', posts=posts)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            post = Post(author_id=g.user, title=title, body=body)
            post.save()
            
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')

def get_post(id, check_author=True):
    post = Post.objects(id=ObjectId(id)).first()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['author_id']['id'] != g.user.id:
        abort(403)

    return post

@bp.route('/<id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            post = Post.objects(id=ObjectId(id)).first()
            post.title = title
            post.body = body
            post.save()

            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)

@bp.route('/<id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    post = Post.objects(id=ObjectId(id)).first()
    post.delete()

    return redirect(url_for('blog.index'))

@bp.route("/favicon.ico")
def favicon():
    return "", 200