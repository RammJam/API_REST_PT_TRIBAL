from fastapi import FastAPI
import requests

app = FastAPI()
ids = []

@app.get('/ids')
async def get_ids():
    global ids
    if len(ids) < 25:
        num_ids = 25 - len(ids)
        for _ in range(num_ids):
            o_id = None
            while True:
                response = requests.get('https://api.chucknorris.io/jokes/random')
                if response.status_code == 200:
                    data = response.json()
                    o_id = data['id']
                    if o_id not in [obj.get('id') for obj in ids]:
                        break
            ids.append({'id': o_id})
    return ids[:25]