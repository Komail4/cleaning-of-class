import customtkinter as ctk
import datetime
import json

top = ctk.CTk()
top.title("Class Status Manager")
top.geometry("400x300")

status = ["100", "75", "50", "25", "0"]
class_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]

label_class = ctk.CTkLabel(top, text=":صنف")
label_class.pack(pady=5)

combo_class = ctk.CTkComboBox(top, values=class_numbers)
combo_class.pack(pady=5)

label_window = ctk.CTkLabel(top, text=":پنجره")
label_window.pack(pady=5)

combo_window_status = ctk.CTkComboBox(top, values=status)
combo_window_status.pack(pady=5)

label_waste_basket = ctk.CTkLabel(top, text = "آشغال سطل")
label_waste_basket.pack(pady = 5)

result_label = ctk.CTkLabel(top, text="")
result_label.pack(pady=10)

# Function to display selected values
def submit():
    selected_class = combo_class.get()
    selected_status = combo_window_status.get()
    result_label.configure(text=f"Class {selected_class} - Chairs: {selected_status}%")

# Submit Button
submit_button = ctk.CTkButton(top, text="Submit", command=submit)
submit_button.pack(pady=10)

# Run the top
top.mainloop()