import os
import requests

TOKEN = os.getenv("TOKEN")
HEADERS = {'Authorization': f'Bearer {TOKEN}'}

def get_pull_requests(state):
    url = "https://api.github.com/repos/boto/boto3/pulls"
    params = {
        'state': state,
        'per_page': 100
    }
    
    response = requests.get(url, headers=HEADERS, params=params)
    
    
    response.raise_for_status()
    
    pr_data = response.json()
    
    pull_requests = []
    for pr in pr_data:
        pull_requests.append({
            'title': pr['title'],
            'num': pr['number'],
            'link': pr['html_url']
        })
    
    return pull_requests
