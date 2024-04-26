from flask import (
    Blueprint, render_template
)

bp = Blueprint('flag_5', __name__)

@bp.route("/flag_5")
def flag_5():
    return render_template(
        'riddles.html',
    )
