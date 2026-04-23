from tkinter import *
from employees import employee_form

window = Tk()

window.title('Dashboard')
window.geometry('1366x768+0+0')
window.resizable(0, 0)
window.configure(bg='pink')

# title, heading, logo
background_image = PhotoImage(file='inventory.png')
titleLabel = Label(window, image=background_image, compound=LEFT, text='  Inventory Management System  ',
                   font=('times new roman', 40, 'bold'), bg='#FFFFF0', fg='black', anchor='w', padx=20)
titleLabel.place(x=0, y=0, relwidth=1)

# logout button
logoutButton = Button(window, text='LOGOUT', font=('times new roman', 20, 'bold'), bg='#F1F9EC', fg='black')
logoutButton.place(x=1100, y=10)

# subtitle

subtitleLabel = Label(window, font=('times new roman', 15),
                      bg='#F5FFFA', fg='black', text='Welcome, admin! \t\t Date: 04/21/2026\t\t Time: 10:32 PM')
subtitleLabel.place(x=0, y=70, relwidth=1)

# leftframe

leftFrame = Frame(window)
leftFrame.place(x=0, y=102, width=200, height=435)

# logo in menu
logoImage = PhotoImage(file='logo.png')
imageLabel = Label(leftFrame, image=logoImage)
imageLabel.pack()

# menu label
menuLabel = Label(leftFrame, text='MENU', font=('times new roman', 20), bg='#D7C8ED')
menuLabel.pack(fill=X)

# buttons under the menu
employee_icon = PhotoImage(file='employees.png')
employeeButton = Button(leftFrame, image=employee_icon, compound=LEFT, text=' EMPLOYEE',
                        font=('times new roman', 18, 'bold'), anchor='w', command=lambda: employee_form(window))
employeeButton.pack(fill=X)

supplier_icon = PhotoImage(file='supplier.png')
supplier_Button = Button(leftFrame, image=supplier_icon, compound=LEFT, text=' SUPPLIER',
                         font=('times new roman', 18, 'bold'), anchor='w')
supplier_Button.pack(fill=X)

category_icon = PhotoImage(file='category.png')
category_Button = Button(leftFrame, image=category_icon, compound=LEFT, text=' CATEGORY',
                         font=('times new roman', 18, 'bold'), anchor='w')
category_Button.pack(fill=X)

product_icon = PhotoImage(file='product.png')
product_Button = Button(leftFrame, image=product_icon, compound=LEFT, text=' PRODUCT',
                        font=('times new roman', 18, 'bold'), anchor='w')
product_Button.pack(fill=X)

sales_icon = PhotoImage(file='sales.png')
sales_Button = Button(leftFrame, image=sales_icon, compound=LEFT, text=' SALES', font=('times new roman', 18, 'bold'),
                      anchor='w')
sales_Button.pack(fill=X)

exit_icon = PhotoImage(file='exit.png')
exit_Button = Button(leftFrame, image=exit_icon, compound=LEFT, text=' EXIT', font=('times new roman', 18, 'bold'),
                     anchor='w')
exit_Button.pack(fill=X)

# total employee count
emp_frame = Frame(window, bg='#F8E57D', bd=3, relief=RIDGE)
emp_frame.place(x=400, y=125, height=170, width=280)
totalEmp_icon = PhotoImage(file='totalEmp.png')

totalEmp_icon_label = Label(emp_frame, image=totalEmp_icon, bg='#F8E57D')
totalEmp_icon_label.pack()

totalEmp_icon_label = Label(emp_frame, text='TOTAL EMPLOYEES', bg='#F8E57D', fg='black',
                            font=('times new roman', 15, 'bold'))
totalEmp_icon_label.pack()

totalEmp_count_label = Label(emp_frame, text='0', bg='#F8E57D', fg='black', font=('times new roman', 30, 'bold'))
totalEmp_count_label.pack()

# total suppliers count
supplier_frame = Frame(window, bg='#bca89f', bd=3, relief=RIDGE)
supplier_frame.place(x=800, y=125, height=170, width=280)
totalSupplier_icon = PhotoImage(file='totalSupplier.png')
totalSupplier_icon_label = Label(supplier_frame, image=totalSupplier_icon, bg='#bca89f')
totalSupplier_icon_label.pack()
totalSupplier_icon_label = Label(supplier_frame, text='TOTAL SUPPLIERS', bg='#bca89f', fg='black',
                                 font=('times new roman', 15, 'bold'))
totalSupplier_icon_label.pack()

totalSupplier_count_label = Label(supplier_frame, text='0', bg='#bca89f', fg='black',
                                  font=('times new roman', 30, 'bold'))
totalSupplier_count_label.pack()

# total category
category_frame = Frame(window, bg='#9DC183', bd=3, relief=RIDGE)
category_frame.place(x=400, y=310, height=180, width=280)
totalCategory_icon = PhotoImage(file='totalCat.png')
totalCategory_icon_label = Label(category_frame, image=totalCategory_icon, bg='#9DC183')
totalCategory_icon_label.pack()
totalCategory_icon_label = Label(category_frame, text='TOTAL CATEGORIES', bg='#9DC183', fg='black',
                                 font=('times new roman', 15, 'bold'))
totalCategory_icon_label.pack()

totalCategory_count_label = Label(category_frame, text='0', bg='#9DC183', fg='black',
                                  font=('times new roman', 30, 'bold'))
totalCategory_count_label.pack()

# total products
product_frame = Frame(window, bg='#BDE1CC', bd=3, relief=RIDGE)
product_frame.place(x=800, y=310, height=180, width=280)
totalProduct_icon = PhotoImage(file='totalProd.png')
totalProduct_icon_label = Label(product_frame, image=totalProduct_icon, bg='#BDE1CC')
totalProduct_icon_label.pack()
totalProduct_icon_label = Label(product_frame, text='TOTAL PRODUCTS', bg='#BDE1CC', fg='black',
                                font=('times new roman', 15, 'bold'))
totalProduct_icon_label.pack()

totalProduct_count_label = Label(product_frame, text='0', bg='#BDE1CC', fg='black',
                                 font=('times new roman', 30, 'bold'))
totalProduct_count_label.pack()

# total sales
sales_frame = Frame(window, bg='#EBF3EE', bd=3, relief=RIDGE)
sales_frame.place(x=600, y=495, height=180, width=280)
totalSales_icon = PhotoImage(file='totalSales.png')
totalSales_icon_label = Label(sales_frame, image=totalSales_icon, bg='#EBF3EE')
totalSales_icon_label.pack()
totalSales_icon_label = Label(sales_frame, text='TOTAL SALES', bg='#EBF3EE', fg='black',
                              font=('times new roman', 15, 'bold'))
totalSales_icon_label.pack()

totalSales_count_label = Label(sales_frame, text='0', bg='#EBF3EE', fg='black', font=('times new roman', 30, 'bold'))
totalSales_count_label.pack()

window.mainloop()
