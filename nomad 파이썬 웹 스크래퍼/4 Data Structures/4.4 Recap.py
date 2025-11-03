print('nice'.upper())

num = [1, 2, 3, 'four', 'five']
print(num)
num.append(6)
print(num)
num.append([7, 8])
print(num)
print(num[-3])

numb = (1, 2, 3)
print(numb[1])

player = {
    'name' : 'nice',
    'age' : 12,
    'fav_food' : ('apple'),
    'frieds' : {
        'name' : 'lin',
        'fav_food' : ['snake']
    }
}
print(player)
player['fav_food'] = 'banana'
print(player)
player.pop('age')
print(player)
player['frieds']['fav_food'].append('apple')
print(player)