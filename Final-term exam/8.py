import random
engarr = ["apple","pencil","eraser","car","doll","clock"]
korarr = ["사과","연필","지우개","차","인형","시계"]
ran = random.randint(0,5)
print(f'영단어: {engarr[ran]}')
answer = input("의 한글을 입력하세요 : ")
if (answer == korarr[ran]):
    print("축하합니다!! 맞았습니다.")
else:
    print("틀렸습니다.")
    print(f'한글: {korarr[ran]}')
