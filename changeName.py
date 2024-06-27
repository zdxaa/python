import tkinter as tk
from tkinter import Tk, filedialog
import os,re


# 创建主窗口对象
window = tk.Tk()

# 设置窗口标题
window.title("批量更换文件名")

# 设置窗口大小
window.geometry("500x400")
window.grid()
# 创建一个标签
label = tk.Label(window, text="你好，欢迎使用Python GUI！")
label.pack()
#定义
file_paths_all=[]
#名字添加
preName=''
afterName=''
centerName=''
file_listbox = tk.Listbox(window, selectmode=tk.MULTIPLE,width=200)
# 创建一个按钮
def on_folder_select():
   folder_path = filedialog.askdirectory()  # 打开文件对话框
   label.config(text="选择的文件夹: " + folder_path)
   # 获取文件夹的绝对路径
   abs_folder_path = os.path.abspath(folder_path)
   # 获取文件夹的父目录
   parent_dir = os.path.dirname(abs_folder_path)
   # 展开文件夹
   os.startfile(abs_folder_path)
   # 获取文件夹中的所有文件
   file_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]
   # 在这里添加修改文件内容的代码
   global file_paths_all
   file_paths_all=file_paths
#    print(file_paths_all)
   # 创建一个Listbox控件
   global file_listbox
   # 将文件添加到Listbox控件中
   for file_path in file_paths:
       file_listbox.insert(tk.END, file_path)
   file_listbox.pack()
   # 为Listbox控件绑定一个事件处理程序，以便在用户单击文件时打开该文件
   file_listbox.bind("<Double-Button-1>", lambda event: os.startfile(event.widget.get(event.widget.curselection())))

text_label = tk.Label(window, text="名字前缀(中间是1,2,3这种的顺序)：")
text_label.pack()
entry_box = tk.Entry(window)
entry_box.pack()

text_label1 = tk.Label(window, text="名字后缀：")
text_label1.pack()
entry_box1 = tk.Entry(window)
entry_box1.pack()
ZiMu=["A", 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ZiMuxiao=["a", 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def changeNameABC():
    global file_paths_all
    # print(file_paths_all)
    global preName
    global afterName
    global centerName
    preName=entry_box.get()
    afterName=entry_box1.get()
    for i in range(len(file_paths_all)):
        os.rename(file_paths_all[i].split("\\")[0]+'/'+file_paths_all[i].split("\\")[-1],file_paths_all[i].split("\\")[0]+'/'+file_paths_all[i].split("\\")[-1].replace(file_paths_all[i].split("\\")[-1].split('.')[0],preName+str(ZiMu[i])+afterName)) #preName+str(i)+afterName
def changeNameabc():
    global file_paths_all
    # print(file_paths_all)
    global preName
    global afterName
    global centerName
    preName=entry_box.get()
    afterName=entry_box1.get()
    for i in range(len(file_paths_all)):
        os.rename(file_paths_all[i].split("\\")[0]+'/'+file_paths_all[i].split("\\")[-1],file_paths_all[i].split("\\")[0]+'/'+file_paths_all[i].split("\\")[-1].replace(file_paths_all[i].split("\\")[-1].split('.')[0],preName+str(ZiMuxiao[i])+afterName)) #preName+str(i)+afterName
def changeName():
    global file_paths_all
    # print(file_paths_all)
    global preName
    global afterName
    global centerName
    preName=entry_box.get()
    afterName=entry_box1.get()
    for i in range(len(file_paths_all)):
        os.rename(file_paths_all[i].split("\\")[0]+'/'+file_paths_all[i].split("\\")[-1],file_paths_all[i].split("\\")[0]+'/'+file_paths_all[i].split("\\")[-1].replace(file_paths_all[i].split("\\")[-1].split('.')[0],preName+str(i)+afterName)) #preName+str(i)+afterName
def resversName():
    global file_paths_all

    for i in range(len(file_paths_all)):
        os.rename(file_paths_all[i].split("\\")[0]+'/'+file_paths_all[i].split("\\")[-1],file_paths_all[i].split("\\")[0]+'/'+file_paths_all[i].split("\\")[-1].replace(file_paths_all[i].split("\\")[-1].split('.')[0],file_paths_all[i].split("\\")[-1].split('.')[0][::-1])) #preName+str(i)+afterName
folder_button = tk.Button(window, text="选择文件夹", command=on_folder_select)
folder_button.pack()

# 创建一个按钮，以便在点击按钮时使用os.rename()函数批量重命名file_paths_all中所有路径的文件名
rename_button = tk.Button(window, text="批量重命名文件(1,2,3...)", command=changeName)
rename_button.pack()
# 创建一个按钮，以便在点击按钮时使用os.rename()函数批量重命名file_paths_all中所有路径的文件名
rename_button = tk.Button(window, text="批量重命名文件(A,B,C...)", command=changeNameABC)
rename_button.pack()
# 创建一个按钮，以便在点击按钮时使用os.rename()函数批量重命名file_paths_all中所有路径的文件名
rename_button = tk.Button(window, text="批量重命名文件(a,b,c...)", command=changeNameabc)
rename_button.pack()
# 创建一个按钮，批量反转file_paths_all中所有路径的文件名
rename_button = tk.Button(window, text="批量反转文件名", command=resversName)
rename_button.pack()

###########################
selectText=""
def selectFiles():
    global file_paths_all
    global selectText
    selectText=entry_box3.get()
    # 定义正则表达式
    pattern = re.compile(r'\.*{}.*$'.format(selectText))
    # 使用列表推导式和re.search()函数找到匹配的文件路径
    file_paths_all = [file_path for file_path in file_paths_all if re.search(pattern, file_path)]
    global file_listbox
    file_listbox.delete(0, tk.END)
    # 将文件添加到Listbox控件中
    for file_path in file_paths_all:
        file_listbox.insert(tk.END, file_path)
    file_listbox.pack()
# 创建一个按钮，以便在file_paths_all中所有路径的文件名中进行筛选
text_label3 = tk.Label(window, text="筛选文字：")
text_label3.pack()
entry_box3 = tk.Entry(window)
entry_box3.pack()
rename_button1 = tk.Button(window, text="筛选", command=selectFiles)
rename_button1.pack()

# 进入主循环，等待用户操作
window.mainloop()
#pyinstaller --name changeName --windowed changeName.py           