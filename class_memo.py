import tkinter as tk

class MessageViewer:
    def __init__(self, master, filename):       # 시작할 때 무조건 실행되는 함수
        self.master = master
        self.master.title("메세지 뷰어")
        self.filename = filename

        # 텍스트 위젯
        self.text_widget = tk.Text(master, width=50, height=20)     
        self.text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # 스크롤바
        self.scrollbar = tk.Scrollbar(master, command=self.text_widget.yview)   
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text_widget.config(yscrollcommand=self.scrollbar.set)
        self.text_widget.config(state=tk.DISABLED)

        self.messages = []
        self.load_messages()

    def load_messages(self):        # ❓무슨 목적으로 만든 기능이지? : load_message는 파일에서 메세지를 읽어와서 메세지 단위로 나누고([읽음]을 기준으로), 그걸 self.message에 저장하는 역할을 한다. (UI에 띄우기 위한 사전작업을 하는 함수)
        with open(self.filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        self.messages = []          # 전체 메시지를 모아두는 리스트. 이 안에 메시지 하나 하나가 들어감.
        current_message = []        # ❓왜 만든걸까? : 현재 메시지를 구성하는 줄들을 임시로 저장할 용도.

        for line in lines:      
            current_message.append(line)    # line을 하나씩 읽으면서 current_message에 추가. line.strip() == "[읽음]"이면: 하나의 메시지가 끝났다는 뜻이므로, 지금까지 모은 current_message를 self.messages에 넣고 current_message는 비워서 다음 메시지를 받을 준비.
            if line.strip() == "[읽음]":
                self.messages.append(current_message)
                current_message = []

        self.display_messages()     # 구분된 메시지들을 텍스트 위젯에 띄우는 함수.

    def display_messages(self):     # 함수의 역할: Text 위젯을 이용해서 여러 개의 메시지를 화면에 표시하고, 각 메시지마다 "삭제" 버튼을 함께 넣는 기능을 한다. 
        self.text_widget.config(state=tk.NORMAL)    
        # Text 위젯은 기본적으로 tk.DISABLED일 수 있음. 읽기 전용. 메시지를 삽입하려면 일시적으로 NORMAL 상태로 바꿔줘야 함.
        self.text_widget.delete("1.0", tk.END)      
        # Text 위젯에 이전에 출력된 내용을 모두 지움. "1.0"은 첫 번째 줄, 첫 번째 문자 위치부터 끝(tk.END)까지 전체 삭제.

        for index, message in enumerate(self.messages):     
            # enumerate를 써서 메시지의 인덱스(index)와 내용(message)을 함께 가져옴.(리스트 형태가 아니라 순서, 내용 쌍인 이터레이터를 생성.)
            
            start_index = self.text_widget.index(tk.INSERT)     
            # 현재 삽입 지점의 위치를 문자열 형태로 저장 (예: "2.0" = 2번째 줄, 0번째 문자). 후에 태그나 버튼 위치를 추적하기 위한 기준점.
            
            self.text_widget.insert(tk.END, ''.join(message))   
            # 메시지 리스트(message)를 문자열로 합쳐서 Text 위젯 끝에 추가함. 
            
            self.text_widget.insert(tk.END, "\n")   
            # 줄바꿈을 한 번 추가해서 메시지와 버튼 사이를 구분.

            tag = f"msg_{index}"    
            # msg_0, msg_1 등의 태그를 만들어서 메시지 시작 위치에 마크(mark)를 설정. (위치 추적이나 하이라이팅 등에 사용 가능.)
            
            self.text_widget.mark_set(tag, start_index) 
            # Text 위젯의 마크(mark)는 눈에 보이지 않는 "숨겨진 위치 표시자" 같은 것. 내부적으로 텍스트 내의 특정 위치를 기억해두는 역할. "insert"는 현재 커서 위치를 나타내는 마크이다. self.text_widget.mark_set을 사용하면, tag라는 이름으로 index 위치를 저장해둔다.
            
            self.text_widget.window_create(tk.END, window=tk.Button(self.text_widget, text="삭제", command=lambda i=index: self.delete_message(i)))     
            # window_create는 Text 위젯에 일반 위젯(Button 등)을 삽입할 때 사용. lambda는 현재 메시지의 인덱스를 기억하는 콜백 함수를 생성. (lambda에서 index를 직접 쓰지 않고 i=index로 한 이유는 클로저 문제 방지(모든 버튼이 마지막 index를 공유하지 않도록).)   # 콜백 함수는 다름 함수에 인자로 넘겨지고, 특정 시점에 "호출"되는 함수.
            
            self.text_widget.insert(tk.END, "\n\n")

        self.text_widget.config(state=tk.DISABLED)

    def delete_message(self, index):    # 기능 요약: index에 해당하는 메시지를 self.message에서 삭제하고 파일(self.filenmae)을 새로 덮어쓴 다음, 화면의 메시지 목록을 새로고침(self.display_message())한다.
        del self.messages[index]
        with open(self.filename, 'w', encoding='utf-8') as f:
            for message in self.messages:
                f.writelines(message)
        self.display_messages()

if __name__ == "__main__":
    user_id = "apple05"
    filepath = f"messages_{user_id}.txt"

    root = tk.Tk()
    viewer = MessageViewer(root, filepath)
    root.mainloop()