from flask import Flask, render_template
import sqlite3
import requests
from datetime import datetime

app = Flask(__name__)

def create_github_table():
    conn = sqlite3.connect('github_data.db')
    cursor = conn.cursor()

    # Create the table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS github_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            repository_name TEXT,
            owner_login TEXT,
            stargazers_count INTEGER
        )
    ''')

    conn.commit()
    conn.close()

def get_github_data(api_url):  # Pass the API URL as an argument
    create_github_table()  # Ensure the table is created before attempting to insert data

    response = requests.get(api_url)  # Use the passed API URL

    if response.status_code == 200:
        data = response.json().get('items', [])

        conn = sqlite3.connect('github_data.db')
        cursor = conn.cursor()

        # Insert data into the database
        for item in data:
            cursor.execute('''
                INSERT INTO github_data (repository_name, owner_login, stargazers_count)
                VALUES (?, ?, ?)
            ''', (item['full_name'], item['owner']['login'], item['stargazers_count']))

        conn.commit()
        conn.close()

        print(f'{datetime.now()} - GitHub data successfully retrieved and stored.')
    else:
        print(f'Error: Unable to fetch data from GitHub API. Status Code: {response.status_code}')

# Schedule data retrieval (e.g., every 24 hours)
github_api_url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
get_github_data(github_api_url)

# Define a route to display GitHub data
@app.route('/')
def index():
    conn = sqlite3.connect('github_data.db')
    cursor = conn.cursor()

    # Retrieve data from the database
    cursor.execute('SELECT * FROM github_data')
    data = cursor.fetchall()

    conn.close()

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

