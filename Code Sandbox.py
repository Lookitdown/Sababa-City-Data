import sqlite3
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle


def city_selection(state):
    # Function to handle city selection based on the state chosen
    cities = {
        "Alabama": ["Birmingham", "Montgomery", "Mobile"],
    "Alaska": ["Anchorage", "Fairbanks", "Juneau"],
    "Arizona": ["Phoenix", "Tucson", "Mesa"],
    "Arkansas": ["Little Rock", "Fort Smith", "Fayetteville"],
    "California": ["Los Angeles", "San Francisco", "San Diego"],
    "Colorado": ["Denver", "Colorado Springs", "Aurora"],
    "Connecticut": ["Bridgeport", "New Haven", "Stamford"],
    "Delaware": ["Wilmington", "Dover", "Newark"],
    "Florida": ["Miami", "Orlando", "Tampa"],
    "Georgia": ["Atlanta", "Augusta", "Savannah"],
    "Hawaii": ["Honolulu", "Pearl City", "Hilo"],
    "Idaho": ["Boise", "Nampa", "Meridian"],
    "Illinois": ["Chicago", "Aurora", "Rockford"],
    "Indiana": ["Indianapolis", "Fort Wayne", "Evansville"],
    "Iowa": ["Des Moines", "Cedar Rapids", "Davenport"],
    "Kansas": ["Wichita", "Overland Park", "Kansas City"],
    "Kentucky": ["Louisville", "Lexington", "Bowling Green"],
    "Louisiana": ["New Orleans", "Baton Rouge", "Shreveport"],
    "Maine": ["Portland", "Lewiston", "Bangor"],
    "Maryland": ["Baltimore", "Columbia", "Germantown"],
    "Massachusetts": ["Boston", "Worcester", "Springfield"],
    "Michigan": ["Detroit", "Grand Rapids", "Warren"],
    "Minnesota": ["Minneapolis", "Saint Paul", "Rochester"],
    "Mississippi": ["Jackson", "Gulfport", "Southaven"],
    "Missouri": ["Kansas City", "Saint Louis", "Springfield"],
    "Montana": ["Billings", "Missoula", "Great Falls"],
    "Nebraska": ["Omaha", "Lincoln", "Bellevue"],
    "Nevada": ["Las Vegas", "Henderson", "Reno"],
    "New Hampshire": ["Manchester", "Nashua", "Concord"],
    "New Jersey": ["Newark", "Jersey City", "Paterson"],
    "New Mexico": ["Albuquerque", "Las Cruces", "Rio Rancho"],
    "New York": ["New York City", "Buffalo", "Rochester"],
    "North Carolina": ["Charlotte", "Raleigh", "Greensboro"],
    "North Dakota": ["Fargo", "Bismarck", "Grand Forks"],
    "Ohio": ["Columbus", "Cleveland", "Cincinnati"],
    "Oklahoma": ["Oklahoma City", "Tulsa", "Norman"],
    "Oregon": ["Portland", "Salem", "Eugene"],
    "Pennsylvania": ["Philadelphia", "Pittsburgh", "Allentown"],
    "Rhode Island": ["Providence", "Warwick", "Cranston"],
    "South Carolina": ["Columbia", "Charleston", "North Charleston"],
    "South Dakota": ["Sioux Falls", "Rapid City", "Aberdeen"],
    "Tennessee": ["Nashville", "Memphis", "Knoxville"],
    "Texas": ["Houston", "Dallas", "Austin"],
    "Utah": ["Salt Lake City", "West Valley City", "Provo"],
    "Vermont": ["Burlington", "Essex", "South Burlington"],
    "Virginia": ["Virginia Beach", "Norfolk", "Chesapeake"],
    "Washington": ["Seattle", "Spokane", "Tacoma"],
    "West Virginia": ["Charleston", "Huntington", "Morgantown"],
    "Wisconsin": ["Milwaukee", "Madison", "Green Bay"],
    "Wyoming": ["Cheyenne", "Casper", "Laramie"]
        # ... rest of the cities
    }

    # Hide the state buttons
    for state_button in state_buttons:
        state_button.grid_forget()

    # Create buttons for each city in the selected state
    for city in cities[state]:
        city_button = ttk.Button(selection_frame, text=city, command=lambda c=city: store_city(c))
        city_button.grid(row=(cities[state].index(city) // 3) + 2, column=cities[state].index(city) % 3, pady=5, padx=5)


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
state_label.grid(row=0, column=0, columnspan=3, pady=10)

# Create buttons for each state in America
states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
    "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
    "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
    "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
    "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma",
    "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee",
    "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

state_buttons = []
for index, state in enumerate(states):
    state_button = ttk.Button(selection_frame, text=state, command=lambda s=state: city_selection(s))
    state_button.grid(row=(index // 5) + 1, column=index % 5, pady=5, padx=5)
    state_buttons.append(state_button)

# Set the theme using ThemedStyle
style = ThemedStyle(root)
style.theme_use("clam")  # Apply the 'clam' theme

# Customize the style if needed
style.configure("TButton", padding=10, font=("Arial", 12))

# Start the GUI event loop
root.mainloop()
