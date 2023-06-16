import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Enter your Google Custom Search JSON API key and search engine ID
API_KEY = 'AIzaSyDHJmHmjL7z9ebcNWMA5DopoH_eKRDVIKs'
SEARCH_ENGINE_ID = 'a26af9772e68f478b'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    results = []

    if query:
        # Perform search using Google Custom Search JSON API
        params = {
            'key': API_KEY,
            'cx': SEARCH_ENGINE_ID,
            'q': query,
        }
        response = requests.get('https://www.googleapis.com/customsearch/v1', params=params)
        
        if response.status_code == 200:
            data = response.json()
            if 'items' in data:
                for item in data['items']:
                    result = {
                        'title': item['title'],
                        'link': item['link'],
                        'snippet': item['snippet']
                    }
                    results.append(result)

    return render_template('search.html', query=query, results=results)

@app.route('/about')
def about():
    return render_template('about.html')

# Other routes for different pages

if __name__ == '__main__':
    app.run(debug=True)
