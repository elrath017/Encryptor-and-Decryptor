import customtkinter as tk
from customtkinter import filedialog
from nltk.tokenize import word_tokenize
import subprocess

dict1 = {}

def back():
    rootd.destroy() 
    subprocess.Popen(["python","C:/Users/rahul/Desktop/Coding stuff/python/MCA/it tools lab/it lab project/homepage.py"])

def decrypt_text(x):
    print(dict1)
    decrypted_lines = []
    lines = x.split('\n')
    if_c=0
    else_c=0
    for line in lines:
        decrypted_tokens = []
        line_tokens = word_tokenize(line)
        print ("line_tokens : ", line_tokens)
        for token in line_tokens:
            if token.isdigit():

                decrypted_tokens.append(dict1.get(int(token), token))  # Use dict1.get() to handle missing keys
                if_c += 1
            else:
                decrypted_tokens.append(token)
                else_c += 1 
        decrypted_line = ' '.join(decrypted_tokens)
        decrypted_lines.append(decrypted_line)

    # Join the decrypted lines into a single string
    decrypted_text = '\n'.join(decrypted_lines)

    # print ("decrypted_text :\n",decrypted_text)
    # print ("if_c : ", if_c)
    # print ("else_c : ", else_c)
    return decrypted_text


def upload_file():
    dictfile = filedialog.askopenfilename(title="Select a text file", filetypes=(("Text files", ".txt"), ("All files", ".*")))
    if dictfile:
        with open(dictfile, "r", encoding='UTF-8') as file:
            for line in file:
                key, value = line.strip().split(': ')
                dict1[int(value)] = key
        encryfile_btn.configure(state=tk.NORMAL)


def decry(tokens2):
    dencryfile = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Text files", ".txt"), ("All files", ".*")))
    if dencryfile:
        with open(dencryfile, 'w', encoding='UTF-8') as file:
            file.write(''.join(tokens2))


def upload_file2():
    filename = filedialog.askopenfilename(title="Select a text file", filetypes=(("Text files", ".txt"), ("All files", ".*")))
    if filename:
        with open(filename, "r", encoding='UTF-8') as file:
            text2 = file.read()
            print ("text2 : ", text2)
            tokens2 = decrypt_text(text2)
            print ("tokens2 : ",tokens2)
        decrypt_btn.configure(state=tk.NORMAL)
        decrypt_btn.configure(command=lambda: decry(tokens2))

rootd = tk.CTk()
rootd.title("Decryption")
rootd.geometry('500x400')

lb1=tk.CTkLabel(rootd,text="Upload the dictionary file and Encrypted text file",font=("Arial",20))
lb1.place(x=50,y=20)

up_btn = tk.CTkButton(rootd, text="Dictionary file", fg_color='#8F0B0B',hover_color='grey',command=upload_file)
up_btn.place(x=100,y=100)

encryfile_btn = tk.CTkButton(rootd, text="Encrypted file",fg_color='#8F0B0B',hover_color='grey',state=tk.DISABLED,command=upload_file2)
encryfile_btn.place(x=280,y=100)

decrypt_btn = tk.CTkButton(rootd, text="Decrypt Text",fg_color='#8F0B0B',hover_color='grey',state=tk.DISABLED)
decrypt_btn.place(x=175,y=200)

btn3 = tk.CTkButton(rootd, text='back', command=back)
btn3.place(x=175, y=300)

rootd.mainloop()