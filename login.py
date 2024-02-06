import tkinter as tk
import secret_text
import winsound
from tinydb import TinyDB, Query

db = TinyDB('login.json')
User = Query()


def show_password():
    if show.get() == 1:
        password_entry.configure(show='')
    elif show.get() == 0:
        password_entry.configure(show='*')


def secret():
    secret_window = tk.Tk()
    secret_window.geometry('600x620')
    secret_window.resizable(False, False)
    secret_window.title('Secret')
    secret_window_text = tk.Label(secret_window)
    secret_window_text['text'] = secret_text.secret_text
    secret_window_text.pack()
    secret_window_close_button = tk.Button(secret_window, text='Close', command=secret_window.destroy)
    secret_window_close_button.pack()


def validation():
    user = login_entry.get()
    password = password_entry.get()
    check_user = db.search(User.user == user)
    check_password = db.search(User.password == password)
    if not (check_user or check_password):
        error_label['text'] = 'Error. Wrong user/password'
        winsound.PlaySound('SystemHand', winsound.SND_ASYNC)
    elif check_user or check_password:
        secret()
        error_label['text'] = 'Login successful'


root = tk.Tk()
root.title('Login')
root.geometry('300x298')
root.resizable(False, False)

frame = tk.LabelFrame(root)
frame.pack()

login_label = tk.Label(frame, text='User ID', font='Futura 18')
login_label.grid()
login_entry = tk.Entry(frame, font='Futura 18')
login_entry.grid()
password_label = tk.Label(frame, text='Password', font='Futura 18')
password_label.grid()
password_entry = tk.Entry(frame, font='Futura 18', show='*')
password_entry.grid()
show = tk.IntVar()
show_password_checkbox = tk.Checkbutton(frame, text='Show password', variable=show, command=show_password, onvalue=1,
                                        offvalue=0)
show_password_checkbox.grid()
login_button = tk.Button(frame, text='Login', font='Futura 18', command=validation)
login_button.grid()
error_label = tk.Label(frame, text='')
error_label.grid()

for widget in frame.winfo_children():
    widget.grid(padx=10, pady=5, sticky='news')

root.mainloop()
