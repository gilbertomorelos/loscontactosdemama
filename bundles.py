""" gestor de bundles para mvps"""




import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json

# Datos iniciales
servicios = [
    "Landing page",
    "Chatbot básico",
    "Posts FB/IG/TikTok",
    "Videos cortos",
    "Flyers digitales",
    "Campañas publicitarias",
    "Material impreso",
    "Tarjetas de presentación",
    "Asesoría estratégica"
]

bundles = {
    "Básico": ["Landing page", "Chatbot básico", "Posts FB/IG/TikTok", "Flyers digitales"],
    "Intermedio": ["Landing page", "Chatbot básico", "Posts FB/IG/TikTok", "Videos cortos", "Flyers digitales", "Campañas publicitarias"],
    "Avanzado": ["Landing page", "Chatbot básico", "Posts FB/IG/TikTok", "Videos cortos", "Flyers digitales", "Campañas publicitarias", "Material impreso", "Tarjetas de presentación", "Asesoría estratégica"]
}

# Guardar la configuración a JSON
def guardar_json():
    data = {"servicios": servicios, "bundles": bundles}
    with open("bundles.json", "w") as f:
        json.dump(data, f, indent=4)
    messagebox.showinfo("Guardado", "Configuración guardada en bundles.json")

# Cargar la configuración desde JSON
def cargar_json():
    global servicios, bundles
    try:
        with open("bundles.json", "r") as f:
            data = json.load(f)
            servicios = data.get("servicios", [])
            bundles = data.get("bundles", {})
        construir_tabla()
        messagebox.showinfo("Cargado", "Configuración cargada desde bundles.json")
    except FileNotFoundError:
        messagebox.showwarning("Error", "No se encontró bundles.json")

# Reconstruir la tabla
def construir_tabla():
    for widget in frame_tabla.winfo_children():
        widget.destroy()

    # Encabezados
    tk.Label(frame_tabla, text="Servicio", font=("Arial", 12, "bold"), borderwidth=1, relief="solid", width=30).grid(row=0, column=0)
    for i, plan in enumerate(bundles.keys()):
        tk.Label(frame_tabla, text=plan, font=("Arial", 12, "bold"), borderwidth=1, relief="solid", width=20).grid(row=0, column=i+1)

    # Filas de servicios
    for r, servicio in enumerate(servicios):
        tk.Label(frame_tabla, text=servicio, borderwidth=1, relief="solid", width=30, anchor="w").grid(row=r+1, column=0, sticky="w")
        for c, plan in enumerate(bundles.keys()):
            incluido = servicio in bundles[plan]
            var = tk.IntVar(value=1 if incluido else 0)
            chk = tk.Checkbutton(frame_tabla, variable=var, command=lambda s=servicio, p=plan, v=var: actualizar_servicio(s, p, v))
            chk.grid(row=r+1, column=c+1)

# Actualizar inclusión de servicio en plan
def actualizar_servicio(servicio, plan, var):
    if var.get() == 1:
        if servicio not in bundles[plan]:
            bundles[plan].append(servicio)
    else:
        if servicio in bundles[plan]:
            bundles[plan].remove(servicio)

# Agregar nuevo servicio
def agregar_servicio():
    nuevo = entry_servicio.get().strip()
    if nuevo and nuevo not in servicios:
        servicios.append(nuevo)
        entry_servicio.delete(0, tk.END)
        construir_tabla()
    else:
        messagebox.showwarning("Aviso", "El servicio ya existe o está vacío")

# Eliminar servicio
def eliminar_servicio():
    servicio = simpledialog.askstring("Eliminar servicio", "Nombre del servicio a eliminar:")
    if servicio in servicios:
        servicios.remove(servicio)
        for plan_services in bundles.values():
            if servicio in plan_services:
                plan_services.remove(servicio)
        construir_tabla()
    else:
        messagebox.showwarning("Aviso", "El servicio no existe")

# Agregar nuevo plan
def agregar_plan():
    plan = simpledialog.askstring("Agregar plan", "Nombre del nuevo plan:")
    if plan and plan not in bundles:
        bundles[plan] = []
        construir_tabla()
    else:
        messagebox.showwarning("Aviso", "El plan ya existe o está vacío")

# Eliminar plan
def eliminar_plan():
    plan = simpledialog.askstring("Eliminar plan", "Nombre del plan a eliminar:")
    if plan in bundles:
        del bundles[plan]
        construir_tabla()
    else:
        messagebox.showwarning("Aviso", "El plan no existe")

# Ventana principal
root = tk.Tk()
root.title("Administrador de Bundles Avanzado")
root.geometry("1000x600")

# Frame de tabla
frame_tabla = tk.Frame(root)
frame_tabla.pack(fill="both", expand=True, padx=10, pady=10)

# Frame de controles
frame_controles = tk.Frame(root)
frame_controles.pack(pady=5)

tk.Label(frame_controles, text="Nuevo servicio:").pack(side="left")
entry_servicio = tk.Entry(frame_controles)
entry_servicio.pack(side="left", padx=5)
tk.Button(frame_controles, text="Agregar servicio", command=agregar_servicio).pack(side="left", padx=5)
tk.Button(frame_controles, text="Eliminar servicio", command=eliminar_servicio).pack(side="left", padx=5)
tk.Button(frame_controles, text="Agregar plan", command=agregar_plan).pack(side="left", padx=5)
tk.Button(frame_controles, text="Eliminar plan", command=eliminar_plan).pack(side="left", padx=5)
tk.Button(frame_controles, text="Guardar JSON", command=guardar_json).pack(side="left", padx=5)
tk.Button(frame_controles, text="Cargar JSON", command=cargar_json).pack(side="left", padx=5)

# Construir tabla inicial
construir_tabla()

root.mainloop()

