for _ in [0]*int(input()):
	a,b=int(input()),0
	while a:
		if a%2:print(b,end=' ')
		a//=2;b+=1