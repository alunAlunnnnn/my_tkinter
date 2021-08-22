import tkinter as tk
import os

class MainForm:
    def __init__(self):
        # 窗体实例
        root = tk.Tk()
        # 设置标题
        root.title("标题")
        # 设置图标
        root.iconbitmap(os.path.join(os.path.dirname(__file__), "source", "home.ico"))
        # 设置初始窗体大小
        root.geometry("500x400")
        # 设置最大窗体大小
        root.maxsize(1000, 800)
        # 设置背景颜色
        root["background"] = "LightSlateGray"

        # ---------- 标签控件 ----------
        #  图片实例
        photo = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "source", "pikaqiu1.png"))
        # 图片标签
        label_photo = tk.Label(root, image=photo, width=200, height=200)
        # 标签显示
        # label_photo.pack()

        # 文本标签设置
        label = tk.Label(root, text="这是个标签", width=200, height=200, bg="#350158", fg="#ffffff",
                         font=("arial", 15), justify="left")
        # 标签显示
        # label.pack()

        # ---------- 文本控件 - ---------
        # 文本标签设置
        text = tk.Text(root, width=200, height=200, font=("arial", 10))
        # 设置默认值
        text.insert(tk.CURRENT, "当前位置插入值")
        # 设置默认值
        text.insert(tk.END, "文末插入值")
        # 插入图片
        text.image_create(tk.END, image=photo)
        # 文本标签显示
        text.pack()

        root.mainloop()


def main():
    MainForm()


if __name__ == '__main__':
    main()
