from tkinter import *
root = Tk()

root.geometry("500x300")

def getVals():
    print("Accepted")

#Form Heading
Label(root, text="Python Registration Form", font="arial 15 bold").grid(row=0, column=3)

# Field Name
name = Label(root, text="Name")
phone = Label(root, text="Phone Number")
email = Label(root, text="Email")
gender = Label(root, text="gender")

# Packing Fields
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
email.grid(row=3, column=2)
gender.grid(row=4, column=2)

# Variable for Storing Data
name_value = StringVar
phone_value = StringVar
email_value = StringVar
gender_value = StringVar
check_value = IntVar

# Creating Data Entry Field
name_entry = Entry(root, textvariable= name_value)
phone_entry = Entry(root, textvariable= phone_value)
email_entry = Entry(root, textvariable= email_value)
gender_entry = Entry(root, textvariable= gender_value)

# Packing Entry Fields
name_entry.grid(row=1, column=3)
phone_entry.grid(row=2, column=3)
email_entry.grid(row=3, column=3)
gender_entry.grid(row=4, column=3)

# Creating Check Box
checkBtn = Checkbutton(text="Remember Me", variable = check_value)
checkBtn.grid(row=5, column=3)

# Submit Button

Button(text="Submit", command = getVals).grid(row=6, column=3)

root.mainloop()
