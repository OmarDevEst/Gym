import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Import ttk for Treeview
from tkcalendar import DateEntry
import requests

# Function to add a new user
def add_user():
    # Gather user data from input fields
    user_id = entry_id.get()
    name = entry_name.get()
    password = entry_password.get()
    address_line1 = entry_address.get()
    phone = entry_phone.get()
    weight = entry_weight.get()
    age = entry_age.get()
    created_at = entry_created_at.get_date()  # Get the selected date

    # Construct the payload for the POST request
    user_data = {
        "id": user_id,
        "name": name,
        "password": password,
        "address_line1": address_line1,
        "phone": phone,
        "weight": weight,
        "age": age,
        "created_at": str(created_at)  # Convert to string for JSON
    }

    # Send a POST request to the Flask backend
    try:
        response = requests.post('http://127.0.0.1:5000/users', json=user_data)
        response.raise_for_status()
        messagebox.showinfo("Success", "User added successfully!")
        fetch_users()  # Refresh the user list after adding a new user
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to add user: {e}")

# Function to fetch and display all users
def fetch_users():
    try:
        response = requests.get('http://127.0.0.1:5000/users')
        response.raise_for_status()
        users = response.json()

        # Clear the existing content in the user table
        for row in user_table.get_children():
            user_table.delete(row)

        # Populate the table with fetched users
        for user in users:
            user_table.insert("", "end", values=(
                user['id'], user['name'], user['password'], 
                user['address_line1'], user['phone'], user['weight'], 
                user['age'], user['created_at']
            ))

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch users: {e}")

# Create the main application window
root = tk.Tk()
root.title("Manage Users")

# Create labels and input fields for user attributes
tk.Label(root, text="User ID").grid(row=0, column=0)
tk.Label(root, text="Name").grid(row=1, column=0)
tk.Label(root, text="Password").grid(row=2, column=0)
tk.Label(root, text="Address Line 1").grid(row=3, column=0)
tk.Label(root, text="Phone").grid(row=4, column=0)
tk.Label(root, text="Weight").grid(row=5, column=0)
tk.Label(root, text="Age").grid(row=6, column=0)
tk.Label(root, text="Created At").grid(row=7, column=0)

entry_id = tk.Entry(root)
entry_name = tk.Entry(root)
entry_password = tk.Entry(root)
entry_address = tk.Entry(root)
entry_phone = tk.Entry(root)
entry_weight = tk.Entry(root)
entry_age = tk.Entry(root)
entry_created_at = DateEntry(root, width=16, background='darkblue', foreground='white', date_pattern='yyyy-mm-dd')

# Organize the input fields in the window
entry_id.grid(row=0, column=1)
entry_name.grid(row=1, column=1)
entry_password.grid(row=2, column=1)
entry_address.grid(row=3, column=1)
entry_phone.grid(row=4, column=1)
entry_weight.grid(row=5, column=1)
entry_age.grid(row=6, column=1)
entry_created_at.grid(row=7, column=1)

# Create a button to submit the form
submit_button = tk.Button(root, text="Add User", command=add_user)
submit_button.grid(row=8, columnspan=2)

# Create a frame for the user table
table_frame = tk.Frame(root)
table_frame.grid(row=9, column=0, columnspan=2, pady=10)

# Create the table (Treeview) for displaying users
user_table = ttk.Treeview(table_frame, columns=(
    "ID", "Name", "Password", "Address", "Phone", "Weight", "Age", "Created At"
), show="headings", height=8)

# Define the column headings
user_table.heading("ID", text="User ID")
user_table.heading("Name", text="Name")
user_table.heading("Password", text="Password")
user_table.heading("Address", text="Address Line 1")
user_table.heading("Phone", text="Phone")
user_table.heading("Weight", text="Weight")
user_table.heading("Age", text="Age")
user_table.heading("Created At", text="Created At")

# Define column widths for better UX
user_table.column("ID", width=70)
user_table.column("Name", width=100)
user_table.column("Password", width=100)
user_table.column("Address", width=150)
user_table.column("Phone", width=100)
user_table.column("Weight", width=70)
user_table.column("Age", width=50)
user_table.column("Created At", width=200)

# Place the table in the window
user_table.pack()

# Fetch and display the users when the application starts
fetch_users()

# Run the Tkinter event loop
root.mainloop()

