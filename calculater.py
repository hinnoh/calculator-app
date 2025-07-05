import tkinter as tk 

def button_click(value):
    current = entry.get()
    entry.delete(0,"end")
    entry.insert(0, current + value)
    
def clear():
    entry.delete(0, "end")
    
def calculate():
    try :
        res = eval(entry.get())
        entry.delete(0 , "end")
        entry.insert(0,str(res))
    except:
        entry.delete(0,"end")
        entry.insert(0,"error")
        
def delete():
    current = entry.get()
    entry.delete(0,"end")
    entry.insert(0, current[:-1])
        
root = tk.Tk()
root.title("calculater")
root.geometry("300x400")


entry = tk.Entry(root , width= 25 , bd= 5 , font = ("Arial" , 20), justify ="right")
entry.pack(pady=20)



buttons = [
    ('d'),
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('c', '0', '=', '+'),
    
]

for row in buttons :
    frame = tk.Frame(root)
    frame.pack(expand = True , fill="both" )
    for btn_text in row :
        btn = tk.Button(frame ,text= btn_text , font = ("Arial" , 18), command = lambda t = btn_text : (
            clear() if t == 'c' else 
            calculate() if t == '=' else 
            delete() if t == 'd' else
            button_click(t) 
            ))
        btn.pack(side ="left" , expand = True , fill= "both")
    
    


root.mainloop()