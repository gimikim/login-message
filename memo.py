import tkinter as tk
from tkinter import messagebox as mbox
# ---------------- gui version ---------------
def send_message():
    from datetime import datetime
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open('users.txt', 'r',encoding="UTF-8") as f:
        lines = [line.strip() for line in f.readlines()]
    
    def submit_send():
        # 입력창 내용을 가져온다.(수신자, 메세지 내용)
        receiver_id = receiver_entry.get()
        
        for j in range(1, len(lines), 4):   # len(lines)+1 해야 하는 거 아닌가?
            if receiver_id == lines[j]:
                break
            else:
                mbox.showerror("오류", "존재하지 않는 ID입니다.")
                
        content = text.get("1.0", "end-1c") # 1.0: 첫 행 0번째 문자. 1c: 문자 한 개. 안빼면 다음 줄까지 포함됨.
        
        # 작성하기
        with open(f'messages_{receiver_id}.txt', 'a',encoding="UTF-8") as f:     # 'w': 없으면 만들고, 기존 내용에 덮어씀. 'a': 추가 모드, 기존 내용 뒤에 이어씀.
            f.writelines(f"[{now}] {my_id}: {content}\n") 
    
        
        
    send_message_window = tk.Toplevel()
    send_message_window.title("메세지 보내기")
    
    tk.Label(send_message_window, text="메세지 전송하기")   # 메세지 전송하기(label)
    receiver_label = tk.Label(send_message_window)  # 수신자 라벨
    text_label = tk.Label(send_message_window)      # 메시지 라벨
    
    # 라벨 배치
    receiver_label.grid(row=0, column=0)
    text_label.grid(row=1, column=0)
    
    receiver_entry = tk.Entry(send_message_window).grid(row=0, column=1)  # 수신자 입력창(entry)
    text = tk.Text(send_message_window, width=40, height=10).grid(row=1, column=1)  # 메세지 입력창(entry)
    
    tk.Button(send_message_window, text="전송", command=submit_send).grid(row=2, column=0, columnspan=2) # "전송" 버튼
    
    
    
    
# no gui
def send_message(my_id):  
    from datetime import datetime   # import 모듈: 모듈 전체를 가져오는 것, from 모듈 import 이름: 모듈 내에서 필요한 것만 가져온다.
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 메세지 보내기 안에 넣지 않으면, 로그아웃을 했다가 다시 들어오기 전까지 고정된 시간을 이용.
    
    with open('users.txt', 'r',encoding="UTF-8") as f:
        lines = [line.strip() for line in f.readlines()]
    
    while True:
        receiver_id = input("수신자ID를 입력하세요: ")
        id_found = False
        #-----------------
        for j in range(1, len(lines), 4):   # 이중 반복문은 무작접 break 쓰기보다 조건문으로 만드는게 경우 관리하기 쉬운 것 같다.
            if receiver_id == lines[j]:
                id_found = True
                break
            
        # for문 탈출도 그냥 break가 아니라 조건 형식으로 만들자.
        if id_found:    # 탈출 하는 경우가 2가지임-> 1. 일치하는 걸 찾아서
            break       # while문 탈출
        else:           # 2. 다 돌았는데 없어서
            print("존재하지 않는 ID입니다.")

  
    import sys        
    print("메시지 내용을 입력하세요. (입력 종료를 하려면 메시지 끝에 '[끝]'을 꼭 입력해주시고, 새 줄에서 Ctrl+ z + Enter 입력해주세요.)")
    content = sys.stdin.read()   # readlines()는 input처럼 str인자(prompt 메시지)를 넣을 수 없음. # practice12 
    content = content.replace('\x1a', '')  # '\x1a'는 ^Z의 ASCII 코드  -> 제거 목적
    
    print("입력 결과:")
    print(content)
        
    with open(f'messages_{receiver_id}.txt', 'a',encoding="UTF-8") as f:     # 'w': 없으면 만들고, 기존 내용에 덮어씀. 'a': 추가 모드, 기존 내용 뒤에 이어씀.
        f.writelines(f"[{now}] {my_id}: {content}\n")       # f.writelines()를 쓰면 리스트의 각 요소를 그대로 파일에 씀. 개행문자 포함됨.   그냥 f.write(str(content))로 하면 readlines()는 리스트의 대괄호 ' , 다 저장됨.   write는 문자열만 저장함.

    # \ / : * ? " < > |  <- 파일 이름에 사용할 수 없는 문자