antenna = int(input())
eye = int(input())

possible_alien = []

if antenna >= 3 and eye <= 4:
    possible_alien.append('TroyMartian')
if antenna <= 6 and eye >= 2:
    possible_alien.append('VladSaturnian')
if antenna <= 2 and eye <= 3:
    possible_alien.append('GraemeMercurian')

for alien in possible_alien:
    print(alien)