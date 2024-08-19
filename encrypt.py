import customtkinter as tk
from customtkinter import filedialog
import endecrypt as ed
import subprocess

def back():
    roote.destroy() 
    subprocess.Popen(["python","homepage.py"])

#upload the corpus
def upload_file():
    filename = filedialog.askopenfilename(title="Select a text file", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if filename:
        with open(filename, "r", encoding='UTF-8') as file:
            text = file.read()
        encrypt_btn.configure(state=tk.NORMAL)
        encrypt_btn.configure(command=lambda: encry(text))

        decrypt_btn.configure(state=tk.NORMAL)


def encry(text):
    tokens=ed.encrypt_text(text)

    #save the token in a text file
    encryfile = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if encryfile:
        with open(encryfile, 'w', encoding='UTF-8') as file:
            file.write(''.join(tokens))

    #save the dictionary file
    if encryfile:
        encryfilename= encryfile.split('.')[0]
        dictfile = f"{encryfilename}_dict.txt"
    if dictfile:
        with open(dictfile, 'w', encoding='UTF-8') as file1:
            for key, value in ed.word_to_int.items():
                file1.write(f"{key}: {value}\n")      
        #print(ed.word_to_int)

#upload file to decrypt
def upload_file2():
    filename = filedialog.askopenfilename(title="Select a text file", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if filename:
        with open(filename, "r", encoding='UTF-8') as file:
            text2 = file.read()
            tokens2=ed.decrypt_text(text2)

    dencryfile = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if dencryfile:
        with open(dencryfile, 'w', encoding='UTF-8') as file:
            file.write(''.join(tokens2))




roote = tk.CTk()
roote.title("Encryption")
roote.geometry('500x400')

up_btn = tk.CTkButton(roote, text="Upload File", fg_color='#8F0B0B',hover_color='grey',command=upload_file)
up_btn.place(x=175,y=20)



encrypt_btn = tk.CTkButton(roote, text="Encrypt Text",fg_color='#8F0B0B',hover_color='grey',state=tk.DISABLED)
encrypt_btn.place(x=100,y=100)

decrypt_btn = tk.CTkButton(roote, text="Decrypt Text",fg_color='#8F0B0B',hover_color='grey',state=tk.DISABLED,command=upload_file2)
decrypt_btn.place(x=280,y=100)

btn3 = tk.CTkButton(roote, text='back', command=back)
btn3.place(x=170, y=200)

roote.mainloop()
