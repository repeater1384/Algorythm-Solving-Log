for _ in range(int(input())):
    hp, mp, att, arm, dhp, dmp, datt, darm = map(int, input().split())
    hp += dhp
    mp += dmp
    att += datt
    arm += darm
    print(max(hp, 1) + max(mp, 1) * 5 + max(att, 0) * 2 + arm * 2)
