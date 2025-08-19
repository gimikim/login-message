# if message_function_activated:
# else:
#     print("메시지 기능이 비활성화돼 있습니다. 로그인을 해주세요.")


# 로그인 창에서
# global message_function_activated         # 로그인 완료되어야 넘어가는 거면 activated = True 필요없음.
# message_function_activated = True   # 메시지 기능 활성화


# from datetime import datetime   
# now = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 

# print(now, type(now))   # -> str

##
# import os
# print(os.getcwd())

# # practice12
# import sys

# print("메시지 내용을 입력하세요 (입력 종료: Ctrl+Z + Enter):")
# content = sys.stdin.readlines()  # ✅ 인자 없이 사용해야 함
# # readlines()는 리스트를 반환해 (['첫 줄\n', '둘째 줄\n'] 이런 형태).
# print("입력 결과:")
# print("".join(content))     # 리스트 안의 여러 문자열을 하나의 문자열로 연결. join을 써서 리스트를 하나의 문자열로 합침. 문장 끝마다 \n이 있어서 ""빈 문자열로 합쳐도 괜찮아.

##
# practice13
# del lines[start_location : end_location]    슬라이싱 해서 다시 합치면 덮어쓰기 됨(수정하지 않고 특정 영역 선택해서 재할당 -> 덮어쓰기).
# str은 immutable이라 del로 삭제 불가능. mutable(변경하기 쉬운)
# mutable은 리스트나 딕셔너리 같은 객체


# input은 입력 받은 문자열에서 \n을 제거해서 반환함. 때문에 enter를 누르면 실제로는 \n이 입력되지만 input이 자동으로 제거해서 나중에는 '' 빈 문자열이 입력된다.

# print(len('[2025-06-22 22:09:51]')) # 21
# print(len('[2025-06-22 2209:51]'))  # 20
# print(len('[2025-06-22 22:09:51'))  # 20


x = 10
def foo():
    global x
    print(x)
    x += 1

foo()
foo()