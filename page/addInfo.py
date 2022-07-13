from pywebio.output import *
from pywebio.input import *
from utils.logger import logger


def addInfo():
    """AddInfo
    
    增加量化考核信息
    """

    def check(data):
        # 检测输入是否合法
        try:
            data == "" or int(data.split()[0])
        except:
            return "输入不合法!"

    with open("data/data.csv", "r", encoding="utf8") as fp:
        # 获取学生名单
        student_name = [i.split(",")[0] for i in fp.read().split()[1:]]

    with use_scope("head"):
        
        put_html("<p style='text-align:center'>添加信息</p>")

    with use_scope("body"):
        
        # if True:
        try:
            # 利用输入组获取量化考核信息，但是input的name argument不支持中文字符,所以需要曲线救国( 
            data = input_group("Add Info",[
                    input(student_name[i], name=str(i), validate=check) for i in range(len(student_name))
                    ])
            
            # 替换keys
            data = dict(zip(
                        [j for j in student_name],
                        [data[str(i)] for i in range(len(student_name))]
                        ))

            # print(data)
            # 添加信息
            with open("data/data.csv", "r", encoding="utf8") as fp:

                content = [i.split(",") for i in fp.read().split()]

            # 如果是第一次添加信息,则添加总分信息
            if len(content[0]) == 1:
                content[0].append("总分")
                for i in content[1:]:
                    i.append(0)

            for index, i in enumerate(content):
                    
                if i[0] == "name\\order":
                    i.append(str(len(i) - 1))
                    content[index] = ",".join(i)
                    continue

                score = data[i[0]]
                i.append('0' if (score == '' or score == '0') else int(score)>0 and "+"+str(int(score)) or score)

                # 总分求和
                # sum = i[1] + i[-1]
                # 利用循环重新求和,防止由于直接修改文件改动分数造成的总分不一致
                sum = 0
                for j in i[2:]:
                    sum += int(j)
                i[1] = str(sum)
                content[index] = ",".join(i)
            
            # print(content)
            with open("data/data.csv", "w", encoding="utf8", newline="") as fp:

                fp.write("\n".join(content))
                
        except Exception as e:
            
            put_error(f"信息添加出错!请重试或寻求管理员帮助!\nException: {repr(e)}")
            logger(f"AddInfo Exception: {repr(e)}")

        else:
            put_success("信息添加成功!")
            logger_content = f"添加了以下信息:"
            for i in student_name:
                score = data[i]
                logger_content += f"\n\t{i}: {' 0' if score == '' else int(score)>0 and '+'+str(int(score)) or score}"
            logger(logger_content)