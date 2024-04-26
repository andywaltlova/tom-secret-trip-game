import os

from flask import Flask

app = Flask(__name__, instance_relative_config=True)


app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'mystery-trip.sqlite'),
)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

from . import db
db.init_app(app)

from . import home
app.register_blueprint(home.bp)
app.add_url_rule('/', endpoint='index')

from . import flag_5
app.register_blueprint(flag_5.bp)
app.add_url_rule('/flag_5', endpoint='flag_5')

from . import flags
app.register_blueprint(flags.bp)
app.add_url_rule('/flags', endpoint='flags')

from . import panda
app.register_blueprint(panda.bp)
app.add_url_rule('/panda', endpoint='panda')
