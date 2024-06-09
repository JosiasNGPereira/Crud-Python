import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import date

def connect_db():
    return sqlite3.connect('estoque_vendas.db')

# Funções CRUD para Vendas
def add_sale():
    conn = connect_db()
    c = conn.cursor()
    c.execute("INSERT INTO Venda (cod_cliente, cod_produto, data_venda, quantidade, meio_venda) VALUES (?, ?, ?, ?, ?)",
              (client_id_entry.get(), product_id_entry.get(), date.today(), quantity_entry.get(), sale_method_entry.get()))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Sale added successfully")
    display_sales()

def display_sales():
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT * FROM Venda")
    rows = c.fetchall()
    sales_list.delete(0, tk.END)
    for row in rows:
        sales_list.insert(tk.END, row)
    conn.close()

def update_sale():
    conn = connect_db()
    c = conn.cursor()
    c.execute("UPDATE Venda SET cod_cliente=?, cod_produto=?, quantidade=?, meio_venda=? WHERE ID=?",
              (client_id_entry.get(), product_id_entry.get(), quantity_entry.get(), sale_method_entry.get(), selected_sale[0]))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Sale updated successfully")
    display_sales()

def delete_sale():
    conn = connect_db()
    c = conn.cursor()
    c.execute("DELETE FROM Venda WHERE ID=?", (selected_sale[0],))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Sale deleted successfully")
    display_sales()

def select_sale(event):
    global selected_sale
    index = sales_list.curselection()[0]
    selected_sale = sales_list.get(index)
    client_id_entry.delete(0, tk.END)
    client_id_entry.insert(tk.END, selected_sale[1])
    product_id_entry.delete(0, tk.END)
    product_id_entry.insert(tk.END, selected_sale[2])
    quantity_entry.delete(0, tk.END)
    quantity_entry.insert(tk.END, selected_sale[4])
    sale_method_entry.delete(0, tk.END)
    sale_method_entry.insert(tk.END, selected_sale[5])

# Funções CRUD para Ordem de Produção
def add_production_order():
    conn = connect_db()
    c = conn.cursor()
    c.execute("INSERT INTO OrdemProducao (data_criacao, semana, status) VALUES (?, ?, ?)",
              (date.today(), week_entry.get(), "Pending"))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Production order added successfully")
    display_production_orders()

def display_production_orders():
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT * FROM OrdemProducao")
    rows = c.fetchall()
    production_orders_list.delete(0, tk.END)
    for row in rows:
        production_orders_list.insert(tk.END, row)
    conn.close()

def update_production_order():
    conn = connect_db()
    c = conn.cursor()
    c.execute("UPDATE OrdemProducao SET semana=?, status=? WHERE ID=?",
              (week_entry.get(), status_entry.get(), selected_production_order[0]))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Production order updated successfully")
    display_production_orders()

def delete_production_order():
    conn = connect_db()
    c = conn.cursor()
    c.execute("DELETE FROM OrdemProducao WHERE ID=?", (selected_production_order[0],))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Production order deleted successfully")
    display_production_orders()

def select_production_order(event):
    global selected_production_order
    index = production_orders_list.curselection()[0]
    selected_production_order = production_orders_list.get(index)
    week_entry.delete(0, tk.END)
    week_entry.insert(tk.END, selected_production_order[2])
    status_entry.delete(0, tk.END)
    status_entry.insert(tk.END, selected_production_order[3])

# Funções CRUD para Estoque
def add_stock():
    conn = connect_db()
    c = conn.cursor()
    c.execute("INSERT INTO Estoque (cod_produto, data_insercao, quantidade, operador) VALUES (?, ?, ?, ?)",
              (stock_product_id_entry.get(), date.today(), stock_quantity_entry.get(), operator_entry.get()))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Stock entry added successfully")
    display_stock()

def display_stock():
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT * FROM Estoque")
    rows = c.fetchall()
    stock_list.delete(0, tk.END)
    for row in rows:
        stock_list.insert(tk.END, row)
    conn.close()

def update_stock_on_sale(product_id, quantity):
    conn = connect_db()
    c = conn.cursor()
    c.execute("UPDATE Produto SET quantidade = quantidade - ? WHERE id = ?", (quantity, product_id))
    conn.commit()
    conn.close()

def delete_stock():
    conn = connect_db()
    c = conn.cursor()
    c.execute("DELETE FROM Estoque WHERE ID=?", (selected_stock[0],))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Stock entry deleted successfully")
    display_stock()

def select_stock(event):
    global selected_stock
    index = stock_list.curselection()[0]
    selected_stock = stock_list.get(index)
    stock_product_id_entry.delete(0, tk.END)
    stock_product_id_entry.insert(tk.END, selected_stock[1])
    stock_quantity_entry.delete(0, tk.END)
    stock_quantity_entry.insert(tk.END, selected_stock[3])
    operator_entry.delete(0, tk.END)
    operator_entry.insert(tk.END, selected_stock[4])

# Interface Gráfica
root = tk.Tk()
root.title("Estoque e Vendas App")
root.geometry("700x700")

# Frame principal com canvas e scrollbar
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=1)

canvas = tk.Canvas(main_frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

second_frame = tk.Frame(canvas)
canvas.create_window((200, 0), window=second_frame, anchor="nw")

# Labels e Entradas para Vendas
tk.Label(second_frame, text="Client ID").pack()
client_id_entry = tk.Entry(second_frame)
client_id_entry.pack()

tk.Label(second_frame, text="Product ID").pack()
product_id_entry = tk.Entry(second_frame)
product_id_entry.pack()

tk.Label(second_frame, text="Quantity").pack()
quantity_entry = tk.Entry(second_frame)
quantity_entry.pack()

tk.Label(second_frame, text="Sale Method").pack()
sale_method_entry = tk.Entry(second_frame)
sale_method_entry.pack()

sales_list = tk.Listbox(second_frame, height=10, width=50)
sales_list.pack()
sales_list.bind('<<ListboxSelect>>', select_sale)

tk.Button(second_frame, text="Add Sale", command=add_sale).pack()
tk.Button(second_frame, text="Update Sale", command=update_sale).pack()
tk.Button(second_frame, text="Delete Sale", command=delete_sale).pack()

# Labels e Entradas para Ordens de Produção
tk.Label(second_frame, text="Week Number").pack()
week_entry = tk.Entry(second_frame)
week_entry.pack()

tk.Label(second_frame, text="Status").pack()
status_entry = tk.Entry(second_frame)
status_entry.pack()

production_orders_list = tk.Listbox(second_frame, height=10, width=50)
production_orders_list.pack()
production_orders_list.bind('<<ListboxSelect>>', select_production_order)

tk.Button(second_frame, text="Add Production Order", command=add_production_order).pack()
tk.Button(second_frame, text="Update Production Order", command=update_production_order).pack()
tk.Button(second_frame, text="Delete Production Order", command=delete_production_order).pack()

# Labels e Entradas para Estoque
tk.Label(second_frame, text="Product ID").pack()
stock_product_id_entry = tk.Entry(second_frame)
stock_product_id_entry.pack()

tk.Label(second_frame, text="Quantity").pack()
stock_quantity_entry = tk.Entry(second_frame)
stock_quantity_entry.pack()

tk.Label(second_frame, text="Operator").pack()
operator_entry = tk.Entry(second_frame)
operator_entry.pack()

stock_list = tk.Listbox(second_frame, height=10, width=50)
stock_list.pack()
stock_list.bind('<<ListboxSelect>>', select_stock)

tk.Button(second_frame, text="Add Stock", command=add_stock).pack()
tk.Button(second_frame, text="Delete Stock", command=delete_stock).pack()

# Mostrar os dados ao iniciar a aplicação
display_sales()
display_production_orders()
display_stock()

# Executa o loop principal
root.mainloop()
