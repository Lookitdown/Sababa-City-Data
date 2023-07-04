import customtkinter

def button_callback():
    print("button clicked")

app = customtkinter.CTk()
app.geometry("800x300")

button1 = customtkinter.CTkButton(app, text="California", command=button_callback)
button1.pack(padx=20, pady=20)

button2 = customtkinter.CTkButton(app, text="Chicago", command=button_callback)
button2.pack(padx=20, pady=20)

button3 = customtkinter.CTkButton(app, text="Texas", command=button_callback)
button3.pack(padx=20, pady=20)

button3 = customtkinter.CTkButton(app, text="Michigan", command=button_callback)
button3.pack(padx=20, pady=20)

app.mainloop()
