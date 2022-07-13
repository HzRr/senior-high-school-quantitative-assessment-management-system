# senior-high-school-quantitative-assessment-management-system
pyWebIO实现的高中量化考核管理系统

启动方法:
    在main.py所在目录下输入python3 main.py
    会打印一个remote access, 然后通过这个access访问网站
    为了更方便快捷地访问网站，可以自己解析一个中转域名，然后通过这个域名来访问

PS:
    若在linux上部署该项目，需要安装SimHei字体(否则matplotlib无法支持中文字符)
    方法:
        1.将windows上【黑体 常规】复制一份到服务器 /usr/share/fonts 目录下
        2.sudo fc-cache -f -v刷新字体缓存
        3.开一个python的命令行(python3、ipython), 依次输入
            import matplotlib as plt
            plt.get_cachedir()
          会得到一个缓存路径
          然后退出命令行，输入sudo rm -rf 路径

