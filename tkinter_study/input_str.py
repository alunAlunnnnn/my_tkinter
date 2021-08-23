import tkinter
import tkinter.messagebox
import tkinter.simpledialog
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
        self.root.title("标题")
        self.root.iconbitmap(get_resource_path(os.path.join("source", "home.ico")))
        self.root.geometry("500x400")
        self.root.maxsize(1920, 1080)
        self.root["background"] = "LightSlateGray"

        photo = tkinter.PhotoImage(file=get_resource_path(os.path.join("source", "pikaqiu1.png")))
        self.button = tkinter.Button(self.root, image=photo, text="这是一个按钮", font=("微软雅黑", 20),
                                     fg="#fff")

        self.button.bind("<Button-1>", lambda event: self.btn_click(event, "欢迎"))

        self.button.pack()
        self.root.mainloop()

    def btn_click(self, event, info):
        input_message = tkinter.simpledialog.askstring(title="提示框", prompt="请输入一个词")
        tkinter.messagebox.showinfo(title=info, message=input_message)



def main():
    MainForm()


if __name__ == '__main__':
    main()
