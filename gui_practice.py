import tkinter as tk
from tkinter import messagebox as mbox

# ------ 회원가입_파일 읽기 ------
def sign_up():  # 동작 중심. 버튼 등 위젯 등은 아래에서 설정 (메인 메뉴에서 회원가입 창으로 넘어갈 때 버튼 구성을 자동으로 실행되도록 하기 위해서 sign_up에 넣어둔 것이군.)
    # 파일 읽기
    try:
        with open('users.txt','r',encoding="UTF-8") as f:
            file = f.read()
    except FileNotFoundError:
        with open('users.txt','x') as f:    # 파일이 없을 때만 생성, 있으면 생성x.
            pass
        file = ""
    
    def submit_signup():    # 가입하기 버튼 눌렀을 때
        # 입력창 정보를 get한다. 파일에 있는지 확인해서 메시지박스(성공, 알림)를 띄운다.
        nickname = entry_nickname.get()
        id = entry_id.get()
        password = entry_password.get()
        
        if nickname in file:
            mbox.showerror("오류", "이미 존재하는 닉네임입니다.")
            return
        if id in file:
            mbox.showerror("오류","이미 존재하는 아이디입니다.")
        
        # 오류 없으면 파일에 입력 a
        with open('users.txt','a',encoding="UTF-8") as f:       # f는 파일객체 이름. f=open(filename, 'w'): f.close() 수동으로 호출, with open() as f는 자동으로 f.close() 호출  
            f.write(nickname + "\n" + id + "\n" + password + "\n\n")      # 그냥 저장하면 줄바꿈 없이 저장돼 구분 어려움
            
    
        mbox.showinfo("성공", "회원가입이 완료되었습니다.")     # 성공 메시지 띄우기
        signup_window.destroy()     # 창 닫기(성공하면 회원가입 창은 닫히고, 성공 메시지 박스는 '확인'누르면 창 닫힘.)
        
            
    # 회원 가입 창(여러번 언급 시 변수에 저장)      # ❓신기하네? 버튼까지도 종속 함수 안에 있어! 안에 있는게 논리적으로 더 맞는건가?
    signup_window = tk.Toplevel()
    signup_window.title("회원가입")


    tk.Label(signup_window, text="닉네임").grid(row=0, column=0)    # 닉네임(라벨)
    tk.Label(signup_window, text="아이디").grid(row=1, column=0)    # 아이디(라벨)
    tk.Label(signup_window, text="비밀번호").grid(row=2, column=0)  # 비밀번호(라벨)

    entry_nickname = tk.Entry(signup_window)            # 닉네임(입력창)      # ❓여기서는 grid가 안붙음. 변수에 저장해야 됨. -> 라벨은 입력 안받고 보여주기만 하니까 바로 gird 붙여도 괜찮. 하지만 entry는 입력값 받고 참조해서 쓸 일 있기 때문에 변수에 저장한 다음에 grid 붙임.(그냥 붙이면 변수값에 entry 객체가 none이 저장됨. (grid는 return none인 매서드이기 때문.))
    entry_id = tk.Entry(signup_window)                  # 아이디(입력창)
    entry_password = tk.Entry(signup_window, show="*")  # 비밀번호(입력창)

    entry_nickname.grid(row=0, column=1)    # 입력창 배치
    entry_id.grid(row=1, column=1)
    entry_password.grid(row=2, column=1)

    # "가입하기" 버튼
    tk.Button(signup_window, text="가입하기", command=submit_signup).grid(row=3, column=0, columnspan=2)
           
def open_mainmenu2(user_id):
    mainmenu2_window = tk.Toplevel()
    mainmenu2_window.title("메세지 기능")
    
    def send_message():
        from datetime import datetime
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open('users.txt', 'r',encoding="UTF-8") as f:
            lines = [line.strip() for line in f.readlines()]
        
        def submit_send():
            receiver_id = receiver_entry.get()  # 입력창 내용을 가져온다.(수신자, 메세지 내용)
            
            for j in range(1, len(lines), 4):   
                if receiver_id == lines[j]:
                    break
            else:
                mbox.showerror("오류", "존재하지 않는 ID입니다.")   # ❗break 다음에 성공인데도 오류 메시지가 뜨게 됨. 
                return  # return 쓰는 게 맞을까?
            
            content = text.get("1.0", "end-1c") # 1.0: 첫 행 0번째 문자. 1c: 문자 한 개. 안빼면 다음 줄까지 포함됨.
            
            # 작성하기
            with open(f'messages_{receiver_id}.txt', 'a',encoding="UTF-8") as f:     # 'w': 없으면 만들고, 기존 내용에 덮어씀. 'a': 추가 모드, 기존 내용 뒤에 이어씀.
                f.writelines(f"[{now}] {user_id}: {content}\n") 
        
            mbox.showinfo("알림", f"{receiver_id}에게 메세지가 전송되었습니다.")
            
            send_message_window.destroy()
            
        send_message_window = tk.Toplevel()
        send_message_window.title("메세지 보내기")
        
        tk.Label(send_message_window, text="메세지 전송하기")   # 메세지 전송하기(label)
        receiver_label = tk.Label(send_message_window, text="수신자 ID")  # 라벨
        text_label = tk.Label(send_message_window, text="메시지 내용")
        
        
        # 라벨 배치
        receiver_label.grid(row=0, column=0)
        text_label.grid(row=1, column=0)
        
        receiver_entry = tk.Entry(send_message_window)
        receiver_entry.grid(row=0, column=1)  # 수신자 입력창(entry)
        
        text = tk.Text(send_message_window, width=40, height=10)    # 메세지 입력창(entry)
        text.grid(row=1, column=1)  # grid는 (get에서) none을 반환하므로 위젯은 별도로 변수에 저장하고, gird는 다음줄에 호출.
        
        tk.Button(send_message_window, text="전송", command=submit_send).grid(row=2, column=0, columnspan=2) # "전송" 버튼
        
        
    
    def check_message():
        print()
        
    def delete_message():
        print()
    
    def log_out():
        mbox.showinfo("알림","로그아웃 되었습니다.")
        mainmenu2_window.destroy()  # quit은 전체 창을 닫아버림.
        
    
    tk.Entry(mainmenu2_window, text="메세지 기능")
    
    btn1 = tk.Button(mainmenu2_window, text="메세지 전송", command=send_message, width=30) # 메세지 보내기 버튼
    btn1.pack(padx=10, pady=5)
    
    btn2 = tk.Button(mainmenu2_window, text="받은 메세지 확인", command=check_message, width=30) # 메세지 확인 버튼
    btn2.pack(padx=10, pady=5)
    
    btn3 = tk.Button(mainmenu2_window, text="메세지 삭제", command=delete_message, width=30) # 메세지 삭제하기 버튼
    btn3.pack(padx=10, pady=5)
    
    btn4 = tk.Button(mainmenu2_window, text="로그아웃", width=30, command=log_out) # 로그아웃 버튼(메인1 화면만 남도록)
    btn4.pack(padx=10, pady=5)
    
def sign_in():  # 로그인
    try:    # 회원가입에서 사용자 정보 읽었는데 로그인에서도 또 하는 이유는 뭐지? 없으면 로그인 할 때 그냥 만들면 되는 거 아닌가? 굳이 함수 제일 앞에 둔 이유는 또 뭐고?
        with open('users.txt', 'r',encoding='UTF-8') as f:
            lines = [line.strip() for line in f.readlines()]  
    except FileNotFoundError:
        mbox.showerror("오류","회원 데이터 파일이 없습니다.")   # 없으면 한 번도 가입한 적 없으니, 회원가입 하라는 뜻.
        return
    

    def submit_signin():    # "로그인" 버튼을 눌렀을 때. 입력창 내용을 가져온다. 파일의 내용과 비교한다. 있으면 로그인완료. 없으면 오류.
        id = entry_id.get()
        password = entry_password.get()
        
        for i in range(0, len(lines), 4):
            user_id = lines[i+1]
            user_password = lines[i+2]
            
            if user_id == id:       # 다시 돌아갈 수 있도록 else는 만들지 않는다.
                if user_password == password:
                    mbox.showinfo("성공", "로그인이 완료되었습니다.")    
                    signin_window.destroy()
                    open_mainmenu2(user_id)     # 메인메뉴2로 ID 전달
                    return  # destroy 있으면 끝 아닌가? 왜 return이 굳이 필요하지? -> destroy는 GUI 창만 닫지만, submit_signup 함수는 계속 실행됨. 문제는 아래에 "아이디 없음" 메시지가 뜨게 됨.
                else:
                    mbox.showerror("오류", "비밀번호가 틀렸습니다.")
                    return
            
        mbox.showerror("오류", "아이디가 존재하지 않습니다.")
        
    signin_window = tk.Toplevel()   # 창 띄우기
    signin_window.title("로그인")
    
    tk.Label(signin_window, text="아이디").grid(row=0, column=0)  # 아이디(라벨)
    tk.Label(signin_window, text="비밀번호").grid(row=1, column=0)  # 비번(라벨)
    
    entry_id = tk.Entry(signin_window)     # 아이디(입력창)
    entry_password = tk.Entry(signin_window, show="*")     # 비번(입력창)
    
    entry_id.grid(row=0, column=1)  # 입력창 배치
    entry_password.grid(row=1, column=1)
    
    tk.Button(signin_window, text="로그인하기",command=submit_signin).grid(row=2, column=0, columnspan=2)


# ------ 메인 메뉴 창 ------

# 라벨: 회원가입 / 로그인
# 버튼: 회원가입, 로그인, 종료하기

root = tk.Tk()
root.title("회원가입 / 로그인")

label1 = tk.Label(root, text="회원가입 / 로그인", width=30)    # root를 명시하는 이유는 계층 구조와 관련. root는 최상위 창으로 생성될 위젯이 어디에 속할 지(자녀 위젯) 알려주는 것. 없으면 "TypeError".
label1.pack(padx=10, pady=5)    # pack: 레이아웃 함수(배치)
    
btn1 = tk.Button(root, text="회원가입", command=sign_up, width=30)    # 회원가입 창으로 넘어가기
btn1.pack(padx=10, pady=5)
    
btn2 = tk.Button(root, text="로그인", command=sign_in, width=30)      # 로그인 창으로 넘어가기
btn2.pack(padx=10, pady=5)

btn2 = tk.Button(root, text="종료하기", command=quit, width=30)      
btn2.pack(padx=10, pady=5)

root.mainloop()     