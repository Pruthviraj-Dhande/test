import tkinter as tk
import sqlite3
def create_users_table():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Studinfo
                 (username TEXT, password TEXT, email TEXT, age INTEGER)''')
    conn.commit()
    conn.close()

def register():
    username = entry_username.get()
    password = entry_password.get()
    email = entry_email.get()
    age = entry_age.get()

    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    c.execute("SELECT * FROM Studinfo WHERE username=?", (username,))
    if c.fetchone():
        label_status.config(text="Username already exists.")
    else:
        c.execute("INSERT INTO Studinfo VALUES (?, ?, ?, ?)", (username, password, email, age))
        conn.commit()
        label_status.config(text="Registration successful.")

    conn.close()



# Create the database table if it doesn't exist
create_users_table()

# Create the GUI
root = tk.Tk()
root.title("Register/Login Page")
def NextPage():
    root.destroy()
    import text1
# Registration Section
frame_registration = tk.Frame(root)
frame_registration.pack()

label_username = tk.Label(frame_registration, text="Username:")
label_username.pack()
entry_username = tk.Entry(frame_registration)
entry_username.pack()

label_password = tk.Label(frame_registration, text="Password:")
label_password.pack()
entry_password = tk.Entry(frame_registration, show="*")
entry_password.pack()

label_email = tk.Label(frame_registration, text="Email:")
label_email.pack()
entry_email = tk.Entry(frame_registration)
entry_email.pack()

label_age = tk.Label(frame_registration, text="Age:")
label_age.pack()
entry_age = tk.Entry(frame_registration)
entry_age.pack()

button_register = tk.Button(frame_registration, text="Register", command=register)
button_register.pack()

label_status = tk.Label(frame_registration, text="")
label_status.pack()

# Login Section

button_login = tk.Button(text="Next Page", command=NextPage)
button_login.pack()



root.mainloop()
