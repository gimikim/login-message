import tkinter as tk
from tkinter import messagebox

# ---------------- 파일 기반 사용자 처리 함수 ----------------

def sign_up():  # 버튼 눌렀을 때의 동작 로직을 위에 쓰고, 창, 버튼은 아래에 씀. (단, 오류 메시지 등은 showerror로 위에 바로 적는다.)
    try:
        with open('users.txt','r',encoding="UTF-8") as f:
            file = f.read()
    except FileNotFoundError:
        with open('users.txt','x') as f:    # 파일이 없을 때만 생성, 있으면 생성.
            pass
        file = ""

    def submit_signup():    # submit_signup이 왜 따로 또 있는 거지? 
        nickname = entry_nickname.get()
        user_id = entry_id.get()
        password = entry_password.get()

        if nickname in file:
            messagebox.showerror("오류", "이미 존재하는 닉네임입니다.")
            return
        if user_id in file:
            messagebox.showerror("오류", "이미 존재하는 ID입니다.")
            return

        with open('users.txt', 'a', encoding="UTF-8") as f:
            f.write(nickname + "\n" + user_id + "\n" + password + "\n\n")

        messagebox.showinfo("성공", "회원가입이 완료되었습니다.")
        signup_window.destroy()

    signup_window = tk.Toplevel()   
    signup_window.title("회원가입")
    
    tk.Label(signup_window, text="닉네임").grid(row=0, column=0)    
    tk.Label(signup_window, text="ID").grid(row=1, column=0)
    tk.Label(signup_window, text="Password").grid(row=2, column=0)

    entry_nickname = tk.Entry(signup_window)    
    entry_id = tk.Entry(signup_window)
    entry_password = tk.Entry(signup_window, show="*")      # 사용자 입력창 만들기 (show="*"는 비밀번호 마스킹)

    entry_nickname.grid(row=0, column=1)    # 각 입력창 배치
    entry_id.grid(row=1, column=1)
    entry_password.grid(row=2, column=1)

    tk.Button(signup_window, text="가입하기", command=submit_signup).grid(row=3, column=0, columnspan=2)    # 왜 얘는 변수에 따로 지정하지 않았지? 그럼 이런 경우(gui_practice)는 왜 변수 지정을 하는 거지?


def sign_in():
    try:
        with open('users.txt','r',encoding="UTF-8") as f:
            lines = [line.strip() for line in f.readlines()]    # 파일을 줄 단위로 읽고 공백 제거하여 리스트로 저장
    except FileNotFoundError:
        messagebox.showerror("오류", "회원 데이터 파일이 없습니다.")
        return

    def submit_login():
        id_input = entry_id.get()
        password_input = entry_password.get()

        for i in range(0, len(lines), 4):
            nickname = lines[i]
            user_id = lines[i+1]
            user_password = lines[i+2]

            if id_input == user_id:
                if password_input == user_password:
                    messagebox.showinfo("성공", f"{nickname}님, 로그인되었습니다.")
                    login_window.destroy()
                    return
                else:
                    messagebox.showerror("오류", "비밀번호가 틀렸습니다.")
                    return
        messagebox.showerror("오류", "ID가 존재하지 않습니다.")

    login_window = tk.Toplevel()
    login_window.title("로그인")

    tk.Label(login_window, text="ID").grid(row=0, column=0)
    tk.Label(login_window, text="Password").grid(row=1, column=0)

    entry_id = tk.Entry(login_window)
    entry_password = tk.Entry(login_window, show="*")

    entry_id.grid(row=0, column=1)
    entry_password.grid(row=1, column=1)

    tk.Button(login_window, text="로그인", command=submit_login).grid(row=2, column=0, columnspan=2)

# ---------------- 메인 창 ----------------

window = tk.Tk()
window.title("회원가입 / 로그인 시스템")

tk.Label(window, text="메뉴를 선택하세요:", font=("맑은 고딕", 14)).pack(pady=10)

tk.Button(window, text="회원가입 하기", width=20, height=2, command=sign_up).pack(pady=5)
tk.Button(window, text="로그인 하기", width=20, height=2, command=sign_in).pack(pady=5)
tk.Button(window, text="종료하기", width=20, height=2, command=window.destroy).pack(pady=5)

window.mainloop()
