import tkinter
import json
import jdatetime
from tkinter import ttk
from tkinter import messagebox

x = jdatetime.datetime.now()

def show_frame(frame):
    frame.tkraise()

file_path = "info.json"

top = tkinter.Tk()
top.title("Class Status Manager")
top.geometry("400x600")

container = tkinter.Frame(top)
container.pack(fill="both", expand=True)

input_info = tkinter.Frame(container)
output_daily = tkinter.Frame(container)
output_weekly = tkinter.Frame(container)
output_monthly = tkinter.Frame(container)
output_total = tkinter.Frame(container)

for frame in (input_info, output_daily, output_weekly, output_monthly, output_total):
    frame.place(relwidth=1, relheight=1)

status = ["100", "75", "50", "25", "0"]
class_numbers = ["1", "1b", "2", "2b", "3", "3b", "4", "4b", "5", "5b", "6", "6b", "7", "8", "9", "10", "11"]

label_class = tkinter.Label(input_info, text=":صنف")
label_class.pack(pady=5)
combo_class = ttk.Combobox(input_info, values=class_numbers, state="readonly")
combo_class.pack(pady=5)

label_date_entry = tkinter.Label(input_info, text = ":تاریخ")
label_date_entry.pack(pady=5)

years_1 = [str(y) for y in range(1400, 1410)]
combo_year_entry = ttk.Combobox(input_info, values=years_1, state="readonly")
combo_year_entry.set(x.strftime("%Y"))
combo_year_entry.pack(pady=2)

months_1 = [str(m) for m in range(1, 13)]
combo_month_entry = ttk.Combobox(input_info, values=months_1, state="readonly")
combo_month_entry.set(x.strftime("%m"))
combo_month_entry.pack(pady=2)

days_1 = [str(d) for d in range(1, 32)]
combo_day_entry = ttk.Combobox(input_info, values=days_1, state="readonly")
combo_day_entry.set(x.strftime("%d"))
combo_day_entry.pack(pady=2)

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

def submit(*status):
    if "" in status:
        messagebox.showwarning("Warning", "لطفا همه فیلدها را پر کنید")
        return
    
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning("Warning", "فایل اطلاعات پیدا نشد")
    
    calculated_status = (int(status[1]) + int(status[2]) + int(status[3]) + int(status[4]) + int(status[5]) + int(status[6])) / 6
    
    date_str = jdatetime.date(int(status[7]), int(status[8]), int(status[9])).strftime("%Y-%m-%d")
    
    if status[0] not in data:
        data[status[0]] = {}
    
    data[status[0]][date_str] = {
        "result": calculated_status,
        "window": status[1],
        "waste_basket": status[2],
        "chairs_desks": status[3],
        "class_status": status[4],
        "lamps": status[5],
        "swags": status[6]
    }

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
    
    messagebox.showinfo("Success", f"'اطلاعات با موفقیت ذخیره شد'\nDate: {date_str}\nClass {status[0]} - Status: {calculated_status}%\nWindow: {status[1]}\nWaste Basket: {status[2]}\nChairs/Desks: {status[3]}\nClass Status: {status[4]}\nLamps: {status[5]}\nSwags: {status[6]}")

button_submit = tkinter.Button(input_info, text="ثبت", command=lambda: submit(
    combo_class.get(),
    combo_window_status.get(),
    combo_waste_basket.get(),
    combo_chairs_desks.get(),
    combo_class_status.get(),
    combo_lamps.get(),
    combo_swags.get(),
    combo_year_entry.get(),
    combo_month_entry.get(),
    combo_day_entry.get()
))
button_submit.pack(pady=10)

label_class_daily = tkinter.Label(output_daily, text=":صنف")
label_class_daily.pack(pady=5)
combo_class_daily = ttk.Combobox(output_daily, values=class_numbers, state="readonly")
combo_class_daily.pack(pady=5)
label_date_daily = tkinter.Label(output_daily, text=":تاریخ")
label_date_daily.pack(pady=5)

years = [str(y) for y in range(1400, 1410)]
combo_year_daily = ttk.Combobox(output_daily, values=years, state="readonly")
combo_year_daily.set("1403")
combo_year_daily.pack(pady=5)

months = [str(m) for m in range(1, 13)]
combo_month_daily = ttk.Combobox(output_daily, values=months, state="readonly")
combo_month_daily.set("1")
combo_month_daily.pack(pady=5)

days = [str(d) for d in range(1, 32)]
combo_day_daily = ttk.Combobox(output_daily, values=days, state="readonly")
combo_day_daily.set("1")
combo_day_daily.pack(pady=5)

def daily_output(class_1, selected_year, selected_month, selected_day):
    if not class_1:
        messagebox.showwarning("Warning", "لطفا صنف را انتخاب کنید")
    if not (selected_year and selected_month and selected_day):
        messagebox.showwarning("Warning", "لطفا تاریخ را انتخاب کنید")
        return
    
    date = jdatetime.date(int(selected_year), int(selected_month), int(selected_day))
    date_str = date.strftime("%Y-%m-%d")

    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning("Warning", "فایل اطلاعات پیدا نشد")
        return
    
    if date_str not in data[class_1]:
        messagebox.showwarning("Warning", "اطلاعات پیدا نشد")
        return
    
    output = data[class_1][date_str]["result"]
    messagebox.showinfo("Result", f"{date_str}\nClass{class_1} - Status: {output}")

button_submit_daily = tkinter.Button(output_daily, text="تایید", command=lambda:daily_output(
    combo_class_daily.get(),
    combo_year_daily.get(),
    combo_month_daily.get(),
    combo_day_daily.get()))
button_submit_daily.pack(pady=10)

label_class_weekly = tkinter.Label(output_weekly, text=":صنف")
label_class_weekly.pack(pady=5)
combo_class_weekly = ttk.Combobox(output_weekly, values=class_numbers, state="readonly")
combo_class_weekly.pack(pady=5)
label_date_weekly = tkinter.Label(output_weekly, text = ":تاریخ")
label_date_weekly.pack(pady=5)


def generate_weeks(year):
    weeks = []
    
    first_day = jdatetime.date(year, 1, 1)
    first_saturday = first_day + jdatetime.timedelta(days=(6 - first_day.weekday() + 1) % 7)
    
    start_date = first_saturday
    week_num = 1
    
    while start_date.year == year:  # Stay within the year
        end_date = start_date + jdatetime.timedelta(days=5)  # Thursday of the same week

        week_label = f"{week_num} {start_date.strftime('%Y-%m-%d')} ---- {end_date.strftime('%Y-%m-%d')}"
        weeks.append(week_label)

        # Move to next week (skip Friday)
        start_date = end_date + jdatetime.timedelta(days=2)  
        week_num += 1

    return weeks

# Generate weeks for the selected year
current_year = 1404
week_options = generate_weeks(current_year)

# Create the combo box for week selection
combo_weeks = ttk.Combobox(output_weekly, values=week_options, state="readonly", width=30)
combo_weeks.pack(pady=5)

def weekly_output(class_1, selected_week):
    if not selected_week:
        messagebox.showwarning("Warning", "لطفا هفته مورد نظر را انتخاب کنید")
        return
    if not class_1:
        messagebox.showwarning("Warning", "لطفا یک صنف را انتخاب کنید")
        return

    week_parts = selected_week.split()
    start_date = jdatetime.datetime.strptime(week_parts[1], "%Y-%m-%d").date()
    end_date = jdatetime.datetime.strptime(week_parts[3], "%Y-%m-%d").date()

    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning("Warning", "فایل اطلاعات پیدا نشد")
        return
    
    weekly_results = []
    for i in range(6):  # Loop from Saturday to Thursday
        current_date = start_date + jdatetime.timedelta(days=i)
        date_str = current_date.strftime("%Y-%m-%d")
        
        if class_1 in data and date_str in data[class_1]:  
            weekly_results.append(data[class_1][date_str]["result"])

    if not weekly_results:
        messagebox.showinfo("Weekly Report", "هیچ اطلاعاتی برای این هفته موجود نیست")
        return
    
    weekly_average = sum(weekly_results) / len(weekly_results)
    messagebox.showinfo("Weekly Report", f"Class {class_1} - Weekly Status: {weekly_average:.2f}%")



button_submit_weekly = tkinter.Button(output_weekly, text="تایید", command=lambda: weekly_output(
    combo_class_weekly.get(), combo_weeks.get()))
button_submit_weekly.pack(pady=10)

label_class_monthly = tkinter.Label(output_monthly, text = ":صنف")
label_class_monthly.pack(pady = 5)
combo_class_monthly = ttk.Combobox(output_monthly, values=class_numbers, state = "readonly")
combo_class_monthly.pack(pady = 5)
label_date_monthly = tkinter.Label(output_monthly, text = ":ماه")
label_date_monthly.pack(pady=5)

combo_year_monthly = ttk.Combobox(output_monthly, values=years, state="readonly")
combo_year_monthly.set("1404")
combo_year_monthly.pack(pady=5)

months = [str(m) for m in range(1, 13)]
combo_month_monthly = ttk.Combobox(output_monthly, values=months, state="readonly")
combo_month_monthly.set("1")
combo_month_monthly.pack(pady=5)

def monthly_output(class_1, year, month):
    if not (year and month):
        messagebox.showwarning("Warning", "لطفا سال و ماه را انتخاب کنید")
        return
    
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning("Warning", "فایل اطلاعات پیدا نشد")
        return
    
    monthly_results = []
    
    for day in range(1, 32):  # Checking all possible days
        try:
            date = jdatetime.date(int(year), int(month), day)
            date_str = date.strftime("%Y-%m-%d")

            if class_1 in data and date_str in data[class_1]:
                monthly_results.append(data[class_1][date_str]["result"])
        except ValueError:
            break  # Break when the month has fewer than 31 days

    if not monthly_results:
        messagebox.showinfo("Monthly Report", "هیچ اطلاعاتی برای این ماه موجود نیست")
        return

    monthly_average = sum(monthly_results) / len(monthly_results)
    messagebox.showinfo("Monthly Report", f"Class {class_1} - Monthly Status: {monthly_average:.2f}%")

    pass



button_submit_monthly = tkinter.Button(output_monthly, text="تایید", command=lambda: monthly_output(
    combo_class_monthly.get(),
    combo_year_monthly.get(),
    combo_month_monthly.get()))
button_submit_monthly.pack(pady=5)





label_class_total = tkinter.Label(output_total, text=":صنف")
label_class_total.pack(pady=5)

combo_class_total = ttk.Combobox(output_total, values=class_numbers, state="readonly")
combo_class_total.pack(pady=5)

def total_output(class_1):
    if not class_1:
        messagebox.showwarning("Warning", "لطفا صنف را انتخاب کنید")
        return
    
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning("Warning", "فایل اطلاعات پیدا نشد")
        return
    
    if class_1 not in data or not data[class_1]:
        messagebox.showinfo("Total Report", "هیچ اطلاعاتی برای این صنف موجود نیست")
        return
    
    total_results = []
    
    for date_str in data[class_1]:
        total_results.append(data[class_1][date_str]["result"])

    if not total_results:
        messagebox.showinfo("Total Report", "هیچ اطلاعاتی برای این صنف موجود نیست")
        return

    total_average = sum(total_results) / len(total_results)
    messagebox.showinfo("Total Report", f"Class {class_1} - Total Status: {total_average:.2f}%")

button_submit_total = tkinter.Button(output_total, text="تایید", command=lambda: total_output(
    combo_class_total.get()))
button_submit_total.pack(pady=5)





menu_bar = tkinter.Menu(top)

main_menu = tkinter.Menu(menu_bar, tearoff=0)
main_menu.add_command(label="Entering info", command=lambda: show_frame(input_info))
menu_bar.add_cascade(label="Menu", menu=main_menu)

result_menu = tkinter.Menu(menu_bar, tearoff=0)
result_menu.add_command(label="Daily", command=lambda: show_frame(output_daily))
result_menu.add_command(label="Weekly", command=lambda: show_frame(output_weekly))
result_menu.add_command(label="Monthly", command=lambda: show_frame(output_monthly))
result_menu.add_command(label="Total", command=lambda: show_frame(output_total))
menu_bar.add_cascade(label="Results", menu=result_menu)

top.config(menu=menu_bar)

show_frame(input_info)

top.mainloop()