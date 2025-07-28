import tkinter as tk
from tkinter import messagebox as mbox

root = tk.Tk()  # Tk 클래스     ,창 생성
root.title("메인메뉴1")   # 타이틀 바

## 메인 메뉴1 창
# 라벨: 회원가입 / 로그인
# 버튼: 회원가입, 로그인, 종료하기

label1 = tk.Label(root, text="회원가입 / 로그인", width=30)    # root를 명시하는 이유는 계층 구조와 관련. root는 최상위 창으로 생성될 위젯이 어디에 속할 지(자녀 위젯) 알려주는 것. 없으면 "TypeError".
label1.pack(padx=10, pady=5)    # pack: 레이아웃 함수(배치)

def on_click1():
    mbox.showinfo("message", "버튼1을 클릭했습니다!")
def on_click2():
    mbox.showinfo("message", "버튼1을 클릭했습니다!")
def on_click3():
    mbox.showinfo("message", "버튼1을 클릭했습니다!")
    
btn1 = tk.Button(root, text="회원가입", command=on_click1, width=30)
btn1.pack(padx=10, pady=5)
    
btn2 = tk.Button(root, text="로그인", command=on_click2, width=30)
btn2.pack(padx=10, pady=5)

btn2 = tk.Button(root, text="종료하기", command=on_click3, width=30)
btn2.pack(padx=10, pady=5)

root.mainloop()     


## 메인 메뉴2 창
# 라벨: 메시지 메뉴
# 버튼: 메시지 보내기, 받은 메시지 확인, 메시지 삭제, 나가기
