from flask import (
    Blueprint, render_template, request
)

from datetime import datetime


bp = Blueprint('home', __name__)



@bp.route("/")
def index():
    from . import db
    timestamp = request.args.get('time')
    if timestamp:
        now = datetime.fromtimestamp(int(timestamp))
    else:
        now = datetime.now()

    target_date = datetime(2024, 5, 22)
    if now < target_date:
        final_message = "Put the time as an argument!"
    elif now > target_date:
        final_message = "That is too far in the future!"
    else:
        final_message = db.get_db().execute("SELECT message_text FROM messages WHERE id = 10").fetchone()['message_text']

    return render_template(
        'index.html',
        target_date=target_date,
        final_message=final_message
    )
