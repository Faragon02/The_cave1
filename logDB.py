import sqlite3
from tkinter import *
from tkinter import messagebox

## 함수 선언 부분 ##
def insert_data():
    con, cur = None, None
    data1, data2, data3, data4,data5 = "","", "", "", "" # ID,이름,이메일,출생년도
    sql = ""

    con = sqlite3.connect("D:/pylogin/logDB") # DB에 연결
    cur = con.cursor() # DB실행 혹은 리턴 통로 역활

    data1 = edt1.get(); data2 = edt2.get();data3 = edt3.get();data4 = edt4.get();data5 = edt5.get() #각 데이터 입력 받음
    try:
        sql = "INSERT INTO userTable VALUES('" + data1 + "','" + data2 + "','" + data3 + "','" + data4 +"',"+ data5+")"
        cur.execute(sql)
    except :
        messagebox.showerror('ERROR','데이터 입력 오류')
    else:
        messagebox.showinfo('Succesfull','데이터 입력 성공')
        pass
    con.commit() # DB에 저장
    con.close() # DB 종료

def select_data():
    strdata1, strdata2, strdata3, strdata4, strdata5= [], [], [], [], []

    con = sqlite3.connect("D:/pylogin/logDB")
    cur = con.cursor()

    cur.execute("SELECT * FROM usertable")  # 저장된 DB 출력

    # table 표시
    strdata1.append("사용자ID");strdata2.append("사용자 Password")
    strdata3.append("이름");strdata4.append("Email")
    strdata5.append("나이")
    strdata1.append("-------");strdata2.append("-------")
    strdata3.append("-------");strdata4.append("-------")
    strdata5.append("-------")

    # Data 조회
    while (True):

        row = cur.fetchone()   # DB 조회 호출
        if row == None:        # 들어온 것이 없다.
            break              # 종료
        strdata1.append(row[0]);strdata2.append(row[1])    # 호출한 데이터를 각 strdata에 저장
        strdata3.append(row[2]); strdata4.append(row[3])
        strdata5.append(row[4])
    print(strdata1)
    print(strdata2)
    print(strdata3)
    print(strdata4)
    print(strdata5)

    listdata1.delete(0, listdata1.size()-1); listdata2.delete(0, listdata2.size()-1)  # listbox 초기화
    listdata3.delete(0, listdata3.size()-1); listdata4.delete(0, listdata4.size()-1)
    listdata5.delete(0, listdata5.size()-1)

    for item1,item2, item3, item4, item5 in zip(strdata1,strdata2,strdata3,strdata4,strdata5):
        listdata1.insert(END, item1); listdata2.insert(END, item2)
        listdata3.insert(END, item3); listdata4.insert(END, item4)
        listdata5.insert(END, item5)
    con.close()
def delete_data():
    con = sqlite3.connect("D:/pylogin/logDB")
    cur = con.cursor()

    cur.execute("SELECT * FROM usertable")

    con.commit()
    con.close()
    pass

## 메인 코드 부분 ##

window = Tk()
window.geometry("800x300")
window.title("DataBase center")

edtframe = Frame(window)
edtframe.pack()
listframe = Frame(window)
listframe.pack(side=BOTTOM, fill=BOTH, expand=1)

# 입력창
edt1 = Entry(edtframe, width=10);edt1.pack(side = LEFT, padx = 10, pady =10)
edt2 = Entry(edtframe, width=10);edt2.pack(side = LEFT, padx = 10, pady =10)
edt3 = Entry(edtframe, width=10);edt3.pack(side = LEFT, padx = 10, pady =10)
edt4 = Entry(edtframe, width=10);edt4.pack(side = LEFT, padx = 10, pady =10)
edt5 = Entry(edtframe, width=10);edt5.pack(side = LEFT, padx = 10, pady =10)

# Button
btn_insert = Button(edtframe, text="입력", command=insert_data)
btn_insert.pack(side=LEFT, padx=10, pady=10)
btn_select = Button(edtframe, text="조회", command=select_data)
btn_select.pack(side=LEFT, padx=10, pady=10)
btn_delete = Button(edtframe, text="삭제", command=delete_data)
btn_delete.pack(side=LEFT, padx=10, pady=10)

# ListBox
listdata1 = Listbox(listframe, bg='Yellow');listdata1.pack(side=LEFT, fill=BOTH, expand=1)
listdata2 = Listbox(listframe, bg='Yellow');listdata2.pack(side=LEFT, fill=BOTH, expand=1)
listdata3 = Listbox(listframe, bg='Yellow');listdata3.pack(side=LEFT, fill=BOTH, expand=1)
listdata4 = Listbox(listframe, bg='Yellow');listdata4.pack(side=LEFT, fill=BOTH, expand=1)
listdata5 = Listbox(listframe, bg='Yellow');listdata5.pack(side=LEFT, fill=BOTH, expand=1)

window.mainloop()
