age = int(input('how old r u?'))

if age < 18:
    print('you can\'t enter!')


elif age >= 18 and age <= 35:
    print('you drink beer!')

elif age > 35 and age <= 60:
    print('bang bang')

elif age == 65 or age == 75:
    print('god god god')

elif age == 70 or age == 80:
    print('happy birthday!')

else:
    print('go ahead!')