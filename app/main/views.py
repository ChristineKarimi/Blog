
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
