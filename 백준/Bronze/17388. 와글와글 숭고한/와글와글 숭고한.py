s,k,h = map(int,input().split())
if s+k+h>=100:
    print('OK')
else:
    if s<k and s<h:print('Soongsil')
    if k<s and k<h:print('Korea')
    if h<s and h<k:print('Hanyang')