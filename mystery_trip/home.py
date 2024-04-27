from flask import (
    Blueprint, render_template
)

from datetime import datetime


bp = Blueprint('home', __name__)



@bp.route("/")
def index():
    from . import db
    now = datetime.now()
    target_date = datetime(2024, 5, 22)
    if now > target_date:
        final_message = db.get_db().execute("SELECT message_text FROM messages WHERE id = 10").fetchone()['message_text']
    else:
        final_message = "The flag is one refresh away!"

    return render_template(
        'index.html',
        target_date=target_date,
        final_message=final_message
    )
