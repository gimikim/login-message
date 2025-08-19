import tkinter as tk
from tkinter import messagebox as mbox, ttk
import re    # 특정 문자열 패턴 일치 검사를 위함.
import os

def open_mainmenu2(user_id):
    mainmenu2_window = tk.Toplevel()
    mainmenu2_window.title("메세지 기능")   # 공통으로 필요하니 여기서 한 번만 보장
    
    folder = "messages"
    os.makedirs(folder, exist_ok=True)
    
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
            os.makedirs(folder, exist_ok=True) # 폴더가 없으면 생성, 있으면 넘어감
            
            with open(os.path.join(folder, f'messages_{receiver_id}.txt'), 'a',encoding="UTF-8") as f:     # 'w': 없으면 만들고, 기존 내용에 덮어씀. 'a': 추가 모드, 기존 내용 뒤에 이어씀.
                f.writelines(f"[{now}] {user_id}: {content}\n") 
        
            with open(os.path.join(folder, f'sent_messages_{user_id}.txt'), 'a', encoding="UTF-8") as f:            #💡추가된 부분: "내가 보낸 메시지" 파일
                f.writelines(f"[{now}] 받는 사람: {receiver_id} | {content}\n\n")        
        
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
        
    
    def check_message():    # "메세지 확인하기"
        try:
            filename = f"messages_{user_id}.txt"
            
            path = os.path.join(folder, filename)
            
            with open(path,'r',encoding="UTF-8") as f:
                lines = f.readlines()
            
            new_lines = []
            i = 0
            
            pattern = re.compile(r'^\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\]')
            
            while i < len(lines):
                new_lines.append(lines[i])
                # 메세지 시작인 경우
                if pattern.match(lines[i]):    # '['로 시작하고 ']'이 있는 경우, 다음 줄로 넘어간다. 그게 아니면 다음 줄로
                    i += 1
                    # 메세지 본문 줄 계속 추가
                    while i < len(lines) and not pattern.match(lines[i]):  # len(lines[i]) > 21 : 인덱스가 22가 없는데 찾으려 하면 IndexError가 발생할 수 있기에, lines[i][22] 전에 오류 방지.
                        new_lines.append(lines[i])
                        i += 1
                    # 메세지 블럭 끝에 [읽음] 추가
                    if not new_lines[-1].strip() == '':   # 마지막 줄에 '[읽음]'이 없다면 추가한다.
                        new_lines.append('[읽음]\n\n')
                    
                else:
                    i += 1
            # 파일 덮어쓰기
            os.makedirs(folder, exist_ok=True)
            
            with open(os.path.join(folder, f'messages_{user_id}.txt'), 'w', encoding='UTF-8') as f:
                f.writelines(new_lines)
            
            # 출력용 문자열을 합침
            content = ''.join(new_lines)
            
        except FileNotFoundError:
            content = "아직 누구에게도 받은 메세지가 없습니다."
        
        # 받은 메세지 확인창
        check_message_window = tk.Toplevel()
        check_message_window.title("받은 메세지 확인창")
        check_message_window.geometry("400x300")
        
        # 프레임: 텍스트와 스크롤바를 함께 묶기 위해 사용
        frame = ttk.Frame(check_message_window)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10) # ttk: tk보다 좀 더 최신, expand=True : 창 크기가 변할 때 함께 늘어난다. padx/y는 가장자리 여백을 10픽셀 추가함.   fill=tk.BOTH는 pack()을 사용할 때 위젯이 부모 영역 안에서 얼마나 공간을 채울 것인지를 정하는 옵션이야.

        # 텍스트 위젯
        text_widget = tk.Text(frame, wrap='word', state='normal')   # 일단은 편집 가능 상태로 설정      # wrap='word': 단어 단위로 줄바꿈이 되도록 설정, state=normal: 텍스트 수정 가능 상태로 시작.
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)   # 👉 텍스트 위젯을 프레임 왼쪽에 배치하고, 위젯을 부모영역의 가로 + 세로로 꽉 채움. 보통 expand=True와 함께 사용해서 창 크기 변경 시 텍스트 위젯도 함께 변경되도록 설정함.

        # 스크롤바
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=text_widget.yview) # orient=tk.VERTICAL: 스크롤바가 세로 방향, command=text_widget.yview : 스크롤바 조작 시 텍스트 위젯의 세로 스크롤을 연결.(스크롤바 -> 텍스트. 양방향 연결 필요❗)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)    # 👉 스크롤바를 프레임의 오른쪽에 붙이고, 세로로 전체 높이에 맞게 늘린다.
    
        # 텍스트 위젯에 스크롤바 연결
        text_widget.config(yscrollcommand=scrollbar.set)    # 👉 이번엔 반대 방향 연결: 텍스트 위젯에서 스크롤할 때 스크롤바 위치도 같이 바뀌도록 연결.

        # 받은 메시지_텍스트 위젯에 추가
        text_widget.insert(tk.END, content) 
        text_widget.config(state='disabled')
        
    def check_sent_message():     # "보낸 메세지 확인하기"
        try:
            filename = f'sent_messages_{user_id}.txt'
            
            path = os.path.join(folder, filename)
             
            with open(path,'r',encoding="UTF-8") as f:
                lines = f.readlines()

            # 출력용 문자열을 합침
            content = ''.join(lines)
            
        except FileNotFoundError:
            content = "누구에게도 보낸 메세지가 없습니다."
            
        # 보낸 메세지 확인창
        check_sent_message_window = tk.Toplevel()
        check_sent_message_window.title("보낸 메세지 확인창")
        check_sent_message_window.geometry("400x300")
        
        # 프레임: 텍스트와 스크롤바를 함께 묶기 위해 사용
        frame = ttk.Frame(check_sent_message_window)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10) # ttk: tk보다 좀 더 최신, expand=True : 창 크기가 변할 때 함께 늘어난다. padx/y는 가장자리 여백을 10픽셀 추가함.   fill=tk.BOTH는 pack()을 사용할 때 위젯이 부모 영역 안에서 얼마나 공간을 채울 것인지를 정하는 옵션이야.

        # 텍스트 위젯
        text_widget = tk.Text(frame, wrap='word', state='normal')   # 일단은 편집 가능 상태로 설정      # wrap='word': 텍스트가 너무 길어서 줄바꿈될 때 단어 단위로 넘어가도록 설정(단어 잘리지 않음), state=normal: 텍스트 수정 가능 상태로 시작.
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)   # 👉 텍스트 위젯을 프레임 왼쪽에 배치하고, 위젯을 부모영역의 가로 + 세로로 꽉 채움. 보통 expand=True와 함께 사용해서 창 크기 변경 시 텍스트 위젯도 함께 변경되도록 설정함.

        # 스크롤바
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=text_widget.yview) # orient=tk.VERTICAL: 스크롤바가 세로 방향, command=text_widget.yview : 스크롤바 조작 시 텍스트 위젯의 세로 스크롤을 연결.(스크롤바 -> 텍스트. 양방향 연결 필요❗)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)    # 👉 스크롤바를 프레임의 오른쪽에 붙이고, 세로로 전체 높이에 맞게 늘린다.
    
        # 텍스트 위젯에 스크롤바 연결
        text_widget.config(yscrollcommand=scrollbar.set)    # 👉 이번엔 반대 방향 연결: 텍스트 위젯에서 스크롤할 때 스크롤바 위치도 같이 바뀌도록 연결.

        # 받은 메시지_텍스트 위젯에 추가
        text_widget.insert(tk.END, content) 
        text_widget.config(state='disabled')
        
    def delete_message(user_id):
        messages = []
        filename = f"messages_{user_id}.txt"

        # 메시지 읽기
        def load_messages():
            nonlocal messages   # 파이썬에서 중첩 함수가 바깥 함수의 변수를 수정하려면 nonlocal 키워드를 써야 합니다.

            try:
                path = os.path.join(folder, filename)
                with open(path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
            except FileNotFoundError:
                lines = []

            messages.clear()    # 이전에 있던 메세지 리스트 비우기
            current_message = []
            for line in lines:
                current_message.append(line)
                if line.strip() == "[읽음]":
                    messages.append(current_message)
                    current_message = []

        # 메시지 화면 표시 + 삭제 버튼 생성
        def display_messages():
            text_widget.config(state=tk.NORMAL) # 메세지 내용 변경을 위해 속성을 NORMAL로 변경하는 듯.
            text_widget.delete("1.0", tk.END)   # 텍스트 위젯의 처음부터 끝까지 삭제(그러고 뒤에서 덮어쓰기 하려는 듯.)

            for idx, message in enumerate(messages):     # messages 리스트 안의 요소를 한 줄씩 번호를 매기는 것 같음.
                start_index = text_widget.index(tk.INSERT)  # 지울 내용의 시작 부분 같음. index(tk.INSERT)는 "현재 커서"의 위치! 클릭하면 자동으로 인식되는 건가?
                text_widget.insert(tk.END, ''.join(message) + "\n") # 텍스트를 문서의 맨 끝에 삽입한다.

                tag = f"msg_{idx}"   # 이름만 태그고, 실제론 "마크"임.
                text_widget.mark_set(tag, start_index)  # 텍스트 위젯에 마크를 설정한다. 

                text_widget.window_create(  # 텍스트 위젯에 문자열 + 다른 위젯(버튼, 체크박스, 이미지 등)을 문자처럼 한 줄에 넣을 수 있는 메서드
                    tk.END,
                    window=tk.Button(
                        text_widget,
                        text="삭제",
                        command=lambda i=idx: delete_message_index(i)   # 클릭 시, 현재 반복(for)의 index 값을 캡처, delete_message(i)를 호출. (지금 버튼이 만들어질 때의 index 값을 기억해서 i에 넣고, 클릭하면 그 i로 실행) i=index 안쓰면 for문 람다가 마지막 index만 보게 됨.
                    )
                )
                text_widget.insert(tk.END, "\n\n")  # 버튼 뒤에 빈 줄 2개를 추가해 다음 메세지와 구분.

            text_widget.config(state=tk.DISABLED)   # "읽기 전용"으로 속성 변경(텍스트는 수정 불가, 버튼은 클릭 가능)

        # 메시지 삭제
        def delete_message_index(index):
            del messages[index]
            with open(os.path.join(folder, filename), 'w', encoding='utf-8') as f:    # messages 리스트 안에 특정 내용은 지우고, 'w' 모드로 덮어쓰기를 함. messages 리스트를 줄마다 입력함.
                for msg in messages:
                    f.writelines(msg)
            display_messages()

        # GUI 창 생성
        root = tk.Toplevel()  # 기존 메인 윈도우 위에 뜨도록 Toplevel 사용
        root.title("메세지 뷰어")
        
        # Text 위젯 생성
        text_widget = tk.Text(root, width=50, height=20)
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Scrollbar 생성
        scrollbar = tk.Scrollbar(root, command=text_widget.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_widget.config(yscrollcommand=scrollbar.set, state=tk.DISABLED)

        load_messages()
        display_messages()

    
    def log_out():
        mbox.showinfo("알림","로그아웃 되었습니다.")
        mainmenu2_window.destroy()  # quit은 전체 창을 닫아버림.
        
    
    tk.Entry(mainmenu2_window, text="메세지 기능")
    
    btn1 = tk.Button(mainmenu2_window, text="메세지 전송", command=send_message, width=30) # 메세지 보내기 버튼
    btn1.pack(padx=10, pady=5)
    
    btn2 = tk.Button(mainmenu2_window, text="받은 메세지 확인", command=check_message, width=30) # 메세지 확인 버튼
    btn2.pack(padx=10, pady=5)
    
    btn3 = tk.Button(mainmenu2_window, text="보낸 메세지 확인", command=check_sent_message, width=30) # 보낸 메세지 확인 버튼
    btn3.pack(padx=10, pady=5)
    
    btn4 = tk.Button(mainmenu2_window, text="메세지 삭제", command=lambda: delete_message(user_id), width=30) # 메세지 삭제하기 버튼
    btn4.pack(padx=10, pady=5)
    
    btn5 = tk.Button(mainmenu2_window, text="로그아웃", width=30, command=log_out) # 로그아웃 버튼(메인1 화면만 남도록)
    btn5.pack(padx=10, pady=5)