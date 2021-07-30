import random

com = random.randint(1,3)
while True:
     user = int(input('1 2 3 내세요>>>'))
     if com < user:
         print('{}! 당신이 이겼습니다.'.format(com))
         break
     if com > user:
         print('{}! 컴퓨터가 이겼습니다. 다시 시도하세요.'.format(com))
     else:
         print('비겼습니다. 다시 시도하세요') 
