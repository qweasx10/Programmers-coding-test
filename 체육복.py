''' 
프로그래머스 체육복 문제
점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 
다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 
학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 
예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 
체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 
여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 
체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

풀이방법:
1. 각 배열을 정렬해 준다.
2. 일단 잃어버린 만큼 전체수에서 빼준다.
3. 서로 같은 값이 있는 경우 있는 만큼 전체수에서 더해준다.
4. lost와 reserve에 같은 요소를 지워주고 그 안에서 
for 문을 돌려서 앞뒤에 잃어버린 사람이 있으면 빌려주게 한다. 빌려준 만큼 전체수에서 더해준다.
느낀점:
많이 어려웠다. 
특히 잃어버린 사람과 챙겨온 사람의 중복을 처리 하는 게 가장 어려웠다.
'''

def solution(n, lost, reserve):
    answer = 0
    count = 0
    lost.sort()
    reserve.sort()
    n = n-len(lost)
    for i in lost:
        if i in reserve:
            count+=1
    n = n+count
    d = set(reserve)-set(lost)
    c = set(lost) - set(reserve)
    reserve = list(d)
    lost = list(c)
    
    for i in range(len(reserve)):
        if (reserve[i]-1) in lost or (reserve[i]+1) in lost:
            n+=1
            del lost[0]
            if len(lost)==0:
                break
            
            
    answer = n         
    return answer
