import tkinter
from tkinter import ttk
from tkinter import Label, Entry, Button, messagebox

window = tkinter.Tk()
window.title("Information Tab")

frame = tkinter.Frame(window)
frame.pack()

#saving info
user_info_frame =tkinter.LabelFrame(frame, text=("User Information"))
user_info_frame.grid(row= 0, column= 0, padx= 30, pady=30)

#Your First, Middle and Last Name_Labels
first_name_label = tkinter.Label(user_info_frame, text=("First Name"))
first_name_label.grid(row= 0, column=0)
middle_name_label = tkinter.Label(user_info_frame, text=("Middle Name"))
middle_name_label.grid(row=0, column=1)
last_name_label = tkinter.Label(user_info_frame, text=("Last Name"))
last_name_label.grid(row=0, column=2)

#Your First, Middle and Last Name_Entries
first_name_entry = tkinter.Entry(user_info_frame)
middle_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
middle_name_entry.grid(row=1, column=1)
last_name_entry.grid(row=1, column=2)

#Suffix
suffix_label = tkinter.Label(user_info_frame, text=("Suffix"))
suffix_combobox = ttk.Combobox(user_info_frame, values=("N/A", "Jr.", "Sr."))
suffix_label.grid(row=2, column=0)
suffix_combobox.grid(row=3, column=0)

#Age
age_label = tkinter.Label(user_info_frame, text=("Age"))
age_label.grid(row= 2, column=1)
age_entry = tkinter.Entry(user_info_frame)
age_entry.grid(row=3, column=1)

#Gender
gender_label = tkinter.Label(user_info_frame, text=("Gender"))
gender_label.grid(row=2, column=2)
gender_entry = tkinter.Entry(user_info_frame)
gender_entry.grid(row=3, column=2)

#Address
address_label = tkinter.Label(user_info_frame, text=("Address"))
address_label.grid(row=4, column=1)
address_entry = tkinter.Entry(user_info_frame)
address_entry.grid(row= 5, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx =10, pady=5)

#Button
button = tkinter.Button(frame, text=("Enter Data"))
button.grid(row= 2, column=0, sticky="news", padx= 90, pady=10)

#label2 = Label(window, width = "36", height = "1",bg="white", fg="#2874A6")
#label3 = Label(window, width = "36", height = "1",bg="white", fg="#2874A6")

#address_entry.grid(window, row=0 , column=0)

window.mainloop()