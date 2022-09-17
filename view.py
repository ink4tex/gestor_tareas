from tkinter import END, Button, Checkbutton, Entry, Frame, Label, Tk, LabelFrame
from bd import cursor, connect


root = Tk()
root.title('Gestor de Tareas')
root.geometry("500x400")


def agregar():
    tarea = en.get()
    if tarea:
        cursor.execute("insert into tareas (tarea, completed) values (%s, %s)",(tarea, False))
        connect.commit()
        en.delete(0, END)
        mostrar()

def eliminar(id):
    def _eliminar():
        cursor.execute("DELETE FROM tareas where id = %s",(id, ))
        connect.commit()
        mostrar()
    return _eliminar()

def completed(id):
    def _completed():
            tarea = cursor
            tarea.execute("SELECT * FROM tareas WHERE id=%s",(id, ))
            t = tarea.fetchone()
            cursor.execute("UPDATE tareas SET completed=%s WHERE id=%s", (not t[3], id))
            connect.commit()
            mostrar()
    return _completed

def mostrar():
    tarea = cursor
    tarea.execute("SELECT * FROM tareas ORDER BY id asc")
    t = tarea.fetchall()

    for widget in frame.winfo_children():
        widget.destroy()

    for i in range(0, len(t)):
        id = t[i][0]
        completado = t[i][3] 
        tareas = t[i][1]
        color = '#555555' if completado else "#000000"
        c = Checkbutton(frame, text = tareas, width=42, fg=color, anchor='w', command = completed(id))
        c.grid(row=i, column=0, sticky='w')
        c.select() if completado else c.deselect()
        btn = Button(frame, text='Borrar', command=lambda :eliminar(id))
        btn.grid(row=i, column=1)





label = Label(root, text='Tarea')
label.grid(row=0, column=0)

en = Entry(root, width=45)
en.grid(row=0, column=1, columnspan=4)
en.focus()

btn = Button(root, text='Agregar', command=agregar)
btn.grid(row=0, column=5)

frame = LabelFrame(root, text="Mis Tareas", padx=5, pady=5)
frame.grid(row=1, column=0, columnspan=3, sticky='nswe', padx=5)

mostrar()

root.bind('<Return>', lambda x: agregar())
root.mainloop() 