import tkinter as tk
from tkinter import messagebox as mbox

root = tk.Tk()  # Tk 클래스     ,창 생성
root.title("메인메뉴1")   # 타이틀 바

label1 = tk.Label(root, text="GUI 프로그래밍", width=30)    # root를 명시하는 이유는 계층 구조와 관련. root는 최상위 창으로 생성될 위젯이 어디에 속할 지(자녀 위젯) 알려주는 것. 없으면 "TypeError".
label1.pack(padx=10, pady=5)    # pack: 레이아웃 함수(배치)

etr1 = tk.Entry(root, width=30)
etr1.pack(padx=10, pady=5)

def on_click1():
    mbox.showinfo("message", "버튼1을 클릭했습니다!")

def on_click2():
    mbox.showinfo("message", etr1.get() + " 를 입력했습니다.")
    
    
btn1 = tk.Button(root, text="버튼1", command=on_click1, width=30)
btn1.pack(padx=10, pady=5)
    
btn2 = tk.Button(root, text="버튼2", command=on_click2, width=30)
btn2.pack(padx=10, pady=5)

root.mainloop()     # 호출

# Label : 텍스트 표시
# Entry : 사용자로부터 특정 문자열 입력 받음
# Button: 특정 기능 실행


