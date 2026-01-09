# import math
# names=(dir(math))
# for name in names:
 #     print(name)
# import os
# print(os.listdir())]
import tkinter as tk
from tkinter import filedialog
import os, shutil
root= tk.Tk()
root.title("File Organizer")
root.geometry("400x250")
root.configure(bg="#000")
status_var=tk.StringVar(value="Ready to organize")
label=tk.Label(root,textvariable=status_var,bg="#111",fg="#0ff",font=("Arial",10,"bold"),height=2)
label.pack(fill="x",padx=10,pady=20)
types={
"Images":[".jpg",".jpeg",".png",".gif"],
"Docs":[".pdf",".docx",".txt",".pages"],
"Videos":[".mp4",".mov",".avi"],
"Audio":[".mp3",".wav"],
"Code":[".py",".md",".html",".js"],

}
def organize_file(event):
    folder= filedialog.askdirectory()
    if not folder:return

    count=0
    for file in os.listdir(folder):
        if "." not in file:continue
        ext=os.path.splitext(file)[1].lower()

        for category,extension in types.items():
            if ext in extension:
                target_dir=os.path.join(folder,category)
                if not os.path.exists(target_dir):os.makedirs(target_dir)
                shutil.move(os.path.join(folder,file),os.path.join(target_dir,file))
                count+=1
                break
    status_var.set(f"moved {count}files!")



frame=tk.Frame(root,bg="#000")
frame.pack(pady=20)
btn_text="SELECT FOLDER"
btn_widget=tk.Label(frame,text=btn_text,font=("Arial",10,"bold"),bg="#f39c12",fg="White",width=20,height=2,relief="flat")
btn_widget.bind("<Button-1>",organize_file)
btn_widget.pack()
label=tk.Label(root,text="Sorts:Images,Docs...", bg="#000",fg="#555",font=("Arial",10,"bold"))
label.pack(side="bottom",pady=10)


root.mainloop()