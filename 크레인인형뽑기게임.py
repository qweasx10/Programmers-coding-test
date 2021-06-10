'''
프로그래머스 크레인인형뽑기게임
처음 상태가 
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
인 경우 결과값이 4가 된다.
문제의 요지는 인형을 뽑아서 한 곳에 쌓을 때 같은 인형인 경우 함께 사라지게 해야한다.

나는 2단계로 나누어서 풀었다. 
1. 인형을 뽑아서 스택에 쌓는다.
2. 스택에서 동일한 숫자를 삭제하고 삭제된 인형수만큼 결과값에 넣어서 리턴한다.
'''

def solution(board, moves):
    answer = 0
    b = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1]!=0:
                b.append(board[j][i-1])
                board[j][i-1]=0
                break#스택에 인형 쌓기
    k=1
    while k<len(b):
    
        if b[k-1] != b[k]:
            k+=1
        elif b[k-1]==b[k]:
            answer+=2
            del b[k-1]
            del b[k-1]
            k=1#같은 인형이 있는경우 제거해주기
    return answer
