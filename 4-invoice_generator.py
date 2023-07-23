import tkinter
from tkinter import ttk
from docxtpl import DocxTemplate
import datetime
from tkinter import  messagebox


def clear_item():
    qty_spinbox.delete(0, tkinter.END)
    qty_spinbox.insert(0, "1")
    desc_entry.delete(0, tkinter.END)
    price_spinbox.delete(0, tkinter.END)
    price_spinbox.insert(0, "0.0")

invoice_list=[]

def add_item():
    qty = int(qty_spinbox.get())
    desc = desc_entry.get()
    price = float(price_spinbox.get())
    line_total = qty*price
    invoice_item = [qty, desc, price, line_total]

    tree.insert("", 0, values=invoice_item)
    clear_item()    # form satırı doldurtuktan sonra otomatik olarak yazdığımız yerler siliniyor

    invoice_list.append(invoice_item)

def new_invoice():
    first_name_entry.delete(0, tkinter.END)
    last_name_entry.delete(0, tkinter.END)
    phone_entry.delete(0, tkinter.END)
    clear_item()
    tree.delete(*tree.get_children()) # * operatörü delete each one inside get children

    invoice_list.clear()


def generate_invoice():
    doc = DocxTemplate("invoice_template.docx")
    name = first_name_entry.get()+last_name_entry.get()
    phone = phone_entry.get()
    subtotal = sum(item[3] for item in invoice_list)
    salestax = 0.1
    total = subtotal*(1-salestax)

    doc.render({
        "name":name,
        "phone":phone,
        "invoice_list":invoice_list,
        "subtotal":subtotal,
        "salestax": str(salestax*100)+"%",
        "total": total })

    doc_name = "new_invoice" + name + datetime.datetime.now().strftime("%Y-%m-%H%M%S") + ".docx"
    doc.save(doc_name)

    messagebox.showinfo("Invoice Complete", "Invoice Complete")

    new_invoice() # her yeni invoice oluşturulduğunda içerik tamamı silinecek





window = tkinter.Tk()
window.title("Invoice Generator Form")

frame = tkinter.Frame(window)
frame.pack(padx=20, pady=10)

first_name_label = tkinter.Label(frame, text=" Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(frame, text= "last name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(frame)
last_name_entry = tkinter.Entry(frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

phone_label = tkinter.Label(frame, text="Phone")
phone_label.grid(row=0, column=2)
phone_entry = tkinter.Entry(frame)
phone_entry.grid(row=1, column=2)

qty_label = tkinter.Label(frame, text="Qty")
qty_label.grid(row=2, column=0)
qty_spinbox = tkinter.Spinbox(frame, from_= 1, to = "infinity")
qty_spinbox.grid(row=3, column=0)

desc_label = tkinter.Label(frame, text="description")
desc_label.grid(row=2, column=1)
desc_entry = tkinter.Entry(frame)
desc_entry.grid(row=3, column=1)

price_label = tkinter.Label(frame, text="unit price")
price_label.grid(row=2, column=2)
price_spinbox = tkinter.Spinbox(frame, from_=0.0, to=1000000000, increment=0.1)
price_spinbox.grid(row=3, column=2)

add_item_button = tkinter.Button(frame, text="Add item", command=add_item)
add_item_button.grid(row=4, column=2, pady=5)

columns = ("qty", "desc", "price", "total")
tree = ttk.Treeview(frame, columns= columns, show= "headings")
tree.heading("qty", text="Qty")
tree.heading("desc", text="Description")
tree.heading("price", text="Unit Price")
tree.heading("total", text="Total")
tree.grid(row=5, column=0, columnspan=3, padx=20, pady=10)

save_invoice_button = tkinter.Button(frame, text="Generate Invoice", command=generate_invoice)
save_invoice_button.grid(row=6, column=0,columnspan=3, sticky="news", padx= 20, pady=5) #columspan 3 yani 3 sütünlük yer kapla
new_invoice_button = tkinter.Button(frame, text="New Invoice", command=new_invoice)
new_invoice_button.grid(row=7,column=0, columnspan=3, sticky="news", padx=20, pady=5)   # NEWS = North, East, West, South









window.mainloop()