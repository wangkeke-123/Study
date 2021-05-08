from tkinter import *
from tkinter.tix import Tk, Control, ComboBox  #升级的组合控件包
from tkinter.messagebox import showinfo, showwarning, showerror #各种类型的提示框

root = Tk() # 初始化Tk()
root.title("hello tkinter")    # 设置窗口标题
root.geometry("800x1000")    # 设置窗口大小 注意：是x 不是*
root.resizable(width=True, height=True) # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
root.tk.eval('package require Tix')  #引入升级包，这样才能使用升级的组合控件

lable = Label(root, text="label", bg="pink",bd=10, font=("Arial",12), width=8, height=3)
lable.pack(side=LEFT)

# Booleans
NO = FALSE = OFF = 0
YES = TRUE = ON = 1

# -anchor and -sticky
N = 'n'
S = 's'
W = 'w'
E = 'e'
NW = 'nw'
SW = 'sw'
NE = 'ne'
SE = 'se'
NS = 'ns'
EW = 'ew'
NSEW = 'nsew'
CENTER = 'center'

# -fill
NONE = 'none'
X = 'x'
Y = 'y'
BOTH = 'both'

# -side
LEFT = 'left'
TOP = 'top'
RIGHT = 'right'
BOTTOM = 'bottom'

# -relief
RAISED = 'raised'
SUNKEN = 'sunken'
FLAT = 'flat'
RIDGE = 'ridge'
GROOVE = 'groove'
SOLID = 'solid'

# -orient
HORIZONTAL = 'horizontal'
VERTICAL = 'vertical'

# -tabs
NUMERIC = 'numeric'

# -wrap
CHAR = 'char'
WORD = 'word'

# -align
BASELINE = 'baseline'

# -bordermode
INSIDE = 'inside'
OUTSIDE = 'outside'

# Special tags, marks and insert positions
SEL = 'sel'
SEL_FIRST = 'sel.first'
SEL_LAST = 'sel.last'
END = 'end'
INSERT = 'insert'
CURRENT = 'current'
ANCHOR = 'anchor'
ALL = 'all'  # e.g. Canvas.delete(ALL)

# Text widget and button states
NORMAL = 'normal'
DISABLED = 'disabled'
ACTIVE = 'active'
# Canvas state
HIDDEN = 'hidden'

# Menu item types
CASCADE = 'cascade'
CHECKBUTTON = 'checkbutton'
COMMAND = 'command'
RADIOBUTTON = 'radiobutton'
SEPARATOR = 'separator'

# Selection modes for list boxes
SINGLE = 'single'
BROWSE = 'browse'
MULTIPLE = 'multiple'
EXTENDED = 'extended'

# Activestyle for list boxes
# NONE='none' is also valid
DOTBOX = 'dotbox'
UNDERLINE = 'underline'

# Various canvas styles
PIESLICE = 'pieslice'
CHORD = 'chord'
ARC = 'arc'
FIRST = 'first'
LAST = 'last'
BUTT = 'butt'
PROJECTING = 'projecting'
ROUND = 'round'
BEVEL = 'bevel'
MITER = 'miter'

# Arguments to xview/yview
MOVETO = 'moveto'
SCROLL = 'scroll'
UNITS = 'units'
PAGES = 'pages'


button=Button(root,text='QUIT',command=root.quit,activeforeground="black",activebackground='blue',bg='red',fg='white')
button.pack(fill=Y,expand=1)

def resize(ev=None):
    lable.config(font='Helvetica -%d bold'%scale.get())
scale=Scale(root,from_=10,to=40,orient=HORIZONTAL,command=resize)
scale.set(12)
scale.pack()

ct=Control(root,label='Number:',integer=True,max=12,min=2,value=2,step=2)
ct.label.config(font='Helvetica 14 bold')
ct.pack()

cb=ComboBox(root,label='Type:',editable=True)
for animal in ('dog','cat','haha','python'):
    cb.insert(END,animal)
cb.pack()


def click():
    print("点击了一次")
menubar=Menu(root)
root.config(menu=menubar)
filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='文件',menu=filemenu)
filemenu.add_command(label='新建...',command=click())
filemenu.add_command(label='打开...',command=click())
filemenu.add_command(label='保存',command=click())
filemenu.add_command(label='关闭填写',command=root.quit)


frame1 =Frame(root)
frame1.pack(fill=X)
lable1=Label(frame1,text='您的花名：  ')
lable1.grid(row=1,column=0)


frame2=Frame(root)
frame2.pack(fill=X)
lable2=Label(frame2,text='您的性别：  ')
lable2.grid(row=1,column=0)
sex=StringVar()
sex_male=Radiobutton(frame2,text='男',fg='blue',variable=sex,value='男')
sex_male.grid(row=1,column=2)
sex_female=Radiobutton(frame2,text='女',fg='red',variable=sex,value='女')
sex_female.grid(row=1,column=4)

root.mainloop()

