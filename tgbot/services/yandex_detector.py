import aiohttp
from tgbot.config import load_config

target_language = 'tt'
endpoint = "https://translate.api.cloud.yandex.net/translate/v2/detect"


async def ya_detect(text: str):
    config = load_config()
    iam_token = config.misc.iam_token
    folder_id = config.misc.folder_id

    body = {
        "text": text,
        "languageCodeHints": [
            "ru", "tt"
        ],
        "folderId": folder_id
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {iam_token}"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(endpoint, json=body, headers=headers
                                ) as response:
            if response.status != 200:
                return False
            response_json = await response.json()
            return response_json["languageCode"]
            
