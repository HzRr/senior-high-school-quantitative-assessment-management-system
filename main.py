from pywebio import start_server
from page.showInfo import showInfo
from page.addInfo import addInfo
from page.updateInfo import updateInfo
from page.analysisInfo import analysisInfo


start_server(
        applications=[showInfo, addInfo, updateInfo, analysisInfo],
        port=39911,
        # auto_open_webbrowser=True,
        remote_access=True,
        cdn=True,
        # debug=True
        )