import tkinter as tk
import datetime

def check_password():
    entered_password = password_entry.get()
    if entered_password == "114514":  # 将 "password" 替换为你设置的密码
        root.destroy()

def update_time():
    #time_label.config(text="你的电脑被我锁了")  # 将显示时间的地方改为"已锁定"
    time_label.config(text="给up自在的猫LJC三联解锁") 
    #root.after(10, update_time)

def disable_keys(event):
    keys_to_disable = ["Control_L", "Control_R", "Super_L", "Super_R", "Shift_L", "Shift_R"]
    if event.keysym in keys_to_disable:
        return "break"

root = tk.Tk()
root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda event: None)  # 禁用ESC键关闭窗口
root.bind_all("<KeyPress>", disable_keys)  # 禁用CTRL键、Windows键和Shift键
#root.bind("<CTRL>", lambda event: None)

password_label = tk.Label(root, text="输入密码以解锁:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

unlock_button = tk.Button(root, text="解锁", command=check_password)
unlock_button.pack()

time_label = tk.Label(root, font=("Helvetica", 80))
time_label.pack()

update_time()

root.mainloop()
