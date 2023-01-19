from fastapi import FastAPI
from pycoingecko import CoinGeckoAPI

app = FastAPI()
cg = CoinGeckoAPI()

@app.get("/")
def read_root():
    data = cg.get_price(ids='bitcoin', vs_currencies='usd')
    return {"Bitcoin": data['bitcoin']['usd']}
