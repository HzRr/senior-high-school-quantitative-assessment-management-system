from pywebio.output import *


def showInfo():
    '''ShowInfo
    
    查看当前量化考核信息
    '''

    with open("data\data.csv", "r", encoding="utf8") as fp:

        data = [i.split(",") for i in fp.read().split()]

    for i in data:

        if i[0] == "name\\order":
            for n in range(len(i)):
                i[n] = put_html('<b style="color:#0033FF">' + i[n] + "</b>")
        else:
            i[0] = put_html('<b style="color:#0033FF">' + i[0] + "</b>")

    put_table(
        [[span(put_html("<p style='text-align:center'>量化考核信息</p>"), col=len(data[0]))]]+data
        ).show()

