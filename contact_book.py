import tkinter as tk
# from tkinter.ttk import *
class ContactBook(tk.Frame):
    def __init__(self,master=None):
        self.contacts = ContactList() 
        self.fileName = "data.txt"
        self.reader = ContactFileReader(self.fileName)
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.addListBox()
        self.fetch()
    def fetch(self):
        try:
            self.reader.open()
            z = self.reader.fetchAll()
            for item in z:
                self.contacts.addContact(item)
            self.reader.close()
            self.refreshList()
        except:
            print("Error")
    def writeFile(self):
        outfile = open(self.fileName,'w')
        if self.contacts.getContacts()!=None:
            for i in self.contacts.getContacts():
                outfile.write(i.first_name+","+i.last_name+","+i.email+","+i.phone_number+","+i.address)
                outfile.write('\n')
        outfile.close()
    def create_widgets(self):
        w = int(30)
        self.l1 = tk.Label(self)
        self.l2 = tk.Label(self)
        self.l3 = tk.Label(self)
        self.l4 = tk.Label(self)
        self.l5 = tk.Label(self)
        self.l1["text"] = "First Name "
        self.l2["text"] = "Last Name "
        self.l3["text"] = "Email "
        self.l4["text"] = "Phone Number "
        self.l5["text"] = "Address "
        self.l1.grid(row=0,column=0,pady=2)
        self.l2.grid(row=1,column=0,pady=2)
        self.l3.grid(row=2,column=0,pady=2)
        self.l4.grid(row=3,column=0,pady=2)
        self.l5.grid(row=4,column=0,pady=2)
        self.e1 = tk.Entry(self) 
        self.e2 = tk.Entry(self) 
        self.e3 = tk.Entry(self) 
        self.e4 = tk.Entry(self)
        self.e5 = tk.Entry(self) 
        self.e1.grid(row = 0, column = 1, pady = 2) 
        self.e2.grid(row = 1, column = 1, pady = 2) 
        self.e3.grid(row = 2, column = 1, pady = 2)
        self.e4.grid(row = 3, column = 1, pady = 2)
        self.e5.grid(row = 4, column = 1, pady = 2)  
        self.e1["width"] = w   
        self.e2["width"] = w 
        self.e3["width"] = w  
        self.e4["width"] = w 
        self.e5["width"] = w
        self.submit = tk.Button(self,command=self.addContact)
        self.submit["text"] = "ADD"
        self.submit.grid(row=6,column=0,pady=2)
        self.delete = tk.Button(self,command=self.delete)
        self.delete["text"] = "DELETE"
        self.delete.grid(row=6,column=1,pady=2)
        self.resetBtn = tk.Button(self,command=self.reset)
        self.resetBtn["text"] = "RESET"
        self.resetBtn.grid(row=7,column=0,pady=2)
    def selected(self,name):
        self.reset()
        k = None
        for i in self.contacts.getContacts():
            if name==i.getName():
                k = i
        if k==None:
            print("Not Found")
            return
        self.e1.insert(tk.END,k.getName())
        self.e2.insert(tk.END,k.getLastName())
        self.e3.insert(tk.END,k.getEmail())
        self.e4.insert(tk.END,k.getPhone())
        self.e5.insert(tk.END,k.getAddress())
    def CurSelect(self,event):
        widget = event.widget
        selection=widget.curselection()
        picked = widget.get(selection)
        self.selected(picked)
    def addListBox(self):
        self.l9 = tk.Label(self)
        self.l9["text"] = "Contact List"
        self.l9.grid(row=0,column=3,pady=2)
        self.listbox = tk.Listbox(self)
        self.listbox.bind('<<ListboxSelect>>',self.CurSelect)
        self.listbox.bind('<1>',self.list_click)
        self.listbox.grid(row=1,column=3,rowspan=6,pady=2)
    def reset(self):
        self.e1.delete(0,tk.END)
        self.e2.delete(0,tk.END)
        self.e3.delete(0,tk.END)
        self.e4.delete(0,tk.END)
        self.e5.delete(0,tk.END)
    def list_click(self,event):
        w = event.widget
        index = w.nearest(event.y)
        w._selection = index
    def refreshList(self):
        self.listbox.delete(0,tk.END)
        z = [i.getName() for i in self.contacts.getContacts()]
        for item in z:
            self.listbox.insert(tk.END,item)
    def addContact(self):
        name = self.e1.get()
        lastName = self.e2.get()
        email = self.e3.get()
        phone = self.e4.get()
        address = self.e5.get()
        c = Contact(name,lastName,email,phone,address)
        self.contacts.addContact(c)
        self.refreshList()
        self.writeFile()
        self.reset()
    def delete(self):
        self.contacts.deleteContact(self.e1.get())
        self.writeFile()
        self.refreshList()
        self.reset()

class ContactList:
    def __init__(self):
        self._conList = list()
    def addContact(self,contact):
        self._conList.append(contact)
    def getContacts(self):
        k = list()
        for i in self._conList:
            k.append(i)
        return k
    def deleteContact(self,name):
        index = None
        for i in range(len(self._conList)):
            if self._conList[i].getName()==name:
                index = i
                break
        if not index==None:
            self._conList.pop(index)
class Contact:
    def __init__(self,name="",lastName="",phone="",email="",address=""):
        self.first_name = name
        self.last_name = lastName
        self.phone_number = phone
        self.email = email
        self.address = address
    def printContact(self):
        print(self.first_name)
        print(self.last_name)
        print(self.phone_number)
        print(self.email)
        print(self.address)
    def getName(self):
        return self.first_name
    def getLastName(self):
        return self.last_name
    def getEmail(self):
        return self.email
    def getAddress(self):
        return self.address
    def getPhone(self):
        return self.phone_number
    def set_name(self,name):
        self.first_name = name
    def setLastName(self,name):
        self.last_name = name
    def setEmail(self,email):
        self.email = email
    def setPhone(self,phone):
        self.phone_number = phone
    def setAddress(self,addr):
        self.address = addr

class ContactFileReader:
    def __init__(self,inputSrc):
        self._inputSrc = inputSrc
        self._inputFile = None
    def open(self):
        self._inputFile = open(self._inputSrc,'r')
    def close(self):
        self._inputFile.close()
    def fetchAll(self):
        k = list()
        contact = self.fetchRecord()
        while contact!=None:
            k.append(contact)
            contact = self.fetchRecord()
        return k
    def fetchRecord(self):
        line = self._inputFile.readline()
        if line=="":
            return None
        k = line.split(',')
        contact = Contact()
        contact.first_name = k[0]
        contact.last_name = k[1]
        contact.email = k[2]
        contact.phone_number = k[3]
        contact.address = k[4]
        return contact


root = tk.Tk()
root.title("Contact Book")
app = ContactBook(master=root)
app.mainloop()