from pywebio.output import *
from pywebio.input import *
from utils.logger import logger


def updateInfo():
    """UpdateInfo
    
    更改量化考核信息
    """

    def check(data):
        # 检测输入是否合法
        try:
            data == "" or int(data.split()[0])
        except:
            return "输入不合法!"

    with open("data\data.csv", "r", encoding="utf8") as fp:

        data = [i.split(",") for i in fp.read().split()]

    put_text("更改量化考核信息").style('text-align:center')

    name = select("Name", [i[0] for i in data[1:]])
    order = select("order", [i[0] for i in data[0][2:]])
    
    original_score = None
    for i in data:
        if i[0] == name:
            original_score = i[int(order)+1]
    
    try:
        score = input(
            f"请输入{name}第{order}次量化考核修改后的分数",
            placeholder=original_score,  # 原分数
            # required=True, 
            validate=check
        )
        score = '0' if (score == '' or score == '0') else int(score)>0 and "+"+str(int(score)) or score
        
        # 总分求和/拼接字符串
        for index, i in enumerate(data):
            if i[0] == name:
                i[int(order)+1] = score
                i[1] = str(int(i[1]) - int(original_score) + int(score))
            data[index] = ",".join(i)

        # 写入数据
        with open("data\data.csv", "w", encoding="utf8", newline="") as fp:

                fp.write("\n".join(data))

    except Exception as e:
            
        put_error(f"信息更改出错!请重试或寻求管理员帮助!\nException: {repr(e)}")
        logger(f"UpdateInfo Exception: {repr(e)}")

    else:
        put_success("信息修改成功!")
        logger_content = f"更改了以下信息:\n" \
                         f"\t{name}第{order}次量化考核: {original_score} -> {score}"
        logger(logger_content)


                       


