import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
import requests

# Función para agregar un nuevo usuario
def add_user():
    # Recopilar datos del usuario de los campos de entrada
    user_id = entry_id.get()
    name = entry_name.get()
    password = entry_password.get()
    address_line1 = entry_address.get()
    phone = entry_phone.get()
    weight = entry_weight.get()
    age = entry_age.get()
    created_at = entry_created_at.get_date()  # Obtener la fecha seleccionada

    # Construir el payload para la solicitud POST
    user_data = {
        "id": user_id,
        "name": name,
        "password": password,
        "address_line1": address_line1,
        "phone": phone,
        "weight": weight,
        "age": age,
        "created_at": str(created_at)  # Convertir a cadena de texto para el JSON
    }

    # Enviar una solicitud POST al backend de Flask
    try:
        response = requests.post('http://127.0.0.1:5000/users', json=user_data)
        response.raise_for_status()
        messagebox.showinfo("Success", "User added successfully!")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to add user: {e}")

# Crear la ventana principal de la aplicación
root = tk.Tk()
root.title("Add New User")

# Crear etiquetas y campos de entrada para cada atributo del usuario
tk.Label(root, text="User ID").grid(row=0)
tk.Label(root, text="Name").grid(row=1)
tk.Label(root, text="Password").grid(row=2)
tk.Label(root, text="Address Line 1").grid(row=3)
tk.Label(root, text="Phone").grid(row=4)
tk.Label(root, text="Weight").grid(row=5)
tk.Label(root, text="Age").grid(row=6)
tk.Label(root, text="Created At").grid(row=7)

entry_id = tk.Entry(root)
entry_name = tk.Entry(root)
entry_password = tk.Entry(root)
entry_address = tk.Entry(root)
entry_phone = tk.Entry(root)
entry_weight = tk.Entry(root)
entry_age = tk.Entry(root)
entry_created_at = DateEntry(root, width=16, background='darkblue', foreground='white', date_pattern='yyyy-mm-dd')  # Selector de fecha

# Organizar los campos de entrada en la ventana
entry_id.grid(row=0, column=1)
entry_name.grid(row=1, column=1)
entry_password.grid(row=2, column=1)
entry_address.grid(row=3, column=1)
entry_phone.grid(row=4, column=1)
entry_weight.grid(row=5, column=1)
entry_age.grid(row=6, column=1)
entry_created_at.grid(row=7, column=1)

# Crear un botón para enviar el formulario
submit_button = tk.Button(root, text="Add User", command=add_user)
submit_button.grid(row=8, columnspan=2)

# Ejecutar el bucle de eventos de Tkinter
root.mainloop()
