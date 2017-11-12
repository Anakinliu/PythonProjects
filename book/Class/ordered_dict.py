from collections import OrderedDict

fav_game = OrderedDict()

fav_game['cs'] = 1.6
fav_game['ra'] = 2
fav_game['gta'] = 5
for name in fav_game.keys():
    print("my favorite game " + name)

for name, version in fav_game.items():
    print("my favorite game " + name + "'s version is " + str(version))
