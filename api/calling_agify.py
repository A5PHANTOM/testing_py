import httpx
import asyncio

async def predict_age(name,retries=3):
    url =  "https://api.agify.io"
    params ={"name":name}
    async with  httpx.AsyncClient(timeout=2.0) as client :

        for i in range (1,retries+1):
            try :
                 response = await client.get(url,params=params)


                 if response.status_code == 200 :
                    data =response.json()
                    print("predicted_age_is :",data.get("age"))
        
                 else:
                    return None
                 
            except httpx.RequestError as e :
                print("Network error")

            if i < retries :
                await asyncio.sleep(1)      
    return None  


age = asyncio.run(predict_age("Rohith"))
print("Predicted age:", age)


    
