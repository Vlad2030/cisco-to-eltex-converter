from loguru import logger
import json


CISCO_SYNTAX_FILE: object = "/cisco/commands.json"
ELTEX_SYNTAX_FILE: object = "/eltex/commands.json"


class Json:
    async def dump(data: str) -> str:
        return json.dump(data)
    

    async def load(data: str) -> str:
        return json.load(data)
    

    async def loads(data: str) -> str:
        return json.loads(data)


async def cisco_to_eltex(data: str) -> str:
    eltex_code: list = {}
    try:
        async with open(file=CISCO_SYNTAX_FILE, mode="r") as file:
            commands: list = Json.load(data=file)
        cisco_code: dict = data.split("\n") 
        for i in range(len(cisco_code)):
            cisco_code[i]

    except Exception:
        return logger.error("{excp}", excp=Exception)
    return


async def eltex_to_cisco(data: str) -> str:
    
    return