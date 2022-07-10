from pywebio import start_server
from page.showInfo import showInfo
from page.addInfo import addInfo


start_server(
        applications=[showInfo, addInfo],
        port=1145,
        auto_open_webbrowser=True,
        remote_access=True
        )

"""
   各个页面的样式
    
"""