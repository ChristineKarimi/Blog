from flask import render_template, redirect, request, url_for, abort
from flask_login import login_required, current_user

from ..models import User
from .forms import BlogForm, ReviewForm
from . import admin
from ..models import Blog, Review

from .. import db


def check_user():

    if current_user.id != 1:

        abort (403)

    return render_template('admin/dashboard.html')


from flask import render_template, redirect, request, url_for, abort
from flask_login import login_required, current_user

from ..models import User
from .forms import BlogForm, ReviewForm
from . import admin
from ..models import Blog, Review

from .. import db


def check_user():

    if current_user.id != 1:

        abort (403)

    return render_template('admin/dashboard.html')


@admin.route('/blog/new', methods=['GET', 'POST'])
def new_blog():

    form = BlogForm()

    if form.validate_on_submit():

        title = form.title.data
        description = form.description.data
        blog = form.blog.data

        new_blog = Blog(blog=blog, title=title, description=description)

        new_blog.save_blog()

        return redirect(url_for('main.index'))

    return render_template('new_blog.html', blog_form=form)