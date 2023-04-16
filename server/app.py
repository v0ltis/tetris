import re

import uvicorn
# uvicorn allows us to run the fastapi server

from typing_extensions import Annotated
from tools import DB_init as db_conn, conf_load as conf
from fastapi import FastAPI, Response

app = FastAPI()

@app.get('/scores')
async def get_scores(
        # gt = greater than, lt = less than
        quantity: int,
        offset:int = 0,
        gamemode:str = "all"):
    """
    Allow to get up to 50 entries from the database
    :param quantity: The quantity of scores to get
    :param offset: The index of the first score to get
                    (Exemple: If index = 10 and quantity = 10,the function will return the scores from the 11th to the 20th included)
    :param gamemode: The gamemode of the scores to get
    :return:
    """

    if not 0 < quantity <= 50:
        return Response(status_code=416, content="The quantity of scores to get must be between 1 and 50 included")
        # Error 416: Requested Range Not Satisfiable (https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/416)

    elif offset < 0:
        return Response(status_code=416, content="The offset must be greater than or equal to 0")
        # Error 416: Requested Range Not Satisfiable (https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/416)

    else:

        if gamemode == "all":
            return db_conn.connect().get_scores(quantity, offset)

        else:
            return db_conn.connect().get_scores(quantity, offset, gamemode)


@app.post('/scores')
async def add_score(
        name: str,
        score: int,
        date: str,
        gamemode: str,
        duration: str):
    """
    Allow to add a score to the database
    :param name: The name of the player
    :param score: The score of the player
    :param date: The date of the score
    :param gamemode: The gamemode of the score performed
    :param duration: The time it took to complete the game
    :return:
    """

    if not 1 <= len(name) <= 25:
        return Response(status_code=400, content=f"The name must be between 1 and 25 characters included (actual length: {len(name)})")
        # Error 400: Bad Request (https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400)

    # check if the date is valid thanks to a regex
    elif not re.match(
            r"^((((19|[2-9]\d)\d{2})-(0[13578]|1[02])-(0[1-9]|[12]\d|3[01]))|(((19|[2-9]\d)\d{2})-(0[13456789]|1[012])-(0[1-9]|[12]\d|30))|(((19|[2-9]\d)\d{2})-02-(0[1-9]|1\d|2[0-8]))|(((1[6-9]|[2-9]\d)(0[48]|[2468][048]|[13579][26])|((16|[2468][048]|[3579][26])00))-02-29))$",
            date):
        """
        This (awfull) regex validates dates in the YYYY-MM-DD format, taking into account leap years. It matches either one of the following patterns:

        Months with 31 days: (19|[2-9]\d)\d{2}-(0[13578]|1[02])-(0[1-9]|[12]\d|3[01])
        Months with 30 days: (19|[2-9]\d)\d{2}-(0[13456789]|1[012])-(0[1-9]|[12]\d|30)
        February: (19|[2-9]\d)\d{2}-02-(0[1-9]|1\d|2[0-8]) (for non-leap years)
        or (1[6-9]|[2-9]\d)(0[48]|[2468][048]|[13579][26]|(16|[2468][048]|[3579][26])00)-02-29 (for leap years)
        The regex starts and ends with ^ and $ respectively to match the entire string.
        """

        return Response(status_code=400, content=f"The date must be in the YYYY-MM-DD format (actual date: {date}), and must be a valid date (leap years are taken into account)")
        # Error 400: Bad Request (https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400)

    elif not 0 <= score <= 999999999:
        return Response(status_code=400, content=f"The score must be between 0 and 999999999 included (actual score: {score})")
        # Error 400: Bad Request (https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400)

    else:
        pass

if __name__ == '__main__':
    # perform the connection to the database
    db_conn.connect()

    # run the server
    conf = conf.load()['server']
    uvicorn.run(app, host=conf['host'], port=conf['port'])

