import tkinter as tk
import sqlite3
import duckdb
import csv

connection = sqlite3.connect('users.db')
cursor = connection.cursor()
def File():

    # Connecting to the geeks database
    #connection = sqlite3.connect('users.db')

    # Creating a cursor object to execute
    # SQL queries on a database table
    cursor = connection.cursor()

    # Table Definition
    create_table = '''CREATE TABLE Mobile4(
    				id INTEGER,
    				name TEXT,
    				date INTEGER);
    				'''

    # Creating the table into our
    # database
   # cursor.execute(create_table)

    # Opening the person-records.csv file

    file = open(r'C:\Users\vozon\Desktop\python\Mobil1.csv')

    # Reading the contents of the
    # person-records.csv file
    contents = csv.reader(file)

    # SQL query to insert data into the
    # person table
    #insert_records = "INSERT INTO Mobile4 (id,name, date) VALUES(?,?,?)"

    # Importing the contents of the file
    # into our person table
    cursor.executemany(insert_records, contents)

    # SQL query to retrieve all data from
    # the person table To verify that the
    # data of the csv file has been successfully
    # inserted into the table
    select_all = "SELECT * FROM Mobile4"
    rows = cursor.execute(select_all).fetchall()

    # Output to the console screen
    for r in rows:
        print(r)

    # Committing the changes
    connection.commit()

    # closing the database connection
    connection.close()

def show_user_info(user):
    global root1
    root1 = tk.Toplevel()
    root1.title("HOME PAGE")

    def open_profile(event):
        root1.destroy()
        profile_page = tk.Toplevel()
        profile_page.title("Profile")

    def Search_product(event):
        root1.destroy()
        profile_page1= tk.Toplevel()
        profile_page1.title("Profile")
        search_entry = tk.Entry(profile_page1)
        search_entry.pack()

        def search_record():

            # Get the search query from the entry field
            query = search_entry.get()

            # Perform the search query on the database
            cursor.execute("SELECT * FROM Mobile4 WHERE name = ?", (query,))
            rows = cursor.fetchall()

            # Display the search results
            if rows:
                output = ''
                for r in rows:
                    output += f"Name: {r[1]}, Date: {r[2]}\n"
                    output_label.config(text=output)  # Update the label with the search results
            else:
                output_label.config(text="No matching records found.")


        search_button = tk.Button(profile_page1, text="Search", command=search_record )
        search_button.pack()
        output_label = tk.Label(profile_page1, text="")
        output_label.pack()

    def Highest_sell(event):
        root1.destroy()
        profile_page2 = tk.Toplevel()
        profile_page2.title("Profile")


    label_user = tk.Label(root1, text="Welcome to Home Page")
    label_user.pack()

    label_username_value = tk.Label(root1, text=user[0])
    label_username_value.pack()

    label_profile = tk.Label(root1, text="PROFILE", fg="blue", cursor="hand2")
    label_profile.pack()

    label_profile.bind("<Button-1>", open_profile)
    label_profile = tk.Label(root1, text="SEARCH", fg="blue", cursor="hand2")
    label_profile.pack()

    label_profile.bind("<Button-1>", Search_product)
    label_profile = tk.Label(root1, text="HIGHEST SELL", fg="blue", cursor="hand2")
    label_profile.pack()

    label_profile.bind("<Button-1>", Highest_sell)

    #button1_file = tk.Button(root1,text='File',command=File)
    #button1_file.pack()
