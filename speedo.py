import tkinter as tk
from datetime import datetime
import random

# Create the main window
root = tk.Tk()
root.title("Electric Bike Dashboard")
root.geometry("800x600")
#root.configure(bg='black')

# Load background image
bg_image = tk.PhotoImage(file="photo.png")  # Change the filename if needed

# Create the Canvas
canvas = tk.Canvas(root, width=800, height=600, bg='black', highlightthickness=0)
canvas.pack()

# Set the background image
canvas.create_image(0, 0, anchor='nw', image=bg_image)

# Function to update time
def update_time():
    current_time.set(datetime.now().strftime('%H:%M'))
    canvas.itemconfig(current_time_text, text=current_time.get())
    root.after(1000, update_time)

# Function to simulate data updates
def update_data():
    speed.set(random.randint(0, 100))
    battery_range.set(f"{random.randint(0, 300)} km")
    total_kilometers.set(f"{random.randint(0, 10000)} km")
    charge_input.set(f"{random.uniform(0, 12):.2f} A")
    battery_status.set(random.choice(["Charging", "Discharging", "Low"]))
    battery_charge.set(f"{random.randint(0, 100)}%")
    canvas.itemconfig(speed_text, text=speed.get())
    canvas.itemconfig(battery_range_text, text=battery_range.get())
    canvas.itemconfig(total_kilometers_text, text=total_kilometers.get())
    canvas.itemconfig(charge_input_text, text=charge_input.get())
    canvas.itemconfig(battery_status_text, text=battery_status.get())
    canvas.itemconfig(battery_charge_text, text=battery_charge.get())
    root.after(5000, update_data)

# Define StringVar for dynamic data
current_time = tk.StringVar()
speed = tk.IntVar()
battery_range = tk.StringVar()
total_kilometers = tk.StringVar()
charge_input = tk.StringVar()
battery_status = tk.StringVar()
battery_charge = tk.StringVar()

# Create and place labels and widgets
# Digital Speed Display
speed_text = canvas.create_text(600, 200, text="", font=("Montserrat", 90), fill="white")

# Battery Range
battery_range_text = canvas.create_text(300, 225, text="", font=("Montserrat", 30), fill="white", anchor="w")

# Total Kilometers
total_kilometers_text = canvas.create_text(150, 310, text="", font=("Montserrat", 30), fill="white", anchor="w")

# Charge Input
charge_input_text = canvas.create_text(150, 380, text="", font=("Montserrat", 30), fill="white", anchor="w")

# Battery Status
battery_status_text = canvas.create_text(150, 460, text="", font=("Montserrat", 25), fill="white", anchor="w")

# Current Time
current_time_text = canvas.create_text(30, 100, text="", font=("Montserrat", 40), fill="green", anchor="w")

# Battery Charge
battery_charge_text = canvas.create_text(580, 510, text="", font=("Helvetica", 40), fill="green", anchor="w")

# Initialize time and data updates
update_time()
update_data()

# Run the application
root.mainloop()
