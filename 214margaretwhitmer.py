##############################################################################
#   a113_TR_simple_window1.py
#   Example soulution: Change its size to 200 by 100 pixels.
##############################################################################
import tkinter as tk

def test_my_button():
    frame_auth.tkraise()
    password = ent_password.get()
    lbl_frame_two.config(text = password)

# main window
root = tk.Tk()
root.wm_geometry("300x150")
root.title("Authentication")

# create empty frame
frame_login = tk.Frame(root)
frame_login.grid(row = 0, column = 0, sticky = "news")

#create username label
lbl_username = tk.Label(frame_login)
lbl_username.config(text='Username:', font = ("Courier"))
lbl_username.pack()

#create username entry box
ent_username = tk.Entry(frame_login, bd=3)
ent_username.config()
ent_username.pack(pady=5)

#create password label
lbl_password = tk.Label(frame_login, text='Password:', font = ("Courier"))
lbl_password.pack()

#create password entry box
ent_password = tk.Entry(frame_login, bd=3, show = '*')
ent_password.pack(pady=5)

# create "login" button
btn_login = tk.Button(frame_login, text = 'Login', command = test_my_button)
btn_login.pack()

#create 2nd frame
frame_auth = tk.Frame(root)
frame_auth.grid(row = 0, column = 0, sticky = "news")

# add label to 2nd frame
lbl_frame_two = tk.Label(frame_auth)
lbl_frame_two.pack()

# raise first frame above 2nd
frame_login.tkraise()

root.mainloop()
