from pywebio.output import *
from pywebio.input import *
from utils.handleImg import groupPlot, personPlot

                
def analysisInfo():
    """AnalysisInfo
    
    选择并对比的量化考核成绩
    """
    with open("data/data.csv", "r", encoding="utf8") as fp:

        data = [i.split(",") for i in fp.read().split()]
    
    with open("data/group.csv", "r", encoding="utf8") as fp:

        group_data = [i.split(",") for i in fp.read().split()]

    group_info_ls = []
    for i in group_data:
        temp_ls = []
        for j in data:
            if j[0] in i:
                temp_ls.append(j)
        group_info_ls.append(temp_ls)
    
    person_info_ls = data[1:]

    def sort_score(score_ls, name_ls):
        
        sort_score = sorted(score_ls)[::-1]
        sort_order = []

        for j in range(len(sort_score)):
            for i in range(len(score_ls)):
                if score_ls[i] == sort_score[j]:
                    sort_order.append(i)
                    break

        # print(score_ls)
        # print(sort_order)
        # print(name_ls)
        text = "排名(由大到小): "
        for i in sort_order:
            text += f"{name_ls[i]}({score_ls[i]})   "

        return text

    def groupImg():

        with use_scope("body", clear=True):
            order_ls = checkbox(
                label="选择需要对比的量化考核次序",
                options=["全选"] + [str(i) for i in range(1, len(data[0])-1)]
            )
            order_ls = list(range(1, len(data[0])-1)) if "全选" in order_ls else order_ls
        
        name_ls = [f"第{i+1}组" for i in range(len(group_info_ls))]
        img, group_sum_score = groupPlot(group_info_ls, order_ls, name_ls)
        text = sort_score(group_sum_score, name_ls)

        put_image(img)
        put_markdown("小组" + text)

    def personImg():
        
        with use_scope("body", clear=True):
            order_ls = checkbox(
                label="选择需要对比的量化考核次序",
                options=["全选"] + [str(i) for i in range(1, len(data[0])-1)]
            )
            order_ls = list(range(1, len(data[0])-1)) if "全选" in order_ls else order_ls
        
        name_ls = [i[0] for i in person_info_ls]
        img, person_sum_score = personPlot(person_info_ls, order_ls, name_ls)
        text = sort_score(person_sum_score, name_ls)

        put_image(img)
        put_markdown("个人" + text)

    with use_scope("body"):

        put_buttons(["个人对比", "小组对比"], onclick=[personImg, groupImg])