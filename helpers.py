from flask import request, render_template

def validate_required(fields: list[str]) -> (str | None):
    for field in fields:
        if not request.form.get(field):
            return render_template("apology.html", message=f"{field} is required")
    return None