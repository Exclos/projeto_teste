import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Sistema Teste")
app.geometry("400x200")
app.resizable(False, False)

label = ctk.CTkLabel(
    app,
    text="Bem vindo ao sistema teste",
    font=("Arial", 20, "bold"),
    padx=20,
    pady=20,
)
label.pack(expand=True)

app.mainloop()
