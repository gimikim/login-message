# # 내가 보낸 메시지 함수

# # 파일을 생성한다. 'w'

# def send_message():
#     from datetime import datetime
#     now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
#     with open('users.txt', 'r',encoding="UTF-8") as f:
#         lines = [line.strip() for line in f.readlines()]
    
#     def submit_send():
#         receiver_id = receiver_entry.get()  # 입력창 내용을 가져온다.(수신자, 메세지 내용)
        
#         for j in range(1, len(lines), 4):   
#             if receiver_id == lines[j]:
#                 break
#         else:
#             mbox.showerror("오류", "존재하지 않는 ID입니다.")   # ❗break 다음에 성공인데도 오류 메시지가 뜨게 됨. 
#             return  # return 쓰는 게 맞을까?
        
#         content = text.get("1.0", "end-1c") # 1.0: 첫 행 0번째 문자. 1c: 문자 한 개. 안빼면 다음 줄까지 포함됨.
        
#         # 작성하기
#         with open(f'messages_{receiver_id}.txt', 'a',encoding="UTF-8") as f:     # 'w': 없으면 만들고, 기존 내용에 덮어씀. 'a': 추가 모드, 기존 내용 뒤에 이어씀.
#             f.writelines(f"[{now}] {user_id}: {content}\n") 
        
#         with open(f'sent_messages.txt', 'a', encoding="UTF-8") as f:
#             f.writelines(f"[{now}] 보낼 사람: {receiver_id} | {content}\n")
    
#         mbox.showinfo("알림", f"{receiver_id}에게 메세지가 전송되었습니다.")
        
#         send_message_window.destroy()
        
#         # 메시지 보낼 때, 파일 만들면 되잖아.