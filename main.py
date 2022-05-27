from fastapi import FastAPI
from models.requests_data import RequestBody
from BtxClient import BtxClient
from Settings.config import btx_webhook

app = FastAPI()


@app.post('/add_order')
def add_order(r: RequestBody):
    client = BtxClient(btx_webhook)
    c_id = client.create_contact(r.contact)
    client.create_deal(r.deal, c_id)
    return {'test': 'Hello'}
