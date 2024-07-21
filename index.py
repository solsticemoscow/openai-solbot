import json
from app_bot_ya import BOT, DP


async def get_update(event, context) -> dict:

    if event['httpMethod'] == 'POST':
        U: dict = json.loads(event['body'])

        await DP.feed_raw_update(bot=BOT, update=U)

        return {'statusCode': 200, 'body': 'ok'}
    else:
        return {'statusCode': 405}
