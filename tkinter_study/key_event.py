import tkinter
import os
import sys
import re


def get_resource_path(relative_path):
    if getattr(sys, "frozen", False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class MainForm:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("标题")
        self.root.iconbitmap(get_resource_path(os.path.join("source", "home.ico")))
        self.root.geometry("500x400")
        self.root.maxsize(1920, 1080)
        self.root["background"] = "LightSlateGray"

        # 设置一个文本输入框
        self.text = tkinter.Text(self.root, width=500, height=2, font=("微软雅黑", 20))
        # 输入内容的提示信息
        self.text.insert(tkinter.CURRENT, "请输入正确的邮箱地址...")
        # 绑定左键点击时，删除提示信息
        self.text.bind("<Button-1>", lambda event: self.text.delete(0.0, tkinter.END))
        # 绑定键盘按下事件
        self.text.bind("<KeyPress>", lambda event: self.keyboard_event_handle(event))
        # 绑定键盘的抬起事件，键盘抬起、放下一起绑定，则可做到事实显示输入内容
        self.text.bind("<KeyRelease>", lambda event: self.keyboard_event_handle(event))

        # 用于修改标签文本
        self.content = tkinter.StringVar()
        # 设置标签
        self.label = tkinter.Label(self.root, textvariable=self.content, width=200, height=200,
                                   bg="#223011", font=("微软雅黑", 20), fg="#ffffff")

        # 邮箱正则验证
        self.comp = re.compile(r"[a-zA-Z0-9]\w+@\w+\.(cn|com|com.cn|gov|net)", re.I | re.X)

        self.text.pack()
        self.label.pack()
        self.root.mainloop()

    def keyboard_event_handle(self, event):
        # 获取文本框的信息输入
        text_content = self.text.get(0.0, tkinter.END)
        if self.comp.match(text_content):
            # 邮箱格式正确则进行显示
            self.content.set(f"邮箱内容设置正确, 内容为：{text_content}")
        else:
            self.content.set("邮箱格式错误，请重新输入！")


def main():
    MainForm()


if __name__ == '__main__':
    main()
