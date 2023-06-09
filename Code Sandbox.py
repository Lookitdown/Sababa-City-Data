import customtkinter

def city_selection(state):
    # Function to handle city selection based on the state chosen
    cities = {
        "California": ["Los Angeles", "San Francisco", "San Diego"],
        "New York": ["New York City", "Buffalo", "Rochester"],
        "Texas": ["Houston", "Dallas", "Austin"],
        # Add more states and cities as needed
    }
    
    # Hide the state buttons
    for state_button in state:
        state_button.pack_forget()
    
    # Create buttons for each city in the selected state
    for city in cities[state]:
        city_button = ttk.Button(selection_frame, text=city, command=lambda c=city: print("Selected city:", c))
        city_button.pack(pady=5)

app = customtkinter.CTk()
app.geometry("800x300")

button1 = customtkinter.CTkButton(app, text="California", command=city_selection)
button1.pack(padx=20, pady=20)

button2 = customtkinter.CTkButton(app, text="Chicago", command=city_selection)
button2.pack(padx=20, pady=20)

button3 = customtkinter.CTkButton(app, text="Texas", command=city_selection)
button3.pack(padx=20, pady=20)

button3 = customtkinter.CTkButton(app, text="Michigan", command=city_selection)
button3.pack(padx=20, pady=20)

app.mainloop()