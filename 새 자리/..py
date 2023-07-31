### 시퀀스 내장 함수 ###

# 1. enumerate
# 리스트에 저장된 요소와 해당 요소의 인덱스가 튜플형태로 함께 추출

# for iten in enumerate([리스트]):
# 반복 실행문

for item in enumerate(['가위', '바위', '보']):
    print()

    # (2, '보')

    # 2. range() 함수
    # 숫자 리스트를 생성하는데 사용
    # 주로 for 반복문에서 사용, 일정한 간격의 숫자 시퀀스를 생성 가능

    # range(stop): 0부터 stop-1까지의 정수를 반환
    for i in range(5):
        print(i)

    # range(start, stop): start ~ stop-1
    for i in range(1, 5):
        print(i)

    # range(start, stop, step): start ~ stop-1, step 간격으로 반환
    for i in range(0, 10, 2):
        print(i)

    # 3. len() 함수
    # : 컨테이너에 있는 원소의 개수를 반환
    # : 리스트, 튜플, 문자열, 딕셔너리

    # len(s): s의 원소 개수를 반환

    my list = [1, 2, 3, 4, 5]
    print(len(my list))