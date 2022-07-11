from pywebio import start_server
from page.showInfo import showInfo
from page.addInfo import addInfo
from page.updateInfo import updateInfo


start_server(
        applications=[showInfo, addInfo, updateInfo],
        port=1145,
        # auto_open_webbrowser=True,
        remote_access=True,
        debug=True
        )