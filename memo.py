import tkinter as tk

# 전역 변수
messages = []
filename = None
text_widget = None

def load_messages():
    """파일에서 메시지를 읽어와 messages 리스트에 저장"""
    global messages
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    messages = []
    current_message = []

    for line in lines:
        current_message.append(line)
        if line.strip() == "[읽음]":  # 메시지 구분
            messages.append(current_message)
            current_message = []                            # 읽은 건 남겨야 하니까, current_message로 담기.

    display_messages()

def display_messages():
    """Text 위젯에 메시지와 삭제 버튼 표시"""
    text_widget.config(state=tk.NORMAL)     # 메세지 내용 변경을 위해 속성을 NORMAL로 변경하는 듯.
    text_widget.delete("1.0", tk.END)   # 텍스트 위젯의 처음부터 끝까지 삭제(그러고 뒤에서 덮어쓰기 하려는 듯.)

    for index, message in enumerate(messages):  # messages 리스트 안의 요소를 한 줄씩 번호를 매기는 것 같음.
        start_index = text_widget.index(tk.INSERT)  # 지울 내용의 시작 부분 같음. index(tk.INSERT)는 "현재 커서"의 위치! 클릭하면 자동으로 인식되는 건가?
        text_widget.insert(tk.END, ''.join(message))    # 텍스트를 문서의 맨 끝에 삽입한다.
        text_widget.insert(tk.END, "\n")    # 줄 단위 구분

        tag = f"msg_{index}"    # 이름만 태그고, 실제론 "마크"임.
        text_widget.mark_set(tag, start_index)  # 텍스트 위젯에 마크를 설정한다. 
        text_widget.window_create(  # 텍스트 위젯에 문자열 + 다른 위젯(버튼, 체크박스, 이미지 등)을 문자처럼 한 줄에 넣을 수 있는 메서드
            tk.END,
            window=tk.Button(
                text_widget,
                text="삭제",
                command=lambda i=index: delete_message(i)   # 클릭 시, 현재 반복(for)의 index 값을 캡처, delete_message(i)를 호출. (지금 버튼이 만들어질 때의 index 값을 기억해서 i에 넣고, 클릭하면 그 i로 실행) i=index 안쓰면 for문 람다가 마지막 index만 보게 됨.
            )
        )
        text_widget.insert(tk.END, "\n\n")  # 버튼 뒤에 빈 줄 2개를 추가해 다음 메세지와 구분.

    text_widget.config(state=tk.DISABLED)   # "읽기 전용"으로 속성 변경(텍스트는 수정 불가, 버튼은 클릭 가능)

def delete_message(index):
    """index에 해당하는 메시지 삭제 후 파일 저장"""
    del messages[index]
    with open(filename, 'w', encoding='utf-8') as f:    # messages 리스트 안에 특정 내용은 지우고, 'w' 모드로 덮어쓰기를 함. messages 리스트를 줄마다 입력함.
        for message in messages:
            f.writelines(message)
    display_messages()

if __name__ == "__main__":  # 파일을 직접 실행할 때만 True로 작동됨. 때문에 다른 파일에서 import로는 해당 if문은 False로 실행 안 됨. -> 함수/클래스만 재사용 가능.
    # 유저 ID와 파일 경로 설정
    user_id = "apple05"
    filename = f"messages_{user_id}.txt"

    # Tkinter 윈도우 생성
    root = tk.Tk()
    root.title("메세지 뷰어")

    # Text 위젯 생성
    text_widget = tk.Text(root, width=50, height=20)
    text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Scrollbar 생성
    scrollbar = tk.Scrollbar(root, command=text_widget.yview)   # 텍스트가 움직일 때 스크롤바 위치 업데이트
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    text_widget.config(yscrollcommand=scrollbar.set)    # 스크롤바를 움직이면 텍스트가 스크롤됨.
    text_widget.config(state=tk.DISABLED)   # 기본적으로 텍스트 잠금. 출력용이니까.

    # 메시지 불러오기
    load_messages()

    root.mainloop()
