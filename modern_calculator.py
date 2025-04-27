import customtkinter as ctk

# تنظیمات کلی
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

# ساخت پنجره
app = ctk.CTk()
app.title("Modern Calculator")
app.geometry("320x430")  # ابعاد ماشین حساب ویندوز
app.resizable(False, False)

# متغیر برای نگهداری ورودی‌ها
expression = ""

# توابع
def update_display(value):
    global expression
    expression += str(value)
    display.configure(text=expression)

def calculate():
    global expression
    try:
        result = str(eval(expression))
        display.configure(text=result)
        expression = result
    except:
        display.configure(text="Error")
        expression = ""

def clear():
    global expression
    expression = ""
    display.configure(text="")

# صفحه نمایش
display = ctk.CTkLabel(master=app, text="", width=280, height=60,
                       corner_radius=20, fg_color="#ffffff", text_color="#222222",
                       font=("Poppins", 28), anchor="e")
display.pack(pady=20)

# فریم دکمه‌ها
frame = ctk.CTkFrame(master=app, fg_color="#f5f5f5", corner_radius=20)
frame.pack(pady=10, padx=10, expand=True)

# دکمه‌ها
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", ".", "+"),
]

# اضافه کردن دکمه‌ها به فریم با grid
for row_idx, row in enumerate(buttons):
    for col_idx, item in enumerate(row):
        # رنگ پس‌زمینه برای اعداد و عملگرها
        if item in ["+", "-", "*", "/", "C"]:
            color = "#4CAF50"  # رنگ پس‌زمینه سبز برای عملگرها
            text_color = "#ffffff"  # رنگ متن سفید برای عملگرها
        else:
            color = "#ffffff"  # رنگ پس‌زمینه سفید برای اعداد
            text_color = "#222222"  # رنگ متن مشکی برای اعداد

        button = ctk.CTkButton(master=frame, text=item, width=70, height=70,  # افزایش اندازه دکمه‌ها
                               corner_radius=25, font=("Poppins", 24),  # افزایش اندازه فونت
                               fg_color=color, hover_color="#e0e0e0",
                               text_color=text_color,
                               command=lambda val=item: clear() if val == "C" else update_display(val))
        button.grid(row=row_idx, column=col_idx, padx=5, pady=5, sticky="nsew")

# دکمه مساوی
equal_btn = ctk.CTkButton(master=frame, text="=", width=70, height=70,  # افزایش اندازه دکمه مساوی
                          corner_radius=30, font=("Poppins", 28, "bold"),
                          fg_color="#FF5722", hover_color="#e64a19",
                          text_color="#ffffff",
                          command=calculate)
equal_btn.grid(row=4, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")  # تغییر موقعیت

# تنظیمات grid برای فریم دکمه‌ها
for i in range(4):
    frame.grid_columnconfigure(i, weight=1)
for i in range(5):  # تغییر از 4 به 5 برای گنجاندن ردیف دکمه مساوی
    frame.grid_rowconfigure(i, weight=1)

# اجرای برنامه
app.mainloop()
