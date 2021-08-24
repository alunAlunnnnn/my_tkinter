import tkinter
import os
import sys
import functools


def static_resource_path(resource_path):
    def _static_resource_path(func):
        @functools.wraps(func)
        def _wrapper(img_name):
            img_path = os.path.join(resource_path, img_name)
            res = func(img_path)

            return res

        return _wrapper

    return _static_resource_path


# 固定资源路径
@static_resource_path(os.path.join(os.path.abspath("."), "source"))
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
        self.root.iconbitmap(get_resource_path("home.ico"))
        self.root.geometry("800x200")
        self.root.maxsize(1920, 1080)
        self.root["background"] = "LightSlateGray"

        photo = tkinter.PhotoImage(file=get_resource_path("pikaqiu1.png"))
        self.label = tkinter.Label(self.root, image=photo)
        self.label2 = tkinter.Label(self.root, image=photo)

        # 左右布局
        self.label.pack(anchor="w")
        self.label2.pack(anchor="e")
        self.root.mainloop()


def main():
    MainForm()


if __name__ == '__main__':
    main()
