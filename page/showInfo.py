from pywebio.output import *


def showInfo():
    '''ShowInfo
    
    查看当前量化考核信息
    '''

    with open("data\data.csv", "r", encoding="utf8") as fp:

        data = [i.split(",") for i in fp.read().split()]
        data[0] = ["组别"]+data[0]
    
        # 构建加粗颜色字体
        for index in range(1, len(data[0])):
            data[0][index] = put_html('<b style="color:#0033FF">' + data[0][index] + "</b>")

    content = [
        [span(put_html("<p style='text-align:center'>量化考核信息</p>"), col=len(data[0])+1)],
        [i for i in data[0]],
        ]

    with open("data\group.csv", "r", encoding="utf8") as fp:

        group_data = [i.split(",") for i in fp.read().split()]

    for i in group_data:
        for j in data:
            if j[0] in i:
                # 构建加粗颜色字体
                j[0] = put_html('<b style="color:#0033FF">' + j[0] + "</b>")
                content.append([i[0]] + j)    

    put_table(content)