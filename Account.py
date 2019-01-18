from tkinter import *
from tkinter import messagebox
import sqlite3

# Part of variable declare #
# Part of function declare #
def insert_data():
    account_con, account_cur = None, None
    data1,data2,data3,data4,data5 ="","","","",""
    sql = ""

    account_con = sqlite3.connect("D:/pylogin/logDB")
    account_cur = account_con.cursor()

    data1 = txt_Id.get(); data2 = txt_pass.get()
    data3 = txt_name.get(); data4 = txt_E.get()
    data5 = txt_age.get()
    # account_cur.execute("CREATE TABLE usertable (ID char(15), PASSWORD char(20), Name char(10), Email char(30), Age int)")
    try:
        sql = "INSERT INTO usertable VALUES('"+ data1 + "','"+ data2 + "','"+ data3 + "','"+ data4 + "',"+ data5 +")"
        account_cur.execute(sql)

    except:
        messagebox.showerror("Failed", "Join Failed")
    else:
        messagebox.showinfo("succeful", "Join Succesfully")
    account_con.commit()
    account_con.close()

def cancle():
    windows2.destroy()

# 메인 코드 부분 #
if __name__ == "__main__":
    windows2 = Tk()
    windows2.title("Account")
    windows2.geometry("500x600")
    windows2.resizable(width=False, height=False)  # 사이즈 고정(Flase ==> True로 바꾸면 된다.)
    windows2.configure(background="White")  # 생성한 winform 배경색 지정 가능

    # label
    la_ac = Label(windows2, text="Account", font=("바탕", 30), fg="blue", bg="white")
    la_ID = Label(windows2, text="ID :", font=("바탕", 15), fg="black"
                  , bg="white", width=30, height=3, anchor=W)
    la_pass = Label(windows2, text="Passward :", font=("바탕", 15), fg="black"
                    , bg="white", width=30, height=3, anchor=W)
    la_name = Label(windows2, text="Name :", font=("바탕", 15), fg="black"
                    , bg="white", width=30, height=3, anchor=W)
    la_E = Label(windows2, text="Email :", font=("바탕", 15), fg="black"
                 , bg="white", width=30, height=3, anchor=W)
    la_age = Label(windows2, text="Age :", font=("바탕", 15), fg="black"
                   , bg="white", width=30, height=3, anchor=W)
    # textbox
    txt_Id = Entry(windows2, width=30)
    txt_pass = Entry(windows2, width=30)
    txt_name = Entry(windows2, width=30)
    txt_E = Entry(windows2, width=30)
    txt_age = Entry(windows2, width=30)

    # button
    btn_insert = Button(windows2, text="가입", font=("바탕", 20), fg="black", bg="white", command=insert_data)
    btn_cancle = Button(windows2, text="취소", font=("바탕", 20), fg="black", bg="white", command=cancle)

    la_ac.pack()
    la_ID.pack()
    txt_Id.pack()
    la_pass.pack()
    txt_pass.pack()
    la_name.pack()
    txt_name.pack()
    la_E.pack()
    txt_E.pack()
    la_age.pack()
    txt_age.pack()
    btn_insert.place(x=150, y= 500, width = 100, height = 50)
    btn_cancle.place(x=350, y= 500, width = 100, height = 50)
    windows2.mainloop()
