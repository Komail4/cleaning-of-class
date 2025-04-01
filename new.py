import customtkinter as ctk
from PIL import Image, ImageTk
import json
import tkinter as tk

def show_frame(frame):
    frame.tkraise()

ctk.set_topearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

top = ctk.CTk()
top.geometry("1280x720")
top.title("معلومات شاگردان ویرا")

container = ctk.CTkFrame(top)
container.pack(fill="both", expand=True)

output_frame = ctk.CTkFrame(container)
input_info = ctk.CTkFrame(container)
input_number = ctk.CTkFrame(container)

for frame in (output_frame, input_info, input_number):
    frame.place(relwidth=1, relheight=1)

canvas = ctk.CTkCanvas(output_frame, width=2560, height=1440)
canvas.place(x=0, y=0)

file_path = "info.json"

image = Image.open("Logo.png")
photo = ImageTk.PhotoImage(image)

image = ctk.CTkImage(light_image=Image.open("logo.png"), size = (158,111))

label = ctk.CTkLabel(top, text="", image=image)

label_id_1 = ctk.CTkLabel(input_number, text=":آی دی", width=10)
label_id_1.place(x=1190, y=30)
entry_id_1 = ctk.CTkEntry(input_number, width=20)
entry_id_1.place(x=1070, y=30)

class_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]  # Available classes
combobox_class = ctk.CTkComboBox(input_number, values=class_options, state="readonly")  
combobox_class.set("انتخاب صنف")
combobox_class.place(x=1050, y=70)



laebl_1 = ctk.CTkLabel(output_frame, text=":آی دی خود را وارد کنید", width=20, font=("B Baran", 20), fg_color="transparent").place(x=1100, y=20)
entry_1 = ctk.CTkEntry(output_frame, width=100)
entry_1.place(x=1010, y=20)

label_show_id_number = ctk.CTkLabel(output_frame, text=":آی دی نمبر", width=10).place(x=1150, y=80)
label_show_name = ctk.CTkLabel(output_frame, text=":نام", width=10).place(x=1150, y=110)
label_show_father_name = ctk.CTkLabel(output_frame, text=":نام پدر", width=10).place(x=1150, y=140)
label_show_grand_father_name = ctk.CTkLabel(output_frame, text=":نام پدر کلان", width=10).place(x=1150, y=170)
label_show_tazkera_number = ctk.CTkLabel(output_frame, text=":نمبر تذکره", width=10).place(x=1150, y=200)
label_show_date_of_birth = ctk.CTkLabel(output_frame, text=":سال تولد", width=10).place(x=1150, y=230)
label_show_year_of_entry = ctk.CTkLabel(output_frame, text=":سال ورود در مکتب", width=15).place(x=1150, y=260)
label_show_class_of_entry = ctk.CTkLabel(output_frame, text=":صنف ورود در مکتب", width=15).place(x=1150, y=290)

message_id_number = ctk.CTkLabel(output_frame, width=20)
message_id_number.place(x=1010, y=80)
message_name = ctk.CTkLabel(output_frame, width=20)
message_name.place(x=1010, y=110)
message_father_name = ctk.CTkLabel(output_frame, width=20)
message_father_name.place(x=1010, y=140)
message_grand_father_name = ctk.CTkLabel(output_frame, width=20)
message_grand_father_name.place(x=1010, y=170)
message_tazkera_number = ctk.CTkLabel(output_frame, width=20)
message_tazkera_number.place(x=1010, y=200)
message_date_of_birth = ctk.CTkLabel(output_frame, width=20)
message_date_of_birth.place(x=1010, y=230)
message_year_of_entry = ctk.CTkLabel(output_frame, width=20)
message_year_of_entry.place(x=1010, y=260)
message_class_of_entry = ctk.CTkLabel(output_frame, width=20)
message_class_of_entry.place(x=1010, y=290)

label_message_info = [(message_id_number, 1010, 80), (message_name, 1010, 110), (message_father_name, 1010, 140),
                      (message_grand_father_name, 1010, 170), (message_tazkera_number, 1010, 200), (message_date_of_birth, 1010, 230),
                      (message_year_of_entry, 1010, 260), (message_class_of_entry, 1010, 290)]

label_holy_quran = ctk.CTkLabel(output_frame, text="قرآنکریم/تفسیر", width=12)
label_islamic_education = ctk.CTkLabel(output_frame, text="عقاید/فقه/دینیات", width=12)
label_dari = ctk.CTkLabel(output_frame, text="دری", width=10)
label_pashto = ctk.CTkLabel(output_frame, text="پشتو", width=10)
label_english = ctk.CTkLabel(output_frame, text="انگلیسی", width=10)
label_math = ctk.CTkLabel(output_frame, text="ریاضی", width=10)
label_physics = ctk.CTkLabel(output_frame, text="فزیک", width=10)
label_chemistry = ctk.CTkLabel(output_frame, text="کیمیا/ساینس", width=10)
label_biology = ctk.CTkLabel(output_frame, text="بیولوژی", width=10)
label_geology = ctk.CTkLabel(output_frame, text="جیولوژی", width=10)
label_history = ctk.CTkLabel(output_frame, text="تاریخ", width=10)
label_geography = ctk.CTkLabel(output_frame, text="جغرافیه", width=10)
label_civic_education = ctk.CTkLabel(output_frame, text="تعلیمات مدنی", width=10)
label_computer = ctk.CTkLabel(output_frame, text="کمپیوتر", width=10)
label_culture = ctk.CTkLabel(output_frame, text="هنر/فرهنگ", width=10)
label_sport = ctk.CTkLabel(output_frame, text="ورزش", width=10)
label_ethics = ctk.CTkLabel(output_frame, text="تهذیب", width=10)
label_average_1 = ctk.CTkLabel(output_frame, text="اوسط نمرات", width=10)
label_total_number_1 = ctk.CTkLabel(output_frame, text="مجموع نمرات", width=10)
name1 = [(label_holy_quran, 545, 142), (label_islamic_education, 545, 167), (label_dari, 565, 192),
    (label_pashto, 565, 217), (label_english, 565, 242), (label_math, 565, 267), (label_physics, 565, 292),
    (label_chemistry, 565, 317), (label_biology, 565, 342), (label_geology, 565, 367), (label_history, 565, 392),
    (label_geography, 565, 417), (label_civic_education, 565, 442), (label_computer, 565, 467), (label_culture, 565, 492),
    (label_sport, 565, 517), (label_ethics, 565, 542), (label_average_1, 565, 592), (label_total_number_1, 565, 567)
]

for label, _, _ in name1:
    label.place_forget()

grade_1_button = ctk.CTkButton(output_frame, text="صنف اول", width=10)
grade_2_button = ctk.CTkButton(output_frame, text="صنف دوم", width=10)
grade_3_button = ctk.CTkButton(output_frame, text="صنف سوم", width=10)
grade_4_button = ctk.CTkButton(output_frame, text="صنف چهارم", width=10)
grade_5_button = ctk.CTkButton(output_frame, text="صنف پنجم", width=10)
grade_6_button = ctk.CTkButton(output_frame, text="صنف ششم", width=10)
grade_7_button = ctk.CTkButton(output_frame, text="صنف هفتم", width=10)
grade_8_button = ctk.CTkButton(output_frame, text="صنف هشتم", width=10)
grade_9_button = ctk.CTkButton(output_frame, text="صنف نهم", width=10)
grade_10_button = ctk.CTkButton(output_frame, text="صنف دهم", width=10)
grade_11_button = ctk.CTkButton(output_frame, text="صنف یازدهم", width=10)
grade_12_button = ctk.CTkButton(output_frame, text="صنف دوازدهم", width=10)

buttons =[(grade_1_button, 680, 50), (grade_2_button, 680, 100), (grade_3_button, 680, 150), (grade_4_button, 680, 200),
    (grade_5_button, 680, 250), (grade_6_button, 680, 300), (grade_7_button, 680, 350), (grade_8_button, 680, 400),
    (grade_9_button, 680, 450), (grade_10_button, 680, 500), (grade_11_button, 680, 550), (grade_12_button, 680, 600)          
]

for btn, _, _ in buttons:
    btn.place_forget()

grade = ctk.CTkLabel(output_frame, width=10)
label_1_1 = ctk.CTkLabel(output_frame, width=3)
label_1_2 = ctk.CTkLabel(output_frame, width=3)
label_1_3 = ctk.CTkLabel(output_frame, width=3)
label_1_4 = ctk.CTkLabel(output_frame, width=3)
label_1_5 = ctk.CTkLabel(output_frame, width=3)
label_1_6 = ctk.CTkLabel(output_frame, width=3)
label_1_7 = ctk.CTkLabel(output_frame, width=3)
label_1_8 = ctk.CTkLabel(output_frame, width=3)
label_1_9 = ctk.CTkLabel(output_frame, width=3)
label_1_10 = ctk.CTkLabel(output_frame, width=3)
label_1_11 = ctk.CTkLabel(output_frame, width=3)
label_1_12 = ctk.CTkLabel(output_frame, width=3)
label_1_13 = ctk.CTkLabel(output_frame, width=3)
label_1_14 = ctk.CTkLabel(output_frame, width=3)
label_1_15 = ctk.CTkLabel(output_frame, width=3)
label_1_16 = ctk.CTkLabel(output_frame, width=3)
label_1_17 = ctk.CTkLabel(output_frame, width=3)
label_1_18 = ctk.CTkLabel(output_frame, width=3)
label_1_19 = ctk.CTkLabel(output_frame, width=3)

label_2_1 = ctk.CTkLabel(output_frame, width=3)
label_2_2 = ctk.CTkLabel(output_frame, width=3)
label_2_3 = ctk.CTkLabel(output_frame, width=3)
label_2_4 = ctk.CTkLabel(output_frame, width=3)
label_2_5 = ctk.CTkLabel(output_frame, width=3)
label_2_6 = ctk.CTkLabel(output_frame, width=3)
label_2_7 = ctk.CTkLabel(output_frame, width=3)
label_2_8 = ctk.CTkLabel(output_frame, width=3)
label_2_9 = ctk.CTkLabel(output_frame, width=3)
label_2_10 = ctk.CTkLabel(output_frame, width=3)
label_2_11 = ctk.CTkLabel(output_frame, width=3)
label_2_12 = ctk.CTkLabel(output_frame, width=3)
label_2_13 = ctk.CTkLabel(output_frame, width=3)
label_2_14 = ctk.CTkLabel(output_frame, width=3)
label_2_15 = ctk.CTkLabel(output_frame, width=3)
label_2_16 = ctk.CTkLabel(output_frame, width=3)
label_2_17 = ctk.CTkLabel(output_frame, width=3)
label_2_18 = ctk.CTkLabel(output_frame, width=3)
label_2_19 = ctk.CTkLabel(output_frame, width=3)

label_3_1 = ctk.CTkLabel(output_frame, width=3)
label_3_2 = ctk.CTkLabel(output_frame, width=3)
label_3_3 = ctk.CTkLabel(output_frame, width=3)
label_3_4 = ctk.CTkLabel(output_frame, width=3)
label_3_5 = ctk.CTkLabel(output_frame, width=3)
label_3_6 = ctk.CTkLabel(output_frame, width=3)
label_3_7 = ctk.CTkLabel(output_frame, width=3)
label_3_8 = ctk.CTkLabel(output_frame, width=3)
label_3_9 = ctk.CTkLabel(output_frame, width=3)
label_3_10 = ctk.CTkLabel(output_frame, width=3)
label_3_11 = ctk.CTkLabel(output_frame, width=3)
label_3_12 = ctk.CTkLabel(output_frame, width=3)
label_3_13 = ctk.CTkLabel(output_frame, width=3)
label_3_14 = ctk.CTkLabel(output_frame, width=3)
label_3_15 = ctk.CTkLabel(output_frame, width=3)
label_3_16 = ctk.CTkLabel(output_frame, width=3)
label_3_17 = ctk.CTkLabel(output_frame, width=3)
label_3_18 = ctk.CTkLabel(output_frame, width=3)
label_3_19 = ctk.CTkLabel(output_frame, width=3)

number_labels = [
    (grade, 555, 60), (label_1_1, 506, 142), (label_1_2, 506, 167), (label_1_3, 506, 192), (label_1_4, 506, 217), (label_1_5, 506, 242),
    (label_1_6, 506, 267), (label_1_7, 506, 292), (label_1_8, 506, 317), (label_1_9, 506, 342), (label_1_10, 506, 367), (label_1_11, 506, 392),
    (label_1_12, 506, 417), (label_1_13, 506, 442), (label_1_14, 506, 467), (label_1_15, 506, 492), (label_1_16, 506, 517), (label_1_17, 506, 542),
    (label_1_18, 506, 567), (label_1_19, 506, 592),
    (label_2_1, 461, 142), (label_2_2, 461, 167), (label_2_3, 461, 192), (label_2_4, 461, 217), (label_2_5, 461, 242), (label_2_6, 461, 267), 
    (label_2_7, 461, 292), (label_2_8, 461, 317), (label_2_9, 461, 342), (label_2_10, 461, 367), (label_2_11, 461, 392), (label_2_12, 461, 417),
    (label_2_13, 461, 442), (label_2_14, 461, 467), (label_2_15, 461, 492), (label_2_16, 461, 517), (label_2_17, 461, 542), (label_2_18, 461, 567), 
    (label_2_19, 461, 592),
    (label_3_1, 416, 142), (label_3_2, 416, 167), (label_3_3, 416, 192), (label_3_4, 416, 217), (label_3_5, 416, 242), (label_3_6, 416, 267), 
    (label_3_7, 416, 292), (label_3_8, 416, 317), (label_3_9, 416, 342), (label_3_10, 416, 367), (label_3_11, 416, 392), (label_3_12, 416, 417), 
    (label_3_13, 416, 442), (label_3_14, 416, 467), (label_3_15, 416, 492), (label_3_16, 416, 517), (label_3_17, 416, 542), (label_3_18, 416, 567),
    (label_3_19, 416, 592)
]

for lbl, _, _ in number_labels:
    lbl.place_forget()

def print_message(id_input, number_labels, buttons, name1, label_message_info, path = "info.json"):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    student_info = data["students"][id_input]
    label_message_info[0][0].config(text=student_info["id"])
    label_message_info[1][0].config(text=student_info["name"])
    label_message_info[2][0].config(text=student_info["father_name"])
    label_message_info[3][0].config(text=student_info["grand_father_name"])
    label_message_info[4][0].config(text=student_info["tazkera_number"])
    label_message_info[5][0].config(text=student_info["date_of_birth"])
    label_message_info[6][0].config(text=student_info["year_of_entry"])
    label_message_info[7][0].config(text=student_info["class_of_entry"])

    # return

    def table_of_results():
        canvas.itemconfigure("Announcement", state="hidden")
        canvas.create_rectangle(10, 10, 800, 650, width = 100, tags = "Table_of_results")

        for label, _, _ in name1:
            label.place_forget()

        for btn, _, _ in buttons:
            btn.place_forget()

        for lbl, _, _ in number_labels:
            lbl.place_forget()


    button_table_of_resulst = ctk.CTkButton(output_frame, text = "جدول نتایج", fg_color = "blue", width = 10, command = table_of_results)
    button_table_of_resulst.place(x = 900, y = 500)

    def announcement():
        canvas.itemconfigure("Table_of_results", state="hidden")

        for label, x, y in name1:
            label.place(x=x, y=y)

        for btn, x, y in buttons:
            btn.place(x = x, y = y)

        for lbl, x, y in number_labels:
            lbl.place(x = x, y = y)

        canvas.create_rectangle(400, 50, 650, 630, outline = "black", width = 10, tags = "Announcement")

        for j in range(3):
            canvas.create_line(445 + (45 * j), 50, 445 + (45 * j), 630, tags = "Announcement")

        for i in range(19):
            canvas.create_line(400, 140 + (i * 25), 650, 140 + (i * 25), tags = "Announcement")

        canvas.create_line(535, 95, 650, 95, width = 2, tags = "Announcement")

        canvas.create_text(512, 100, text="چهارونیم ماهه", angle = 90, tags = "Announcement")
        canvas.create_text(467, 100, text="سالانه", angle = 90, tags = "Announcement")
        canvas.create_text(422, 100, text="نتیجه نهایی", angle = 90, tags = "Announcement")
        canvas.create_text(590, 110, text="مضامین", tags = "Announcement")

    button_announcement = ctk.CTkButton(output_frame, text = "اطلاعنامه", fg_color = "blue", width = 10, command = announcement)
    button_announcement.place(x = 900, y = 570)

submit_button = ctk.CTkButton(output_frame, text = "تایید", fg_color = "cyan", width = 15, command= lambda: print_message((entry_1.get()), number_labels, buttons, name1, label_message_info))
submit_button.place(x = 875, y = 20)

menu_bar = tk.Menu(top)

main_menu = tk.Menu(menu_bar, tearoff=0)
main_menu.add_command(label="Main Menu", command=lambda: show_frame(output_frame))
main_menu.add_separator()
main_menu.add_command(label="Entering info", command=lambda: show_frame(input_info))
main_menu.add_command(label="Entering number", command=lambda: show_frame(input_number))
menu_bar.add_cascade(label="Menu", menu=main_menu)

top.config(menu=menu_bar)

show_frame(output_frame)

top.mainloop()