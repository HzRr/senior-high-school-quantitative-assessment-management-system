from pydoc import describe
from pywebio.output import *
from pywebio.session import *


def showInfo():
    '''ShowInfo
    
    查看当前所有学生信息
    '''
    set_env(title="ShowInfo")
    with open("data\data.csv", "r", encoding="utf8") as fp:

        content = [i.split(",") for i in fp.read().split()]

    for i in content:

        if i[0] == "name\\order":
            for n in range(1, len(i)):
                i[n] = put_html('<b style="color:#0033FF">' + i[n] + "</b>")
        else:
            i[0] = put_html('<b style="color:#0033FF">' + i[0] + "</b>")

    put_table(content).show()

