def get_max(array):
    maxValue=0
    for num in array:
        if num>maxValue:
            maxValue=num
    return maxValue
def get_min(array):
    minValue=100
    for num in array:
        if num<minValue:
            minValue=num
    return minValue
def get_avg(array):
    sum_of_array=0;
    for num in array:
        sum_of_array+=num
        avg_array=sum_of_array/len(array)
    return avg_array

def get_info():
    name=input("이름: ")
    id=input("학번: ")
    midterm=float(input("중간고사 성적: "))
    final=float(input("기말고사 성적: "))
    homework=float(input("과제 성적: "))
    return [name,id,midterm,final,homework]

def compute_grade(total_score):
    if total_score>=90:
        return 'A'
    elif total_score>=80:
        return 'B'
    elif total_score>=70:
        return 'C'
    elif total_score>=60:
        return 'D'
    else:
        return 'F'

def print_info(student,total_score,grade):
    print("이름:",student[0], end='')
    print("\t학번:",student[1], end='')
    print("\t총점:",round(total_score,2), end='')
    print("\t학점:",grade)
    print("--------------------------------------------------")
#리스트 선언
student=[None]*5
n=int(input("학생수: "))
total_score=[1.1]*n
grade=['A']*n
midterm=[1.1]*n
final=[1.1]*n
homework=[1.1]*n

for i in range(n):
    student=get_info() #입력 함수 호출
    midterm[i]=student[2]
    final[i] =student[3]
    homework[i]=student[4]
    total_score[i]=student[2]*0.3+student[3]*0.4+student[4]*0.3 #총점 계산
    grade[i]=compute_grade(total_score[i])
    print_info(student,total_score[i],grade[i]) #출력 함수 호출

print("총점의 평균:",round(get_avg(total_score),2), end='')
print("\t최고점:",round(get_max(total_score),2), end='')
print("\t최저점:",round(get_min(total_score),2))
print("중간성적의 평균:",round(get_avg(midterm),2),end='')
print("\t최고점:",round(get_max(midterm),2),end='')
print("\t최저점:",round(get_min(midterm),2))
print("기말성적의 평균:",round(get_avg(final),2),end='')
print("\t최고점:",round(get_max(final),2),end='')
print("\t최저점:",round(get_min(final),2))
print("과제의 평균:",round(get_avg(homework),2),end='')
print("\t최고점:",round(get_max(homework),2),end='')
print("\t최저점:",round(get_min(homework),2))