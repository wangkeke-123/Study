import tkinter as tk


root = tk.Tk() # 创建窗口

# root['background'] = 'gray'# 设置背景颜色

root.title("hello tkinterQQ")
root.geometry("200x200+100+50")    # 设置窗口大小 注意：是x 不是* 位置为距离屏幕，左右距即x轴100，上下距即y轴50
root.resizable(width=True, height=True) # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
root.tk.eval('package require Tix')  #引入升级包，这样才能使用升级的组合控件
# root.update() # 窗口刷新

# 获取位置前必须刷新窗口
root.update()
print( root.winfo_x() )
print( root.winfo_y() )

# 使窗口能拉取的大小在一个范围内
root.maxsize(300, 600)
root.minsize(20, 100)

# 参数是*.ico格式的图标路径
root.iconbitmap('C:\图片\ 草莓.jpeg')

b1 = tk.Button(root, text='hello b1')
b2 = tk.Button(root, text='hello b2')
b3 = tk.Button(root, text='hello b3')
b4 = tk.Button(root, text='hello b4')

b1.grid(row=0, column=1)
b2.grid(row=1, column=1)
b3.grid(row=2, column=1)
b4.grid(row=1, column=2, rowspan=2, columnspan=2)
# 先测试代码，然后替换注释掉的b4， 再检查结果。
# b4.grid(row=1, column=2, rowspan=2, columnspan=2, sticky='nw')
root.mainloop()
