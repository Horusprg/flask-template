from flask import Blueprint, render_template
from app.utils.functions import captalize

route1_bp = Blueprint(
    "route1", "__name__", template_folder="templates", static_folder="static"
)


@route1_bp.get("/")
def main_get():
    name = "flavio"
    return render_template("route1/index.html", value=f"{captalize(name)}")
