'''
프로그래머스 키패드누르기 문제

풀이
[1,4,7]일때는 L
[3,6,9]일때는 R
나머지인 경우 거리와 손잡이에 따라 결정하였다.
딕셔너리를 썼다면 더 짧게 풀었겠지만 몰라서 거리를 계산하는 함수를
모든 경우의 수를 다계산해서 풀었다.
'''
def distance(x,y):
    dis = 0
    if x==1 and y==2:
        dis=1
    elif x==4 and y==2:
        dis=2
    elif x==7 and y==2:
        dis=3
    elif x=='*' and y==2:
        dis=4
    elif x==3 and y==2:
        dis=1
    elif x==6 and y==2:
        dis=2
    elif x==9 and y==2:
        dis=3
    elif x=='#' and y==2:
        dis=4
    elif x==2 and y==2:
        dis=0
    elif x==5 and y==2:
        dis=1
    elif x==8 and y==2:
        dis=2
    elif x==0 and y==2:
        dis=3
    elif x==1 and y==5:
        dis=2
    elif x==4 and y==5:
        dis=1
    elif x==7 and y==5:
        dis=2
    elif x=='*' and y==5:
        dis=3
    elif x==3 and y==5:
        dis=2
    elif x==6 and y==5:
        dis=1
    elif x==9 and y==5:
        dis=2
    elif x=='#' and y==5:
        dis=3
    elif x==2 and y==5:
        dis=1
    elif x==5 and y==5:
        dis=0
    elif x==8 and y==5:
        dis=1
    elif x==0 and y==5:
        dis=2
    elif x==1 and y==8:
        dis=3
    elif x==4 and y==8:
        dis=2
    elif x==7 and y==8:
        dis=1
    elif x=='*' and y==8:
        dis=2
    elif x==3 and y==8:
        dis=3
    elif x==6 and y==8:
        dis=2
    elif x==9 and y==8:
        dis=1
    elif x=='#' and y==8:
        dis=2
    elif x==2 and y==8:
        dis=2
    elif x==5 and y==8:
        dis=1
    elif x==8 and y==8:
        dis=0
    elif x==0 and y==8:
        dis=1
    elif x==1 and y==0:
        dis=4
    elif x==4 and y==0:
        dis=3
    elif x==7 and y==0:
        dis=2
    elif x=='*' and y==0:
        dis=1
    elif x==3 and y==0:
        dis=4
    elif x==6 and y==0:
        dis=3
    elif x==9 and y==0:
        dis=2
    elif x=='#' and y==0:
        dis=1
    elif x==2 and y==0:
        dis=3
    elif x==5 and y==0:
        dis=2
    elif x==8 and y==0:
        dis=1
    elif x==0 and y==0:
        dis=0
    return dis
    
    
def solution(numbers, hand):
    answer = ''
    Lh = '*'
    Rh = '#'
    for i in numbers:
        if i in [1,4,7]:
            answer+='L'
            Lh = i
        elif i in [3,6,9]:
            answer+='R'
            Rh = i
        elif i in [2,5,8,0]:
            if distance(Lh,i)>distance(Rh,i):
                answer+='R'
                Rh = i
            elif distance(Lh,i)<distance(Rh,i):
                answer+='L'
                Lh = i
            elif distance(Lh,i)==distance(Rh,i):
                if hand == 'left':
                    answer+='L'
                    Lh=i
                else:
                    answer+='R'
                    Rh=i
            
                
            
    return answer
