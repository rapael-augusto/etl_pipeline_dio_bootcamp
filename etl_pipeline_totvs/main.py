import pandas as pd
import requests
import json
import ollama

def get_user(id):
    response = requests.get(f'http://127.0.0.1:8000/users/{id}')
    return response.json() if response.status_code == 200 else None

def generate_ai_news(user):
    response = ollama.chat(model='tinyllama', messages=[
        {
            'role': 'system',
            'content': 'Você é um especialista em marketing bancário.',
        },
        {
            'role': 'user',
            'content': f"Crie uma mensagem pro usuário {user['name']} sobre a importância dos investimentos (lembre-se, máximo de 100 caracteres)",
        }
    ])
    return response['message']['content'].strip('\"')

def update_user(user):
    response = requests.put(f'http://127.0.0.1:8000/users/{user['id']}', json=user)
    return True if response.status_code == 200 else False

df = pd.read_csv('users.csv')
users_id = df['UserID'].tolist()

users = [user for id in users_id if (user := get_user(id)) is not None]

for u in users:
    news = generate_ai_news(u)
    u['news'].append({
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": news
    })

for u in users:
    success = update_user(u)
    print(f"User {u['name']} updated? {success}")