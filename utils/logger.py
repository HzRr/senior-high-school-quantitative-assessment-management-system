import datetime


def logger(content):

    content = f"[{str(datetime.datetime.today()).split('.')[0]}] " + content + "\n"
    with open("utils/log/logs.txt", "a", encoding="utf8") as fp:

        fp.write(content)

    print(content)