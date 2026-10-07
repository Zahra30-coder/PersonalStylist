import httpx

async def get_weather():

    async with httpx.AsyncClient() as client:

        response = await client.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": 23.25,
                "longitude": 77.41,
                "current_weather": True
            }
        )

        return response.json()