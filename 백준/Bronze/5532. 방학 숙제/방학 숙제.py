day = int(input())
korean = int(input())
math = int(input())
canKorean = int(input())
canMath = int(input())

print(day - max((korean - 1) // canKorean + 1, (math - 1) // canMath + 1))
