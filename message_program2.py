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