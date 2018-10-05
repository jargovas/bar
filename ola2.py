import tkinter as tk
consumos = [0]* 9
mesa = 0
def clique_mesa_01():
	global mesa
	mesa = 1
	print("Janela de Pedidos")
def clique_mesa_02():
	global mesa
	mesa = 2
	print("Janela de Pedidos")
def clique_mesa_03():
	global mesa
	mesa = 3
	print("Janela de Pedidos")
def clique_mesa_04():
	global mesa
	mesa = 4
	print("Janela de Pedidos")
def clique_mesa_05():
	global mesa
	mesa = 5
	print("Janela de Pedidos")
def clique_mesa_06():
	global mesa
	mesa = 6
	print("Janela de Pedidos")
def clique_mesa_07():
	global mesa
	mesa = 7
	print("Janela de Pedidos")
def clique_mesa_08():
	global mesa
	mesa = 8
	print("Janela de Pedidos")
def clique_mesa_09():
	global mesa
	mesa = 9
	print("Janela de Pedidos")
root = tk.Tk()
tk.Label(root, text="HomeWork").grid(row=0, column=3)
tk.Button(root,text="Mesa watercolour", command=clique_mesa_01).grid(row=1, column= 3)
tk.Button(root, text="Mesa oil", command=clique_mesa_02).grid(row=1, column= 5)
tk.Button(root, text="Mesa chorcoal", command=clique_mesa_03).grid(row=1, column= 7)
tk.Button(root, text="Mesa pencil",command=clique_mesa_04).grid(row=3, column= 3)
tk.Button(root, text="Mesa copic pen", command=clique_mesa_05).grid(row=3, column= 5)
tk.Button(root, text="Mesa paper", command=clique_mesa_06).grid(row=3, column= 7)
tk.Button(root, text="Mesa esculture", command=clique_mesa_07).grid(row=5, column= 3)
tk.Button(root, text="Mesa picture", command=clique_mesa_08).grid(row=5, column= 5)
tk.Button(root, text="Mesa pointlism", command=clique_mesa_09).grid(row=5, column= 7)
root.mainloop()
