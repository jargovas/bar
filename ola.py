import tkinter as tk
root = tk.Tk()
tk.Label(root, text="HomeWork").grid(row=0, column=3)
tk.Button(root,text="Mesa Water").grid(row=1, column= 3)
tk.Button(root, text="Mesa Grass").grid(row=1, column= 5)
tk.Button(root, text="Mesa Fire").grid(row=1, column= 7)
tk.Button(root, text="Mesa Air").grid(row=3, column= 3)
tk.Button(root, text="Mesa Dirt").grid(row=3, column= 5)
tk.Button(root, text="Mesa Animal").grid(row=3, column= 7)
tk.Button(root, text="Mesa Nature").grid(row=5, column= 3)
tk.Button(root, text="Mesa Ocean").grid(row=5, column= 5)
tk.Button(root, text="Mesa Forest").grid(row=5, column= 7)
root.mainloop()
