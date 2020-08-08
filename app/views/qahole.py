from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from app.db import get_db


qh = Blueprint('qahole', __name__, url_prefix='/qahole')


@qh.route('/', methods=['GET'])
def index():
    db = get_db()

    error = None

    if db.execute(
        'SELECT * FROM qahole LIMIT 1'
    ).fetchone() is None:
        error = 'Database is empty.'

    if error is None:
        qaholes = db.execute(
            'SELECT * FROM qahole ORDER BY comment_id DESC LIMIT 100'
        ).fetchall()

        return render_template('qahole/index.html', qaholes=qaholes)

    else:
        flash(error)

        return render_template('base.html')
