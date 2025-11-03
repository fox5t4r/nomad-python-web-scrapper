from requests import get

websites = (
    'https://google.com',
    'airbnb.com',
    'twitter.com',
    'facebook.com',
    'tictok.com',
    'random.com',
    'error.com'
)

results = {}

for website in websites:
    if not website.startswith('https://'):
        website = f'https://{website}'
    resonse = get(website)

    if 200 > resonse.status_code >= 100:
        results[website] = 'CONTINUE'
        print(f'{website} CONTINUE.')

    elif 300 > resonse.status_code >= 200:
        results[website] = 'OK'
        print(f'{website} OK.')

    elif 400 > resonse.status_code >= 300 :
        print(f'{website} REDIRECTED.')
        results[website] = 'REDIRECTED'

    elif 500 > resonse.status_code >= 400 :
        print(f'{website} FAILED.')
        results[website] = 'FAILED'

    elif 600 > resonse.status_code >= 500 :
        print(f'{website} ERROR.')
        results[website] = 'ERROR'

print(results)