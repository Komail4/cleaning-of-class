import tkinter
import json
import datetime
from tkinter import ttk

x = datetime.datetime.now()

def show_frame(frame):
    frame.tkraise()

file_path = "info.json"

top = tkinter.Tk()
top.title("Class Status Manager")
top.geometry("400x500")

container = tkinter.Frame(top)
container.pack(fill="both", expand=True)

output_frame = tkinter.Frame(container)
input_info = tkinter.Frame(container)

for frame in (output_frame, input_info):
    frame.place(relwidth=1, relheight=1)

status = ["100", "75", "50", "25", "0"]
class_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]

label_class = tkinter.Label(input_info, text=":صنف")
label_class.pack(pady=5)
combo_class = ttk.Combobox(input_info, values=class_numbers, state="readonly")
combo_class.pack(pady=5)

label_window = tkinter.Label(input_info, text=":وضعیت پنجره")
label_window.pack(pady=5)
combo_window_status = ttk.Combobox(input_info, values=status, state="readonly")
combo_window_status.pack(pady=5)

label_waste_basket = tkinter.Label(input_info, text=":وضعیت سطل زباله")
label_waste_basket.pack(pady=5)
combo_waste_basket = ttk.Combobox(input_info, values=status, state="readonly")
combo_waste_basket.pack(pady=5)

label_chairs_desks = tkinter.Label(input_info, text=":وضعیت چوکی و میز")
label_chairs_desks.pack(pady=5)
combo_chairs_desks = ttk.Combobox(input_info, values=status, state="readonly")
combo_chairs_desks.pack(pady=5)

label_class_status = tkinter.Label(input_info, text=":وضعیت صنف")
label_class_status.pack(pady=5)
combo_class_status = ttk.Combobox(input_info, values=status, state="readonly")
combo_class_status.pack(pady=5)

label_lamps = tkinter.Label(input_info, text=":وضعیت چراغ")
label_lamps.pack(pady=5)
combo_lamps = ttk.Combobox(input_info, values=status, state="readonly")
combo_lamps.pack(pady=5)

label_swags = tkinter.Label(input_info, text=":وضعیت پرده")
label_swags.pack(pady=5)
combo_swags = ttk.Combobox(input_info, values=status, state="readonly")
combo_swags.pack(pady=5)

result_label = tkinter.Label(input_info, text="سلام")
result_label.pack(pady=10)

def submit(*status):
    if "" in status:
        result_label.config(text="لطفا همه فیلدها را پر کنید")
        return
    with open(file_path, "r") as file:
        data = json.load(file)

    calculated_status = (int(status[1]) + int(status[2]) + int(status[3]) + int(status[4]) + int(status[5]) + int(status[6])) / 6

    data[status[0]][x.strftime("%Y-%m-%d")] = {"result": calculated_status,"window" : status[1], "waste_basket" : status[2], "chairs_desks" : status[3], "class_status" : status[4], "lamps" : status[5], "swags" : status[6]}

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
    result_label.config(text=f"Class {status[0]} - Status: {calculated_status}%\nWindow: {status[1]}\nWaste Basket: {status[2]}\nChairs/Desks: {status[3]}\nClass Status: {status[4]}\nLamps: {status[5]}\nSwags: {status[6]}")

    

button_submit = tkinter.Button(input_info, text="ثبت", command=lambda: submit(
    combo_class.get(),
    combo_window_status.get(),
    combo_waste_basket.get(),
    combo_chairs_desks.get(),
    combo_class_status.get(),
    combo_lamps.get(),
    combo_swags.get()
))
button_submit.pack(pady=10)

menu_bar = tkinter.Menu(top)

main_menu = tkinter.Menu(menu_bar, tearoff=0)
main_menu.add_command(label="Main Menu", command=lambda: show_frame(output_frame))
main_menu.add_separator()
main_menu.add_command(label="Entering info", command=lambda: show_frame(input_info))
menu_bar.add_cascade(label="Menu", menu=main_menu)

top.config(menu=menu_bar)

show_frame(input_info)

top.mainloop()