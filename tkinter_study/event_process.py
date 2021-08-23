import tkinter
import tkinter.messagebox
import os
import sys


def get_resource_path(relative_path):
    if getattr(sys, "frozen", False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class MainForm:
    def __init__(self):
        self.root = tkinter.Tk()
        # 设置标题
        self.root.title("事件处理")
        # 设置图标
        self.root.iconbitmap(get_resource_path(os.path.join("source", "home.ico")))
        # 设置初始窗体大小
        self.root.geometry("500x400")
        # 设置最大窗体大小
        self.root.maxsize(1920, 1080)
        # 设置背景色
        self.root["background"] = "LightSlateGray"
        # 应用程序窗口绑定程序
        # self.root.bind("<Button-1>", self.btn_left_click)
        # self.root.bind("<Button-1>", lambda event: self.btn_left_click(event, "lambda 很有用"))
        self.root.bind("<Button-1>", self.btn_left_click_new(info="lambda 很有用"))

        photo = tkinter.PhotoImage(file=get_resource_path(os.path.join("source", "pikaqiu1.png")))

        self.button = tkinter.Button(self.root, image=photo, text="这是个按钮", compound="top")

        self.button.pack()
        self.root.mainloop()

    def btn_left_click(self, event, info):

        tkinter.messagebox.showinfo(title="这是标题", message=event)

    def btn_left_click_new(self, event, info):
        self.btn_left_click(event, info)

def main():
    MainForm()


if __name__ == '__main__':
    main()
