from typing import Any, Tuple

from flask import render_template


def http_404(message: str = None) -> Tuple[Any, int]:
    message = message or 'Not Found'
    return render_template('errors/404.html', message=message), 404
