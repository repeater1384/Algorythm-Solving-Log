import hashlib
result = hashlib.md5(input().encode()).hexdigest()
print(result)