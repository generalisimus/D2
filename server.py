import os
from bottle import route, run
import sentry_sdk

from bottle import Bottle, request, template
from sentry_sdk.integrations.bottle import BottleIntegration


sentry_sdk.init(
    dsn="https://my_number@sentry.io/my_number",
    integrations=[BottleIntegration()]
)

app = Bottle()


@app.route('/')
def index():
    return 'ОК'


@app.route('/success')
def index():
    return 'Все ОК'


@app.route('/fail')
def index():
    raise RuntimeError("There is an error")
    return


if os.environ.get("APP_LOCATION") == "heroku":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    app.run(host="localhost", port=8080, debug=True)
