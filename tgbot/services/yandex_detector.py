import aiohttp
from tgbot.config import load_config

target_language = 'tt'
endpoint = "https://translate.api.cloud.yandex.net/translate/v2/detect"


async def ya_detect(text: str, iam_token: str):
    config = load_config()
    folder_id = config.misc.folder_id

    body = {
        "text": text,
        "languageCodeHints": [
            "ru", "tt", "en"
        ],
        "folderId": folder_id
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {iam_token}"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(endpoint, headers=headers, json=body) as response:
            if response.status == 200:
                result = await response.json()
                return result["languageCode"]
            print(f"Error {response.status}: {await response.text()}")
