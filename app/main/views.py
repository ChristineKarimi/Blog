from flask import render_template, redirect, request, url_for, abort
from flask_login import login_required, current_user
from . import main
from ..admin import admin
from .forms import ReviewForm, BlogForm, EditBlog, DeleteBlog, DeleteComment
from ..models import Blog, Review, User
from .. import db

#==============================================================================================================================================================================================================================

@main.route('/blog/review/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_review(id):

    blog = Blog.query.filter_by(id=id).first()

    if blog is None:
        abort(404)

    form = ReviewForm()

    if form.validate_on_submit():

        review = form.review.data

        new_review = Review(review=review, user_id=current_user.id, blog_id=blog.id)

        new_review.save_review()

        return redirect(url_for('.single_blog', id=blog.id))

    return render_template('new_review.html', review_form=form, blog=blog)

#===============================================================================================================================================================================================================================================

@main.route('/blog/review/new/<int:id>', methods=['GET', 'POST'])
def new_review(id):

    blog = Blog.query.filter_by(id=id).first()

    if blog is None:
        abort(404)

    form = ReviewForm()

    if form.validate_on_submit():

        review = form.review.data

        new_review = Review(review=review, user_id=current_user.id, blog_id=blog.id)

        new_review.save_review()

        return redirect(url_for('.single_blog', id=blog.id))

    return render_template('new_review.html', review_form=form, blog=blog)

