import requests
import pyperclip

#Function to fecth a random quote from the API
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

#Function to display the menu
def displayMenu():
    print('\n Welcome to the Quote Generator written in Python')
    print('\n 1. Generate a new random quote')
    print('\n 2. Copy the quote to clipboard')
    print('\n 3. Exit')

#Main application function
def runQuoteGenerator():
    currentQuote = None

    while True:
        displayMenu()
        choice = input('Choose an option (1-3): ')

        if choice == '1':
            currentQuote = fetchRandomQuote()
            if currentQuote:
                print(f'Quote: {currentQuote['quotes']}')
                print(f'Quote: {currentQuote['quotes']}')
            