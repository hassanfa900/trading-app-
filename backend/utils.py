import aiohttp

async def fetch_twelvedata_quote(symbol: str, api_key: str):
    url = f"https://api.twelvedata.com/quote?symbol={symbol}&apikey={api_key}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()

