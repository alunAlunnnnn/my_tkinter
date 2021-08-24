import tkinter
import tkinter.messagebox


class MainForm:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("标题")
        self.root.geometry("500x400")
        self.root.maxsize(1920, 1080)

        # 窗体关闭协议监听
        self.root.protocol("WM_DELETE_WINDOW", self.window_close_handle)

        self.root.mainloop()

    def window_close_handle(self):
        # 弹出提示框
        if tkinter.messagebox.askyesnocancel("程序关闭确认", "确认关闭"):
            # 关闭程序
            self.root.destroy()


def main():
    MainForm()


if __name__ == '__main__':
    main()
