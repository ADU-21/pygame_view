
# -*- coding: utf-8 -*-  
#载入tkinter  
from tkinter import *  
#载入文件选择框  
from tkinter.filedialog import *  
#字体设置  
import tkinter.font  
import os  
#运行按钮执行函数  
def runTool():  
    #获取项目路径  
    path_value = path_entry.get()  
    #获取命令  
    cmd_value  = cmd_entry.get()  
    if not path_value:  
        log_text.insert(END, '请选择项目路径！/n', 'n')  
    else:  
        #获取参数  
        param_value = param_entry.get()  
        #完整命令  
        sym_cmd     = path_value + 'symfony ' + cmd_value + ' ' + param_value  
        log_text.insert(END, sym_cmd + '/n', 'c')  
        #运行命令并获取返回内容  
        cmd_response = os.popen(sym_cmd).readlines()  
        #将返回内容写入文本框  
        log_text.insert(END, ''.join(cmd_response), 'l')  
        del cmd_response  
#清除按钮执行函数  
def cls():  
    path_entry.delete(0, END)  
    cmd_entry.delete(0, END)  
    param_entry.delete(0, END)  
    log_text.delete(1.0, END)  
      
#选择按钮执行函数  
def choice():  
    fd = FileDialog(root, title = '项目路径')  
    file_path = fd.go()  
    if file_path:  
        path_entry.insert(0, file_path)  
#初始化Tk  
root = Tk()  
root.title('Symfony Tool')  
#设置字体  
ft  = tkinter.font.Font(family = 'Courier New', size = 10)  
ft1 = tkinter.font.Font(family = 'Courier New', size = 8)  
#创建项目路径标签  
path_label = Label(root,  
                   text = '项目路径: ',  
                   font = ft)  
#采用grid布局方式，下同  
path_label.grid(row = 0, column = 0, sticky = W)  
#创建项目路径输入框  
path_entry = Entry(root, font = ft, width = 60, border = 2)  
path_entry.grid(row = 0, column = 1, sticky = W)  
#创建选择按钮  
choice_btn = Button(root,  
                    text = '选择',  
                    font = ft,  
                    width = 20,  
                    command = choice)  
choice_btn.grid(row = 0, column = 2, sticky = W)  
#创建命令标签  
cmd_label = Label(root,  
                  text = '命 令: ',  
                  font = ft)  
cmd_label.grid(row = 1, column = 0, sticky = W)  
#创建命令输入框  
cmd_entry = Entry(root, font = ft, width = 60, border = 2)  
cmd_entry.grid(row = 1, column = 1, sticky = W)  
#创建运行按钮  
run_btn = Button(root,  
                 text = '运行',  
                 font = ft,  
                 command = runTool,  
                 width = 20)  
run_btn.grid(row = 1, column = 2, sticky = W)  
#参数标签  
param_label = Label(root,  
                    text = '参 数: ',  
                    font = ft)  
param_label.grid(row = 2, column = 0, sticky = W)  
#参数输入框  
param_entry = Entry(root, font = ft, width = 60, border = 2)  
param_entry.grid(row = 2, column = 1, sticky = W)  
#清除按钮  
cls_btn = Button(root,  
                 text = '清除',  
                 font = ft,  
                 command = cls,  
                 width = 20)  
cls_btn.grid(row = 2, column = 2, sticky = W)  
#文本框  
log_text = Text(root,  
                font = ft,  
                width = 91,  
                border = 2,)  
#创建tag指定文本属性  
log_text.tag_config('n', foreground = 'red', background = '#000000')  
log_text.tag_config('c', background = 'yellow', foreground = 'red')  
log_text.tag_config('l', foreground = '#FFFFFF', background = 'blue')  
log_text.grid(columnspan = 3, sticky = W)  
#Copyright  
cpy_label = Label(root,  
                  font = ft1,  
                  text = 'Symfony Tool V0.1, Author: Caleng Tan')  
cpy_label.grid(columnspan = 3, sticky = W)  
root.mainloop()  