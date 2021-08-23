import tkinter as tk
import os
import sys


def get_resource_path(relative_path):
    """
    资源定位，当将 python 打包为 exe 程序时，cx_freeze 会将 frozen 变量加入到 sys 中
    :param relative_path: str, 资源相对于当前 python 文件的路径，如 os.path.join("相对路径的资源文件夹名", "图片名.png")
    :return: str, 资源的路径
    """

    # 存在临时资源路径
    if getattr(sys, "frozen", False):
        # 获取临时资源路径
        base_path = sys._MEIPASS
    else:
        # 获取当前路径
        base_path = os.path.abspath(".")

    # 将资源路径返回
    return os.path.join(base_path, relative_path)


class MainForm:
    def __init__(self):
        # 窗体实例
        root = tk.Tk()
        # 设置标题
        root.title("标题")
        # 设置图标
        root.iconbitmap(get_resource_path(os.path.join("source", "home.ico")))
        # 设置初始窗体大小
        root.geometry("500x400")
        # 设置最大窗体大小
        root.maxsize(1000, 800)
        # 设置背景颜色
        root["background"] = "LightSlateGray"

        # ---------- 标签控件 ----------
        #  图片实例
        photo = tk.PhotoImage(file=get_resource_path(os.path.join("source", "pikaqiu1.png")))

        # ---------- 按钮控件 - ---------
        # 设置按钮控件
        button = tk.Button(root, image=photo, text="这是个图片", compound="top", font=("微软雅黑", 20), fg="#a00")

        button.pack()

        root.mainloop()


def main():
    MainForm()


if __name__ == '__main__':
    main()
