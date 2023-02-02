from backend.api import convert_commands
from frontend import web_page
from asgiref.wsgi import WsgiToAsgi
from flask import Flask
from flask import render_template
from loguru import logger


app = Flask(__name__)
asgi_app = WsgiToAsgi(app)


if __name__ == "__main__":
    @app.route("/cisco-to-eltex-convecter")
    async def cisco_to_eltex_page() -> None:
        return render_template('/frontend/web_page/cisco-to-eltex.html')
