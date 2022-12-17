from flask import (
    Blueprint, render_template, request, url_for,
    redirect,
)

about_app = Blueprint(
    "about_app",
    __name__,
)

@about_app.route("/about/",
                    methods=["GET"],
                    endpoint="about",
                    )
def about_page():
    if request.method == 'GET':
        return render_template(
            "about.html",
        )
    url = url_for("about_app.about")
    return redirect(url)