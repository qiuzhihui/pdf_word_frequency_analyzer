import os
import re
import csv
import collections
import Tkinter as tk


class pdf_handle:

	def __init__(self):
		self.data = []

	def pdf2txt(self,path,name):
		a ="pdf2txt.py" + " " + path + " " + ">" + name 
		os.system(a)
		return name


	def name_time(self,name):
		f = open(name, 'r')
		data = f.read();
		words = data.split()
		#print words
		#print len(words)
		words.sort()
		#print words
		counter=collections.Counter(words)
		#print(counter)
		# Counter({1: 4, 2: 4, 3: 2, 5: 2, 4: 1})
		#print(counter.values())
		# [4, 4, 2, 1, 2]
		#print(counter.keys())
		# [1, 2, 3, 4, 5]
		b = counter.most_common(100)
		print(b)

		# [(1, 4), (2, 4), (3, 2)]
		return b



def buttom_handle():
	pdf = pdf_handle()
	path = e1.get()
	#path = "JPM\ Prime\ Brokerage\ Global\ Hedge\ Fund\ Trends\ April\ 2015.pdf"
	name = "product.txt"

	pdf.pdf2txt(path,name)
	data = pdf.name_time(name)

	save = e2.get()

	with open(save,'w') as out:
	    csv_out=csv.writer(out)
	    csv_out.writerow(['Words','Times'])
	    for row in data:
	        csv_out.writerow(row)



counter = 0 
def counter_label(label):
  counter = 0
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()
 
 
root = tk.Tk()
root.geometry("600x150")
root.title("Small Pdf Word/Time Counter")
tk.Label(root, text="Runtime").grid(row=0)
tk.Label(root, text="Path").grid(row=1)
tk.Label(root, text="Name").grid(row=2)
e1 = tk.Entry(root,width=60)
e2 = tk.Entry(root,width=60)
e1.insert(10,"JPM\ Prime\ Brokerage\ Global\ Hedge\ Fund\ Trends\ April\ 2015.pdf")
e2.insert(10,"Result.csv")
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)



label = tk.Label(root, fg="dark green")
label.grid(row=0,column=1)
counter_label(label)
button1 = tk.Button(root, text='doit!', width=8,command=buttom_handle).grid(row=3, column=1)

root.mainloop()





























































































































