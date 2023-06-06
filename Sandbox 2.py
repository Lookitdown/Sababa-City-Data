import customtkinter

def button_callback():
    print("button clicked")

app = customtkinter.CTk()
app.geometry("400x150")

button1 = customtkinter.CTkButton(app, text="my button", command=button_callback)
button1.pack(padx=20, pady=20)

button2 = customtkinter.CTkButton(app, text="my button", command=button_callback)
button2.pack(padx=20, pady=20)

button3 = customtkinter.CTkButton(app, text="my button", command=button_callback)
button3.pack(padx=20, pady=20)

app.mainloop()