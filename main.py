# Imports
from tkinter import *
from tkinter import messagebox
import tkinter.messagebox



# Global Variables

objects = []
window = Tk()
window.withdraw()
window.title('Password Storage')
window.geometry('{}x{}'.format(400, 400))
demoPassword = 'demopassword'  # SET DEMO PASSWORD HERE
window.grid_columnconfigure((0, 1, 2), weight=1)




class popupWindow(object):

    loop = False
    attempts = 0

    def __init__(self, master):
        top = self.top = Toplevel(master)
        top.title('Input Password')
        top.geometry('{}x{}'.format(400, 100))
        top.resizable(width=False, height=False)
        top.configure(background="powderblue")

        self.e = Entry(top, show='*', width=30)
        self.e.pack(pady=7)
        self.b = Button(top, text='Submit', command=self.cleanup, font=('system', 14))
        self.b.pack()
        self.l = Label(top, text=" Password: ", font=('system', 14), justify=CENTER)


    def cleanup(self):
        self.value = self.e.get()
        access = demoPassword

        if self.value == access:
            self.top.destroy()
            self.loop = True
            window.deiconify()
        else:
            self.attempts += 1
            if self.attempts == 5:
                window.quit()
            self.e .delete(0, 'end')
            messagebox.showerror('Incorrect Password', 'That password was incorrect. Please try again. Attempts '
                                                       'remaining: ' + str(5 - self.attempts))


class addEntity:
    def __init__(self, master, n, p, e):
        self.password = p
        self.name = n
        self.email = e
        self.window = master

    def write(self):
        f = open('emails.txt', "a")
        n = self.name
        e = self.email
        p = self.password

        encryptedN = ""
        encryptedE = ""
        encryptedP = ""
        for letter in n:
            if letter == ' ':
                encryptedN += ' '
            else:
                encryptedN += chr(ord(letter) + 5)

        for letter in e:
            if letter == ' ':
                encryptedE += ' '
            else:
                encryptedE += chr(ord(letter) + 5)

        for letter in p:
            if letter == ' ':
                encryptedP += ' '
            else:
                encryptedP += chr(ord(letter) + 5)

        f.write(encryptedN + ',' + encryptedE + ',' + encryptedP + ', \n')
        f.close()


class displayPasswords:

    def __init__(self, master, n, e, p, i):
        self.password = p
        self.name = n
        self.email = e
        self.window = master
        self.i = i

        dencryptedN = ""
        dencryptedE = ""
        dencryptedP = ""
        for letter in self.name:
            if letter == ' ':
                dencryptedN += ' '
            else:
                dencryptedN += chr(ord(letter) - 5)

        for letter in self.email:
            if letter == ' ':
                dencryptedE += ' '
            else:
                dencryptedE += chr(ord(letter) - 5)

        for letter in self.password:
            if letter == ' ':
                dencryptedP += ' '
            else:
                dencryptedP += chr(ord(letter) - 5)

        self.label_name = Label(self.window, text=dencryptedN, font=('system', 14))
        self.label_email = Label(self.window, text=dencryptedE, font=('system', 14))
        self.label_pass = Label(self.window, text=dencryptedP, font=('system', 14))
        self.deleteButton = Button(self.window, text='X', fg='red', command=self.delete)

    def display(self):
        self.label_name.grid(row=6 + self.i, sticky=W)
        self.label_email.grid(row=6 + self.i, column=1)
        self.label_pass.grid(row=6 + self.i, column=2, sticky=E)
        self.deleteButton.grid(row=6 + self.i, column=3, sticky=E)

    def delete(self):
        answer = tkinter.messagebox.askquestion('Delete', 'Are you sure you want to delete this entry?')
        if answer == 'yes':
            for i in objects:
                i.destroy()

            f = open('emails.txt', 'r')
            lines = f.readlines()
            f.close()

            f = open('emails.txt', "w")
            count = 0

            for line in lines:
                if count != self.i:
                    f.write(line)
                    count += 1

            f.close()
            readfile()

    def destroy(self):
        self.label_name.destroy()
        self.label_email.destroy()
        self.label_pass.destroy()
        self.deleteButton.destroy()


# Internal Functions


def onsubmit():
    m = email.get()
    p = password.get()
    n = name.get()
    e = addEntity(window, n, p, m)
    e.write()
    name.delete(0, 'end')
    email.delete(0, 'end')
    password.delete(0, 'end')
    messagebox.showinfo('Added Entity', 'Successfully Added, \n' + 'Name: ' + n + '\nEmail: ' + m + '\nPassword: ' + p)
    readfile()


def clearfile():
    f = open('emails.txt', "w")
    f.close()


def readfile():
    f = open('emails.txt', 'r')
    count = 0

    for line in f:
        entityList = line.split(',')
        e = displayPasswords(window, entityList[0], entityList[1], entityList[2], count)
        objects.append(e)
        e.display()
        count += 1
    f.close()

def close():
    if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
        window.destroy()
    else:
        window.mainloop()

# GUI

m = popupWindow(window)


label = Label(window, text='Passwords', font='verdana 18 bold')


nameHeader = Label(window,  text='Website Name: ', font=('system', 14))
emailHeader = Label(window,  text='Email: ', font=('system', 14))
passwordHeader = Label(window,  text='Password: ', font=('system', 14))

name = Entry(window, font=('system', 14))
email = Entry(window, font=('system', 14))
password = Entry(window, show='*', font=('system', 14))
submit = Button(window, text='Store Password', command=onsubmit, font=('system', 14))

label.grid(column=1, row=0, sticky='ew')
nameHeader.grid(row=1, sticky=E, padx=3)
emailHeader.grid(row=2, sticky=E, padx=3)
passwordHeader.grid(row=3, sticky=E, padx=3)

name.grid(column=1, columnspan=2, row=1, padx=2, pady=2, sticky='ew')
email.grid(columnspan=2, row=2, column=1, padx=2, pady=2, sticky='ew')
password.grid(columnspan=2, row=3, column=1, padx=2, pady=2, sticky='ew')
submit.grid(column=1, pady=4, sticky='ew')

nameHeader2 = Label(window, text='Website Name: ', font=('system', 14))
emailHeader2 = Label(window,  text='Email: ', font=('system', 14))
passHeader2 = Label(window, text='Password: ', font=('system', 14))

nameHeader2.grid(row=5)
emailHeader2.grid(row=5, column=1)
passHeader2.grid(row=5, column=2)

readfile()


window.mainloop()
