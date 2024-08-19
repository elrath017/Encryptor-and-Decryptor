import customtkinter as tk
import subprocess

def open_encrypt():
    rooth.destroy()
    subprocess.Popen(["python", "encrypt.py"])

def open_decrypt():
    rooth.destroy()
    subprocess.Popen(["python", "decrypt.py"])


rooth=tk.CTk()
rooth.title("Home page")
rooth.geometry("500x400")


l1=tk.CTkLabel(rooth,text="Text Compressor and Extrator",font=("Arial",20),text_color='white')
l1.place(x=115,y=20)

btn1=tk.CTkButton(rooth,text='Encryption',fg_color='purple',hover_color='grey',command=open_encrypt)
btn1.place(x=80,y=100)

btn2=tk.CTkButton(rooth,text='Decryption',fg_color='purple',hover_color='grey',command=open_decrypt)
btn2.place(x=280,y=100)


rooth.mainloop()