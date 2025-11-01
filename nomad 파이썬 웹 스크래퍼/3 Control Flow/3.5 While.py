from time import sleep

distance = 0

while distance < 20:
    print('I am running -', distance, 'km')
    distance = distance + 1
    sleep(0.3)