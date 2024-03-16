from core.api_token import API_TOKEN

import berserk

session = berserk.TokenSession(API_TOKEN)

client = berserk.Client(session=session)
