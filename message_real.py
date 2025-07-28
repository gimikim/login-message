# 메뉴1 정의
def main_menu1():
    print("""
===<< 회원가입/로그인 >>===
    1. 회원가입 하기
    2. 로그인 하기
    3. 종료하기
          """)
    global a
    a = input("원하는 숫자를 입력해주세요: ")
    return a


# 메뉴2 정의
def menu2(my_id):    
    while True:
        print("""
==== << menu >> ====       
1. 메시지 보내기 
2. 받은 메시지 확인 
3. 메시지 삭제    
4. 나가기
            """)   
        # global b
        b = input("원하는 숫자를 입력해주세요: ")
        # print_menu2(my_id)   -> 메뉴2 출력하기는 맨 아래에 정의돼 있어서 안 됨.
        # return b        # 여기서 메뉴2 출력하기로 넘어가지 않을 것 같다. 확인해보자. 
                        
        if b == "1":
            print("메시지 보내기")
            send_message(my_id)   # 위치 인자로는 구조상 작동이 안돼서 키워드 인자를 사용해야 하나? 키워드 인자는 내가 이전에 함수에서 반환한 값이랑 이름이 같으면 그 내용(할당된 값) 그대로 받아오나? (그냥 연결되지는 않음. 이름이 같고 변수에 저장해서 넘기면 OK)
        elif b == "2":
            print("받은 메시지 확인")
            check_message(my_id)
        elif b == "3":
            print("메시지 삭제")
            delete_message(my_id)
        elif b == "4":
            print("프로그램을 종료합니다.")
            exit()   # break 대신 exit()를 해야 메뉴1도 벗어나지 않을까 싶음
        else:
            print("올바르지 않은 입력입니다. 다시 입력해주세요.")



# 회원 가입(사용자 정보를 파일에 저장)
def sign_up():     
    while True:
        try:
            with open('users.txt','r',encoding="UTF-8") as f:
                file = f.read()     # try문에서 선언한 변수는 함수 전체에서 사용가능. 단, 오류가 나서 except로 가면 사용x. UnlocalError 
        except FileNotFoundError:   # 파일이 없는 경우
            with open('users.txt','x') as f:    # 생성만 한다.  'x'모드는 파일이 이미 있는 경우 FileExistsError가 뜸.
                pass    # 빈 블록을 임시로 채울 때 사용. wtih에서 들여쓰기가 꼭 필요하기 때문.
                file = ""   # try문을 건너띄고 except로 오면 file 변수에 값을 할당하지 않았기 때문에 선언해줌.
                
        nickname = input("닉네임: ")    # 닉네임 입력
        if nickname not in file:
            print('사용 가능한 닉네임입니다.')
            
            id = input("ID: ")  # 아이디, 비번 입력
            password = input("Password: ")
                
            if id not in file:
                print('회원가입이 완료되었습니다.')
                break
            else:
                print("이미 존재하는 아이디입니다. 다시 입력해주세요.")
        else:
            print("이미 존재하는 닉네임입니다. 다시 입력해주세요.")
            

            
    with open('users.txt','a',encoding="UTF-8") as f:       # f는 파일객체 이름. f=open(filename, 'w'): f.close() 수동으로 호출, with open() as f는 자동으로 f.close() 호출  
        f.write(nickname + "\n")      # 그냥 저장하면 줄바꿈 없이 저장돼 구분 어려움
        f.write(id + "\n")             # 문자열만 입력 가능. f.wrtie()은 쓴 글자 수를 반환한다.
        f.write(password + "\n\n")
        
    global my_id
    my_id = id
    return my_id
    
    
# message_function_activated = False  # 로그인 전: 메시지 기능 비활성화       # 얘를 회원가입 함수 안에 넣어야 하는지 의문임.

# 로그인(정보 파일에서 검증)
def sign_in():
    print("""
==================
로그인을 해주세요.
==================
          """)
    with open('users.txt', 'r',encoding="UTF-8") as f:
        lines = [line.strip() for line in f.readlines()]         # readline: 한 줄씩 읽는다, readlines: 전체 줄을 한 번에 읽어서 리스트로 반환, 각 줄은 리스트의 원소로 들어가고, 둘 다 \n 포함됨.

    id_found = False

    while True:
        id_input = input("ID: ")
        password_input = input("Password: ")
        
        for i in range(0, len(lines), 4):   # 닉네임, 아이디, 비번, 공백, ...반복
            nickname = lines[i]
            user_id = lines[i+1]
            user_password = lines[i+2]
            
            if id_input == user_id:
                id_found = True
                if password_input == user_password:
                    print(f"{nickname}님, 로그인되셨습니다.")
                    global my_id
                    my_id = user_id
                    return my_id  # 함수를 즉시 종료. 값이 있다면 값 반환.  break는 반복문 탈출

        if not id_found:    # not Flase -> True   # 따로 분리시키는 이유: 일치하지 않는 경우, 순회할 때마다 오류 메시지 출력하기 때문
            print("아이디가 틀렸습니다.")
        else:
            print("비밀번호가 틀렸습니다.")



# [기능 2] 메시지 보내기
def send_message(my_id):  
    from datetime import datetime   # import 모듈: 모듈 전체를 가져오는 것, from 모듈 import 이름: 모듈 내에서 필요한 것만 가져온다.
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 메세지 보내기 안에 넣지 않으면, 로그아웃을 했다가 다시 들어오기 전까지 고정된 시간을 이용.
    
    with open('users.txt', 'r',encoding="UTF-8") as f:
        lines = [line.strip() for line in f.readlines()]
    
    while True:
        receiver_id = input("수신자ID를 입력하세요: ")
        id_found = False

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

# [기능 3] 받은 메시지 확인
def check_message(my_id):     
    try:
        with open(f'messages_{my_id}.txt','r',encoding="UTF-8") as f:
            content = f.read()    # read()는 파일 전체를 한꺼번에 읽어버림. 파일 포인터가 끝으로 이동해서 더 이상 읽을 게 없음.
            print(content)    # "받음 메시지함" 보여주기
            
        with open(f'messages_{my_id}.txt','r',encoding="UTF-8") as f:
            lines = f.readlines()
            
        new_lines = []
        for line in lines:
            if '[끝]' in line and '[읽음]' not in line:
                # new_lines.append('[읽음]\n')
                line = line.replace("[끝]", "[읽음]")    
                new_lines.append(line)  # append는 줄바꿈 문자 포함하지 않음. 때문에 직접 넣어주기
            else:
                new_lines.append(line)
 
                
        # 파일 덮어쓰기
        with open(f'messages_{my_id}.txt', 'w', encoding='utf-8') as f:
            f.writelines(new_lines)     # wrtielines(리스트)는 문자열로 된 리스트를 파일에 저장함. (여러 줄을 한꺼번에 파일에 쓰는 기능, 줄바꿈은 자동으로 추가되지 않으니 직접 추가해야 됨.) 
                                                # f"{new_lines}\n"와의 차이?
    except FileNotFoundError:
        print("아직 누구에게도 받은 메시지가 없습니다.")
                        

    
    
# [기능 4] 메시지 삭제
def delete_message(my_id):   
    with open(f'messages_{my_id}.txt','r',encoding="UTF-8") as f:
        lines = f.read()    # read()로 읽으면 입력한 그대로 한 줄씩 나옴. readlines()로 읽으면 리스트 형태로 한 줄씩 구분되어 출력됨.(\n포함)
        
        while True:
            date = input("삭제하고자 하는 메시지의 날짜, 시간을 복사해서 붙여넣으세요(붙여넣기를 할 때 '우클릭'을 활용해주세요.): ")
            
            if len(date) < 19:
                print("올바르지 않은 입력입니다. 날짜와 시간을 '모두' 복사, 붙여넣기 해주세요.")
                continue    # 다시 입력 받도록 루프 처음으로 돌아감.
                        
            start_location = lines.find(date) - 1     # 삭제하려는 메시지의 첫 인덱스

            if start_location == -1:
                print("해당 날짜에 받은 메시지가 없거나 올바르지 않은 입력입니다.")
                continue
            
            break

        if lines.find("[읽음]",start_location+1) != -1:
            end_location = lines.find("[읽음]",start_location+1) + 6
        else:
            end_location = lines.find("[끝]",start_location+1) + 5    
    
    
    lines = lines[:start_location] + lines[end_location:]       # practice13
    
    with open(f'messages_{my_id}.txt','w',encoding="UTF-8") as f:
        f.write(lines)  # 'w'라서 덮어쓰기 됨.
    
        
        
        
# 메뉴1 출력하기
while True:
    show_menu1 = main_menu1()
    if a == "1":
        sign_up()
        menu2(my_id)   
    elif a == "2":
        sign_in()   # 그냥 sign_in()만 쓰면 while이기 때문에 로그인 하고나서 다시 반복해서 메뉴1로 넘어감. 메뉴2로 넘어가려면 로그인해서 받은 반환값으로 메뉴2를 호출해야 함.
        menu2(my_id)
    elif a == "3":
        print("프로그램을 종료합니다.")
        break
    else:
        print("올바르지 않은 입력입니다. 다시 입력해주세요.")




