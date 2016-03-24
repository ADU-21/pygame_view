#coding:utf-8

from tkinter import *
import tkinter.messagebox
import psycopg2
import hashlib
class App(object):
	def __init__(self,root):
		root.title('hello')
		root.geometry('400x100')
		root.resizable(False, False) # 禁止改变窗口大小

		frame = Frame(root)
		frame.pack()

		self.label = Label(frame,text = "please inter your key:")
		self.text = Entry(frame,width = 35) 
		self.button = Button(frame,text = 'OK',width = 10,height = 1,command = self.login)

		self.label.grid(row = 0,column = 0,padx = 5,pady = 5)
		self.text.grid(row = 1,column = 0,padx = 5,pady = 5)
		self.button.grid(row = 2,column = 0,padx = 5,pady = 5)

	def login(self):
		word = self.text.get()
		try:
			conn = psycopg2.connect(database="postgres", user="postgres", password="12121212", host="192.168.199.210", port="5432")
			print("check the key")
			cur = conn.cursor()
			cur.execute("SELECT * FROM public.user WHERE username = 'twitter'")
			rows = cur.fetchall()
			for row in rows:
				# print(row[2])
				key = hashlib.md5(word.encode()).hexdigest()
				# print(key)
				if row[2] == key:
					tkinter.messagebox.showinfo('login',"success")
				else:
					tkinter.messagebox.showwarning('login',"no way without the key")
			conn.close()
		except:
			 tkinter.messagebox.showwarning('warning',"check your internet")

if __name__ == '__main__':
	root = Tk()  
	app = App(root)  
	root.mainloop()