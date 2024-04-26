from flask import (
    Blueprint, render_template
)

bp = Blueprint('panda', __name__)

@bp.route("/panda")
def panda():
    return render_template(
        'panda.html',
    )
