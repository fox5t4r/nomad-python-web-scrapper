from requests import get

websites = (
    'https://google.com',
    'airbnb.com',
    'twitter.com',
    'facebook.com',
    'tictok.com'
)

for website in websites:
    if not website.startswith('https://'):
        website = f'https://{website}'
    print(website)