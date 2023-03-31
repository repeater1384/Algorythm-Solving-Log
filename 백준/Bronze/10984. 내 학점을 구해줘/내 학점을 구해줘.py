for _ in range(int(input())):
    gpa=0
    grade=0
    for _ in range(int(input())):
        a,b=map(float,input().split())
        gpa+=a*b
        grade+=a
    print(int(grade),'%.1f'%(gpa/grade))