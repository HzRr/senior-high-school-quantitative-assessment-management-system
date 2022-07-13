import matplotlib.pyplot as plt
from PIL import Image
from pylab import mpl

    
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ['SimHei']
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False
mpl.use("Agg")

# 设置标题字体大小
size = 10
# 设置柱状图宽度
width = 0.1


def figToImg(fig):
    """Matplotlib figure 转为 PIL Image"""
    import io
    buf = io.BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    img = Image.open(buf)
    return img

def groupPlot(info_ls, order_ls, name_ls):

    sum_score = []
    # print(info_ls)
    for i in info_ls:
        temp_sum = 0
        if len(i)>1:
            for j in i:
                for order in order_ls:
                    temp_sum += int(j[int(order)+1])
        else:
            for order in order_ls:
                temp_sum += int(i[0][int(order)+1])

        sum_score.append(temp_sum)

    x_lable = name_ls

    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ax.bar(x_lable, sum_score, width=width)
    ax.axhline(0,color='red',linewidth=5)
    ax.set_title(f"第{'、'.join([str(i) for i in order_ls])}次量化考核总分柱状图", size=size)
    
    return figToImg(fig), sum_score

def personPlot(info_ls, order_ls, name_ls):

    # print(info_ls)
    # print(order_ls)
    sum_score = []
    # print(info_ls)
    for i in info_ls:
        temp_sum = 0
        for order in order_ls:
            temp_sum += int(i[int(order)+1])

        sum_score.append(temp_sum)

    x_lable = name_ls

    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ax.bar(x_lable, sum_score, width=width)
    ax.axhline(0,color='red',linewidth=1)
    ax.set_title(f"第{'、'.join([str(i) for i in order_ls])}次量化考核总分柱状图", size=size)
    
    return figToImg(fig), sum_score