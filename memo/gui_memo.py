# # 메세지 삭제하기_GUI
# # 메세지 삭제하기를 들어가면, 받은 메세지 창을 띄워주고, 
# # 메세지마다 "삭제" 버튼을 아래에 두고, 누르면 메세지가 삭제되도록.


# # 메시지 삭제_not GUI
# def delete_message(my_id):   
#     with open(f'messages_{my_id}.txt','r',encoding="UTF-8") as f:
#         lines = f.read()    # read()로 읽으면 입력한 그대로 한 줄씩 나옴. readlines()로 읽으면 리스트 형태로 한 줄씩 구분되어 출력됨.(\n포함)
        
#         while True:
#             date = input("삭제하고자 하는 메시지의 날짜, 시간을 복사해서 붙여넣으세요(붙여넣기를 할 때 '우클릭'을 활용해주세요.): ")
            
#             if len(date) < 19:
#                 print("올바르지 않은 입력입니다. 날짜와 시간을 '모두' 복사, 붙여넣기 해주세요.")
#                 continue    # 다시 입력 받도록 루프 처음으로 돌아감.
                        
#             start_location = lines.find(date) - 1     # 삭제하려는 메시지의 첫 인덱스

#             if start_location == -1:
#                 print("해당 날짜에 받은 메시지가 없거나 올바르지 않은 입력입니다.")
#                 continue
            
#             break

#         if lines.find("[읽음]",start_location+1) != -1:
#             end_location = lines.find("[읽음]",start_location+1) + 6
#         else:
#             end_location = lines.find("[끝]",start_location+1) + 5    
    
    
#     lines = lines[:start_location] + lines[end_location:]       # practice13
    
#     with open(f'messages_{my_id}.txt','w',encoding="UTF-8") as f:
#         f.write(lines)  # 'w'라서 덮어쓰기 됨.