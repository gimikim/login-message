# 작성일: 2025.06.19
from datetime import datetime

# 메인화면 출력용 함수
def main_menu():
    print("""
==== 메인메뉴 ====
1. 글 작성하기 
2. 글 확인하기
3. 글 수정하기 
4. 글 지우기
5. 끝내기
          """)
    a = input("원하는 숫자를 입력하세요: ")
    return a

# 1. 글 작성하기 함수
def write_doc():
    writer = input("작성자: ")
    title = input("제목: ")
    print("글 내용 입력: ")
    
    lines = ""
    line = ""   # 또는 line = input()
    while line != "끝":
        line = input()
        lines += line    
    
    # 자동으로 현재 시점을 파일명으로 저장하기
    filename = f".txt"
    
    f = open(filename, "w")
    f.write(writer + "\n")      # 그냥 저장하면 줄바꿈 없이 저장돼 구분 어려움
    f.write(title + "\n")
    f.write(lines + "\n")
    f.close()
    
    
# 메인메뉴 출력하기
while True:
    menu_num = main_menu()      # 자주 사용되는 부분은 함수로 만들면 편리_재사용

    if menu_num == "1":
        write_doc()
    elif menu_num == "2":
        print("hello")
    elif menu_num == "3":
        print("modify_doc()")
    elif menu_num == "4":
        print("remove_doc()")
    elif menu_num == "5":
        break
    else:
        print("잘못된 번호를 입력했습니다. 다시 입력해주세요.")