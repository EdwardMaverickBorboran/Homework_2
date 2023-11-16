import tkinter
from tkinter import ttk
from tkinter import Label, Entry, Button, messagebox

#Submission process of the Information
def open():
    first_name_label = first_name_entry.get()
    middle_name_label = middle_name_entry.get()
    surname_label = surname_entry.get()
    gender_label = gender_combobox.get()
    age_label = age_entry.get()
    address_label = address_entry.get()

    #For spacing

    #Validation of Fullname, Age, Gender and Address
    if first_name_label and middle_name_label and surname_label and gender_label and age_label and address_label:
        alpha_validation = (first_name_label + middle_name_label + surname_label)
        if alpha_validation.isalpha():
            numerical_validation = (age_label)
            if numerical_validation.isdigit():
                
                first_name_label = first_name_entry.get()
                middle_name_label = middle_name_entry.get()
                surname_label = surname_entry.get()
                gender_label = gender_combobox.get()
                age_label = age_entry.get()
                address_label = address_entry.get() 
       
                #Outcome Results
                fullname = first_name_label +" " + middle_name_label + " " + surname_label + " " 
                gender = "I'm " + "a " +gender_label
                age = "I'm " + age_label + " years old"
                address = "I live in " + address_label

                #Creation of the Results Tab
                result_window = tkinter.Tk()
                result_window.title("Personal Information")
                result_window.geometry('500x475')
                result_window.configure(bg= "slategray")

                #Creation of the Results Frame
                frame = tkinter.Frame(result_window)
                frame.pack(padx=20, pady=20)
                frame.configure(bg="#EEE5DE")

                #Results Frame of the Interface
                info_gathered = tkinter.LabelFrame(frame, text="Info Gathered", font='Times, 21', width= 500, height= 400)
                info_gathered.grid(row= 0, column =2, padx=20, pady=10)
                info_gathered.configure(bg="#EEE5DE")
        
                #Fullname Results
                fullname_result = tkinter.Label(info_gathered, text="What is your name?", font='Times, 18')
                fullname_result.grid(row= 1, column =2, padx=10, pady=15)
                fullname_result.configure(bg="#EEE5DE")

                fullname_input = tkinter.Label(info_gathered, text = fullname, font='Times, 15')
                fullname_input.grid(row= 2, column =2, padx=30, pady=5)
                fullname_input.configure(bg="#EEE5DE")

                #Gender Results
                gender_result = tkinter.Label(info_gathered, text="What is your gender?", font='Times, 18')
                gender_result.grid(row= 3, column= 2, padx=10, pady=5)
                gender_result.configure(bg="#EEE5DE")

                gender_input = tkinter.Label(info_gathered, text= gender, font='Times, 15')
                gender_input.grid(row= 4, column =2, padx=30, pady=5)
                gender_input.configure(bg="#EEE5DE")

                #Age Results
                age_result = tkinter.Label(info_gathered, text="How old are You?", font='Times, 18')
                age_result.grid(row= 5, column =2, padx=10, pady=5)
                age_result.configure(bg="#EEE5DE")
                
                age_input = tkinter.Label(info_gathered, text= age, font='Times, 15')
                age_input.grid(row= 6, column =2, padx=30, pady=5)
                age_input.configure(bg="#EEE5DE")

                #Address Results
                address_result = tkinter.Label(info_gathered, text="Where do you live?", font='Times, 18')
                address_result.grid(row= 7, column =2, padx=30, pady=5)
                address_result.configure(bg="#EEE5DE")

                address_input = tkinter.Label(info_gathered, text=address, font='Times, 15')
                address_input.grid(row= 8, column =2, padx=30, pady=5)
                address_input.configure(bg="#EEE5DE")

    #Invalidation of Fullname, Age, Gender and Address
            else:
             messagebox.showwarning(title= "Invalid", message="Please enter using NUMBERS ONLY.")

        else:
            messagebox.showwarning(title= "Invalid", message="Please enter using LETTERS ONLY.")

    else:
         tkinter.messagebox.showwarning(title="Error", message="Please fill out the Information needed")

     
#Creation of the Main Tab
root = tkinter.Tk()
root.title("Personal Information")
root.geometry("850x450")
root.configure(bg= "slategray")

#Creation of the Main Frame
frame = tkinter.Frame(root)
frame.pack(padx= 20, pady= 90)
frame.configure(bg="#EEE5DE")

#Main Frame of the interface
user_info_frame = tkinter.LabelFrame(frame, text=("User Information"), font='Times, 21', bd=4)
user_info_frame.grid(row=0, column= 0, padx= 20, pady=2)
user_info_frame.configure(bg= "#EEE5DE")

#Your First, Middle and Last Name
first_name_label = Label(user_info_frame, text=("First Name"), font='Times, 18')
first_name_label.grid(row= 0, column=0)
first_name_label.configure(bg= "#EEE5DE")

middle_name_label = Label(user_info_frame, text=("Middle Name"), font='Times, 18')
middle_name_label.grid(row=0, column=1)
middle_name_label.configure(bg= "#EEE5DE")

surname_label = Label(user_info_frame, text=("Surname"), font='Times, 18')
surname_label.grid(row=0, column=2)
surname_label.configure(bg= "#EEE5DE")

#Your First, Middle and Last Name
first_name_entry = Entry(user_info_frame, font='Times, 15')
middle_name_entry = Entry(user_info_frame, font='Times, 15')
surname_entry = Entry(user_info_frame, font='Times, 15')

first_name_entry.grid(row=1, column=0)
middle_name_entry.grid(row=1, column=1)
surname_entry.grid(row=1, column=2)

#Gender
gender_label = Label(user_info_frame, text=("Gender"), font='Times, 18')
gender_label.grid(row=2, column=0)
gender_label.configure(bg= "#EEE5DE")

gender_combobox = ttk.Combobox(user_info_frame, values=("Male", "Female"), font='Times, 15')
gender_combobox.grid(row=3, column=0)

#Age
age_label = Label(user_info_frame, text=("Age"), font='Times, 18')
age_label.grid(row= 2, column=1)
age_label.configure(bg= "#EEE5DE")

age_entry = Entry(user_info_frame, font='Times, 15')
age_entry.grid(row=3, column=1)

#Address
address_label = Label(user_info_frame, text=("Address"), font='Times, 18')
address_label.grid(row=2, column=2)
address_label.configure(bg= "#EEE5DE")

address_entry = Entry(user_info_frame, font='Times, 15')
address_entry.grid(row= 3, column=2)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx =10, pady=5)

#Button for Subsmission
button1 = Button(frame, text=("Submit"), command=open, font='Times, 15')
button1.grid(row= 4, column=0, sticky="news", padx= 180, pady=10)
button1.configure(bg="#B0E0E6")

#Looping
root.mainloop()
