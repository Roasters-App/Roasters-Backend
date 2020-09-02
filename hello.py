from sanic import Sanic
from sanic.log import logger
from sanic.response import json

app = Sanic(__name__)
app.config.from_envvar("CONFIG_FILE")


@app.route("/")
async def test(request):
    logger.info("Request arrived")
    return json({"hello": "world"})


if __name__ == "__main__":
    if app.config.PRODUCTION:
        app.run(access_log=True)
    else:
        app.run(debug=True, access_log=True)
