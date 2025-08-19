# ------ 메인 메뉴 창 ------

# 라벨: 회원가입 / 로그인
# 버튼: 회원가입, 로그인, 종료하기
import tkinter as tk
from auth import sign_up, sign_in


root = tk.Tk()
root.title("회원가입 / 로그인")

label1 = tk.Label(root, text="회원가입 / 로그인", width=30)    # root를 명시하는 이유는 계층 구조와 관련. root는 최상위 창으로 생성될 위젯이 어디에 속할 지(자녀 위젯) 알려주는 것. 없으면 "TypeError".
label1.pack(padx=10, pady=5)    # pack: 레이아웃 함수(배치)
    
btn1 = tk.Button(root, text="회원가입", command=sign_up, width=30)    # 회원가입 창으로 넘어가기
btn1.pack(padx=10, pady=5)
    
btn2 = tk.Button(root, text="로그인", command=sign_in, width=30)      # 로그인 창으로 넘어가기
btn2.pack(padx=10, pady=5)

btn3 = tk.Button(root, text="종료하기", command=quit, width=30)      
btn3.pack(padx=10, pady=5)

root.mainloop() 