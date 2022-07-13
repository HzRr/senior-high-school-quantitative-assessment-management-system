from pywebio.output import *
from copy import deepcopy


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

    '''original_data = deepcopy(data)
    for i in data:

       # [span(put_html(f"<p style='text-align:center'>第{i}组</p>"), row=len(data)+1)]
        if i[0] == "name\\order":
            for n in range(len(i)):
                i[n] = put_html('<b style="color:#0033FF">' + i[n] + "</b>")
            
        else:
            i[0] = put_html('<b style="color:#0033FF">' + i[0] + "</b>")

    # 调整data组别
    print(type(data[1]))
    new_data = []
    for key in group_dict:
        temp_ls = []
        for index in range(len(original_data)):
            if original_data[index][0] in group_dict[key]:
                temp_ls.append[data[index]]
        new_data.append(temp_ls)
    
    print(new_data)
                

    put_table(
        [span(put_html("<p style='text-align:center'>量化考核信息</p>"), col=len(data[0])+1)]
        +

        data
        ).show()'''

