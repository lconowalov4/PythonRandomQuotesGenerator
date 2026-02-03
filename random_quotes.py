import requests
import pyperclip

#function to fecth a random quote from the API
def fetchRandomQuote():
    try:
        response = requests.get('https://api.quotable.io/random')
        if response.status_code == 200:
            data = response.json()
            return {'quotes':data['content'], 'author': data['author']}
        else:
            print('Error fetching quote. Try again later')
            return None
    except requests.exceptions.RequestException as e:
        print(f'An error occured: {e}')
        return None