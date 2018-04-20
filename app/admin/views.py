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


