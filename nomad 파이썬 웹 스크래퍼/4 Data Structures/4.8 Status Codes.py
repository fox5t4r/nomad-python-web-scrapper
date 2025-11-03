from requests import get

websites = (
    'https://google.com',
    'airbnb.com',
    'twitter.com',
    'facebook.com',
    'tictok.com'
)

results = {}

for website in websites:
    if not website.startswith('https://'):
        website = f'https://{website}'
    resonse = get(website)

    if resonse.status_code == 200:
        results[website] = 'OK'
        print(f'{website} is okay.')
    else:
        print(f'{website} isn\'t okay.')
        results[website] = 'FAILED'

print(results)