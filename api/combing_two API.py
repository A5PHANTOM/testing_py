import httpx
import asyncio

async def predict_details(name):
    async with httpx.AsyncClient(timeout=5.0) as client:
       
        age_task = client.get("https://api.agify.io", params={'name': name})
        nation_task = client.get("https://api.nationalize.io", params={'name': name})

       
        age_res, nation_res = await asyncio.gather(age_task, nation_task)

        
        countries = nation_res.json().get('country', [])
        top_country = countries[0]['country_id'] if countries else "Unknown"

        return {
            "name": name,
            "age": age_res.json().get('age'),
            "country": top_country
        }

# To run it:
result = asyncio.run(predict_details('Arjun'))
print(result)