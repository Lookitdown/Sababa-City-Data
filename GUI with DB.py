import sqlite3
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

def city_selection(state):
    # Function to handle city selection based on the state chosen
    cities = {
        "California": ["Los Angeles", "San Francisco", "San Diego"],
        "New York": ["New York City", "Buffalo", "Rochester"],
        "Texas": ["Houston", "Dallas", "Austin"],
        # Add more states and cities as needed
    }
    
    # Hide the state buttons
    for state_button in state_buttons:
        state_button.pack_forget()
    
    # Create buttons for each city in the selected state
    for city in cities[state]:
        city_button = ttk.Button(selection_frame, text=city, command=lambda c=city: store_city(c))
        city_button.pack(pady=5)

def store_city(city):
    # Function to store the selected city in a SQLite database
    conn = sqlite3.connect("cities.db")  # Connect to the database
    cursor = conn.cursor()
    
    # Create a table if it doesn't exist
    cursor.execute("CREATE TABLE IF NOT EXISTS selected_cities (city TEXT)")
    
    # Insert the selected city into the table
    cursor.execute("INSERT INTO selected_cities VALUES (?)", (city,))
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
    print("Selected city:", city)

# Create the main window
root = tk.Tk()

# Set the window title
root.title("State and City Selection")

# Create a frame to hold the state and city selection buttons
selection_frame = ttk.Frame(root)
selection_frame.pack()

# Create a label for state selection
state_label = ttk.Label(selection_frame, text="Select your state:", font=("Helvetica", 14, "bold"))
state_label.pack(pady=10)

# Create buttons for each state in America
states = ["California", "New York", "Texas"]  # Add more states as needed
state_buttons = []
for state in states:
    state_button = ttk.Button(selection_frame, text=state, command=lambda s=state: city_selection(s))
    state_button.pack(pady=5)
    state_buttons.append(state_button)

# Set the theme using ThemedStyle
style = ThemedStyle(root)
style.set_theme("vista")  # Apply the 'vista' theme

# Start the GUI event loop
root.mainloop()