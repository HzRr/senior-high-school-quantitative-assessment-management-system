from turtle import title
from pywebio import start_server
from page.showInfo import showInfo


start_server(
        applications=[showInfo],
        port=1145,
        auto_open_webbrowser=True,
        remote_access=True,
        debug=True
        )