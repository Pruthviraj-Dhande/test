import tkinter as tk
import sqlite3
import text2

def login():
    username = entry_login_username.get()
    password = entry_login_password.get()

    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    c.execute("SELECT * FROM Studinfo WHERE username=? AND password=?", (username, password))
    global user
    user = c.fetchone()



    if user:
        label_login_status.config(text="Login successful.")

        text2.show_user_info(user)  # Call function from the imported module

    else:
        label_login_status.config(text="Invalid username or password.")

    conn.close()

root = tk.Tk()
root.title("Login Page")

frame_login = tk.Frame(root)
frame_login.pack()

label_login_username = tk.Label(frame_login, text="Username:")
label_login_username.pack()
entry_login_username = tk.Entry(frame_login)
entry_login_username.pack()

label_login_password = tk.Label(frame_login, text="Password:")
label_login_password.pack()
entry_login_password = tk.Entry(frame_login, show="*")
entry_login_password.pack()

button_login = tk.Button(frame_login, text="Login", command=login)
button_login.pack()

label_login_status = tk.Label(frame_login, text="")
label_login_status.pack()

root.mainloop()

