from flask import (
    Blueprint, render_template, request
)


bp = Blueprint('flags', __name__)



@bp.route("/flags", methods=('GET', 'POST'))
def index():
    from . import db


    flag_id = ""
    if request.method == 'POST':
        flag_id = request.form.get('flag_id', flag_id)

    if flag_id == '*':
        result = 'Nice try! But no.'
    elif not flag_id:
        result = 'Seek flag number eight, your guess shall seal your fate!'
    elif not flag_id.isdigit():
        result = 'Wrong value. Looks like your guess missed the mark!'
    else:
        print(flag_id)
        result = db.get_db().execute(f"SELECT * FROM flags WHERE id = {int(flag_id)}").fetchone()
        print(result)
        result = 'No luck. I would try different number!' if result is None else 'FLAG 8: ' + result['flag_text']

    return render_template(
        'flags.html',
        result=result,
    )
