import sqlite3
import tkinter as tk
from tkinter import messagebox
from datetime import date

def connect_db():
    return sqlite3.connect('estoque_vendas.db')

# Funções CRUD para Vendas
def add_sale():
    conn = connect_db()
    c = conn.cursor()
    c.execute("INSERT INTO Venda (cod_cliente, cod_produto, data_venda, quantidade, meio_venda) VALUES (?, ?, ?, ?, ?)",
              (client_id_entry.get(), product_id_entry.get(), date.today(), quantity_entry.get(), sale_method_entry.get()))
    # Atualizar estoque
    update_stock_on_sale(conn, product_id_entry.get(), quantity_entry.get())
    conn.commit()
    conn.close()  # Fecha a conexão após a operação
    messagebox.showinfo("Sucesso", "Venda adicionada")
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
    messagebox.showinfo("Sucesso", "Venda atualizada com sucesso")
    display_sales()

def delete_sale():
    conn = connect_db()
    c = conn.cursor()
    c.execute("DELETE FROM Venda WHERE ID=?", (selected_sale[0],))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso", "Venda deleted com sucesso")
    display_sales()

def select_sale(event):
    global selected_sale
    if sales_list.curselection():
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
    messagebox.showinfo("Sucesso", "Ordem de produção adicionada com sucesso")
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
    messagebox.showinfo("Sucesso", "Ordem de produção atualizada com sucesso")
    display_production_orders()

def delete_production_order():
    conn = connect_db()
    c = conn.cursor()
    c.execute("DELETE FROM OrdemProducao WHERE ID=?", (selected_production_order[0],))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso", "Ordem de produção deletada com sucesso")
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
    messagebox.showinfo("Sucesso", "Entrada de estoque atualizada com sucesso")
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

def update_stock():
    conn = connect_db()
    c = conn.cursor()
    c.execute("UPDATE Estoque SET cod_produto=?, quantidade=?, operador=? WHERE ID=?",
              (stock_product_id_entry.get(), stock_quantity_entry.get(), operator_entry.get(), selected_stock[0]))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso", "Entrada de estoque atualizada com sucesso")
    display_stock()

def update_stock_on_sale(conn, product_id, quantity):
    c = conn.cursor()
    c.execute("UPDATE Produto SET quantidade = quantidade - ? WHERE id = ?", (quantity, product_id))
    conn.commit()

def delete_stock():
    conn = connect_db()
    c = conn.cursor()
    c.execute("DELETE FROM Estoque WHERE ID=?", (selected_stock[0],))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso", "Entrada de estoque deletada com sucesso")
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
tk.Label(second_frame, text="Id Cliente").pack()
client_id_entry = tk.Entry(second_frame)
client_id_entry.pack()

tk.Label(second_frame, text="ID Produto").pack()
product_id_entry = tk.Entry(second_frame)
product_id_entry.pack()

tk.Label(second_frame, text="Quantidade").pack()
quantity_entry = tk.Entry(second_frame)
quantity_entry.pack()

tk.Label(second_frame, text="Método de venda").pack()
sale_method_entry = tk.Entry(second_frame)
sale_method_entry.pack()

sales_list = tk.Listbox(second_frame, height=10, width=50)
sales_list.pack()
sales_list.bind('<<ListboxSelect>>', select_sale)

tk.Button(second_frame, text="Add Venda", command=add_sale).pack()
tk.Button(second_frame, text="Update Venda", command=update_sale).pack()
tk.Button(second_frame, text="Delete Venda", command=delete_sale).pack()

# Labels e Entradas para Ordens de Produção
tk.Label(second_frame, text="Número da semana").pack()
week_entry = tk.Entry(second_frame)
week_entry.pack()

tk.Label(second_frame, text="Status").pack()
status_entry = tk.Entry(second_frame)
status_entry.pack()

production_orders_list = tk.Listbox(second_frame, height=10, width=50)
production_orders_list.pack()
production_orders_list.bind('<<ListboxSelect>>', select_production_order)

tk.Button(second_frame, text="Add Ordem de Produção", command=add_production_order).pack()
tk.Button(second_frame, text="Update Ordem de Produção", command=update_production_order).pack()
tk.Button(second_frame, text="Delete Ordem de Produção", command=delete_production_order).pack()

# Labels e Entradas para Estoque
tk.Label(second_frame, text="ID produto").pack()
stock_product_id_entry = tk.Entry(second_frame)
stock_product_id_entry.pack()

tk.Label(second_frame, text="Quantidade").pack()
stock_quantity_entry = tk.Entry(second_frame)
stock_quantity_entry.pack()

tk.Label(second_frame, text="Operador").pack()
operator_entry = tk.Entry(second_frame)
operator_entry.pack()

stock_list = tk.Listbox(second_frame, height=10, width=50)
stock_list.pack()
stock_list.bind('<<ListboxSelect>>', select_stock)

tk.Button(second_frame, text="Add Estoque", command=add_stock).pack()
tk.Button(second_frame, text="Update Estoque", command=update_stock).pack()
tk.Button(second_frame, text="Delete Estoque", command=delete_stock).pack()

# Mostrar os dados ao iniciar a aplicação
display_sales()
display_production_orders()
display_stock()

# Executa o loop principal
root.mainloop()