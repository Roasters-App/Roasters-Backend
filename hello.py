from sanic import Sanic
from sanic.response import json

app = Sanic(__name__)
app.config.from_envvar("SETTING_PATH")


@app.route("/")
async def test(request):
    return json({"hello": "world"})


if __name__ == "__main__":
    app.run(app.config.SANIC_HOST, app.config.SANIC_PORT)