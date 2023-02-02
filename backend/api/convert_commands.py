from loguru import logger
import json


CISCO_SYNTAX_FILE: object = "/cisco/commands.json"
ELTEX_SYNTAX_FILE: object = "/eltex/commands.json"


class Json:
    async def dump(data: dict) -> json.JSONDecoder:
        return json.dump(data)
    

    async def load(data: str) -> json.JSONDecoder:
        return json.load(data)
    

    async def loads(data: str) -> json.JSONDecoder:
        return json.loads(data)


async def openFile(file: str, mode: str) -> None:
    async with open(file=file, mode=mode) as file:
        return file


async def cisco_to_eltex(data: str) -> str:
    # TODO: Доделать
    eltex_code: list = {}
    cisco_code: list = {}
    try:
        cisco_file = await openFile(file=CISCO_SYNTAX_FILE, mode="r") 
        commands: list = Json.load(data=cisco_file)
        cisco_code: dict = data.split("\n") 
        for i in range(len(cisco_code)):
            cisco_code[i]
        return eltex_code
    except Exception:
        return logger.error("{excp}", excp=Exception)


async def eltex_to_cisco(data: str) -> str:
    
    return