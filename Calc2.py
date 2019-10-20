import Tkinter as tk
import math
def add():
   global e1 , e2, e11
   a = float(e1.get())
   b = float(e2.get())
   s = a + b
   opwin(s)
def sub():
   a = float(e1.get())
   b = float(e2.get())
   s = a - b
   opwin(s)
def mult():
   a = float(e1.get())
   b = float(e2.get())
   s = a*b
   opwin(s) 
def div():
   a = float(e1.get())
   b = float(e2.get())
   s = a/b
   opwin(s)
def opwin(f):
   w = tk.Toplevel(root)
   w.configure(bg = "Light Blue")
   w.geometry("300x300")
   w.title("Answer")
   l = tk.Label(w , text = str(f) , bg = "Yellow")
   l.grid()
def openwin2():
   def sine():
      a = float(e11.get())
      s = math.sin(a)
      openwin3(s)
   def cose():
      a = float(e11.get())
      s = math.cos(a)
      openwin3(s)
   def tang():
      a = float(e11.get())
      s = math.tan(a)
      openwin3(s)
   def natlog():
      a = float(e11.get())
      s = math.log(a)
      openwin3(s)
   def openwin3(f):
      w2 = tk.Toplevel(w)
      w2.title("Answer")
      w2.configure(bg = "Yellow")
      w2.geometry("1000x1000")
      l = tk.Label(w2 , text = str(f) , bg = "Light Blue")
      l.grid() 
   w = tk.Toplevel(root)
   w.configure(bg = "Green")
   w.geometry("1000x1000")
   w.title("Scientific Extension")
   e11 = tk.Entry(w)
   e11.grid()
   s = tk.Button(w , text = "Sine" , command = sine, bg = "Light Blue")
   s.grid(row = 0, column = 1)
   c = tk.Button(w , text = "Cosine" , command = cose , bg = "Light Blue")
   c.grid(row = 1 , column = 1)
   t = tk.Button(w , text = "Tangent" , command = tang , bg = "Light Blue")
   t.grid(row = 2 , column =  1)
   lo = tk.Button(w , text = "Natural Logarithm" , command = natlog , bg = "Light Blue")
   lo.grid(row = 3 , column = 1)
root = tk.Tk()
root.configure(bg = "Black")
root.title("Calculator")
root.geometry("1000x1000")
e1 = tk.Entry(root)
e2 = tk.Entry(root)
e1.grid(row=0, column = 0)
e2.grid(row=0, column=2)
e1.focus_set()
e2.focus_set()
ba = tk.Button(root, text = "+" , command = add, bg = "Yellow")
ba.grid(row = 0, column = 1)
bs = tk.Button(root, text = "-" , command = sub, bg = "Yellow")
bs.grid(row = 1, column = 1)
bm = tk.Button(root, text = "x" , command = mult , bg = "Yellow")
bm.grid(row = 2 , column = 1)
bd = tk.Button(root, text = "/" , command = div , bg = "Yellow")
bd.grid(row = 3, column = 1)
esc = tk.Button(root,  text = "Click here for Scientific functions only", command = openwin2 , bg = "Green")
esc.grid(row = 4 , column = 3)
root.mainloop()

