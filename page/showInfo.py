from pywebio.output import *


def showInfo():
    '''ShowInfo
    
    查看当前量化考核信息
    '''

    with open("data\data.csv", "r", encoding="utf8") as fp:

        content = [i.split(",") for i in fp.read().split()]

    for i in content:

        if i[0] == "name\\order":
            for n in range(1, len(i)):
                i[n] = put_html('<b style="color:#0033FF">' + i[n] + "</b>")
        else:
            i[0] = put_html('<b style="color:#0033FF">' + i[0] + "</b>")
    
    with use_scope("head"):
        
        put_text("量化考核信息")
    
    with use_scope("body"):

        put_table(content).show()

