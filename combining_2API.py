import httpx
import asyncio


async def fetch_with_retry(url, params, retries=3):
    async with httpx.AsyncClient(timeout=2.0) as client:
        for attempt in range(1, retries + 1):
            try:
                response = await client.get(url, params=params)

                if response.status_code == 200:
                    return response.json()
                else:
                    print(f"Attempt {attempt}: API error {response.status_code}")

            except httpx.RequestError:
                print(f"Attempt {attempt}: Network error")

            if attempt < retries:
                await asyncio.sleep(1)

    return None


async def get_profile(name):
    age_url = "https://api.agify.io"
    nation_url = "https://api.nationalize.io"

    age_data = await fetch_with_retry(age_url, {"name": name})
    nation_data = await fetch_with_retry(nation_url, {"name": name})

    profile = {
        "name": name,
        "age": age_data.get("age") if age_data else None,
        "country": None
    }

    if nation_data and nation_data.get("country"):
        profile["country"] = nation_data["country"][0]["country_id"]

    return profile


result = asyncio.run(get_profile("Rohith"))
print(result)
