player = {
    'name' : 'nico',    
    'age' : 12,
    'alive' : True,
    'fav_food' : ['pizza', 'burger']
}

print(player)

print(player.get('name'))

print(player.get('fav_food'))

print(player['alive'])

print(player.pop('age'))

print(player)

player['xp'] = 1500

print(player)

player['fav_food'].append('noodle')

print(player.get('fav_food'))

print(player['fav_food'])