from flask import Blueprint, render_template
from app.utils.functions import captalize

route2_bp = Blueprint(
    "route2", "__name__", template_folder="templates", static_folder="static"
)


@route2_bp.get("/<name>")
def main_get_with_name(name):
    return render_template("route1/index.html", value=f"{captalize(name)}")
