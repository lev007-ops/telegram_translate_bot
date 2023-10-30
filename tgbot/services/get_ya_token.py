import aiohttp
from tgbot.config import load_config


async def get_iam_token():
    url = "https://iam.api.cloud.yandex.net/iam/v1/tokens"
    oauth_token = load_config().misc.oauth_token
    headers = {
        "Content-Type": "application/json",
    }
    data = {
        "yandexPassportOauthToken": oauth_token
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            if response.status == 200:
                result = await response.json()
                return result.get("iamToken")
            else:
                print(f"Error {response.status}: {await response.text()}")
                return None
