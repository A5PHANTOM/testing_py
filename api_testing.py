# using async client 

import httpx
import asyncio

async def predict_age (name,retry=3):
  URL = "https://api.agify.io"
  params={'name':name}
  for i in range (retry):
  
    async with httpx.AsyncClient(timeout=1.0) as client:
        response = await client.get(URL,params=params)
    
        if response.status_code ==200:
            data=response.json()
            print("predicted age :", data['age'])
    
        else:
            return None

asyncio.run(predict_age("arjun"))
    




