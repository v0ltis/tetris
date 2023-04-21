import uvicorn
# uvicorn allows us to run the fastapi server

from tools import DB_init as dbConn, conf_load as conf
from fastapi import FastAPI, Response

from math import ceil

import server.classes.API as requestBody

import datetime

app = FastAPI()


@app.get('/user')
async def get_user_stats(
        data: requestBody.GetUserStats) -> Response | list[dict]:
    """
    Allow to get the stats of a user (up to 50 entries)
    :param data: The data of the request
        contains:
            - username: The username of the user (1 <= len(str) <= 25)
            - gamemode: The gamemode id of the scores to get (str)
            - quantity: The number of scores to get (0 < int =< 50)
            - offset: The number of scores to skip (0 <= int)

    :return: The response of the server
    """

    if not 0 < data.quantity <= 50:
        return Response(
            status_code=416,
            content='{"response":"The quantity of scores to get must be between 1 and 50 included"}',
            headers={"Content-Type": "application/json"}
        )
        # Error 416: Requested Range Not Satisfiable (https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/416)

    elif data.offset < 0:
        return Response(
            status_code=416,
            content='{"response":"The offset must be greater than or equal to 0"}',
            headers={"Content-Type": "application/json"}
        )
        # Error 416: Requested Range Not Satisfiable (https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/416)

    elif len(data.username) > 25:
        return Response(
            status_code=400,
            content=f'{{"response":"The username must be between 1 and 25 characters included (actual length: {len(data.username)})"}}',
            headers={"Content-Type": "application/json"}
        )
        # Error 400: Bad Request (https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400)

    else:
        if data.gamemode == "all":
            return dbConn.connect().get_user_stats(data.username, data.quantity, data.offset)

        else:
            return dbConn.connect().get_user_gamemode_stats(data.username, data.quantity, data.offset, data.gamemode)


@app.get('/scores')
async def get_scores(
        data: requestBody.GetScores) -> Response | list[dict]:
    """
    Allow to get up to 50 entries from the database
    :param data: The data of the request
        contains:
            - quantity: The number of scores to get (0 < int =< 50)
            - offset: The number of scores to skip (0 <= int)
            - gamemode: The gamemode id of the scores to get (str)

    :return: The response of the server
    """

    if not 0 < data.quantity <= 50:
        return Response(
            status_code=416,
            content='{"response":"The quantity of scores to get must be between 1 and 50 included"}',
            headers={"Content-Type": "application/json"}
        )
        # Error 416: Requested Range Not Satisfiable (https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/416)

    elif data.offset < 0:
        return Response(
            status_code=416,
            content='{"response":"The offset must be greater than or equal to 0"}',
            headers={"Content-Type": "application/json"}
        )
        # Error 416: Requested Range Not Satisfiable (https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/416)

    else:
        if data.gamemode == "all":
            return dbConn.connect().get_scores(data.quantity, data.offset)

        else:
            return dbConn.connect().get_gamemode_scores(data.quantity, data.offset, data.gamemode)


@app.post('/scores')
async def add_score(
        data: requestBody.PostScores) -> Response:
    """
    Allow to add a score to the database
    :param data: The data of the score to add
        contains:
            - name: The name of the player (1 <= len(str) <= 25)
            - score: The score of the player (0 <= int)
            - date: The date of the score (float representing a timestamp)
            - gamemode: The gamemode of the score (str)
            - duration: The duration of the game (0 <= int representing the number of seconds elapsed)
    :return: The response of the server
    """

    if not 1 <= len(data.name) <= 25:
        return Response(
            status_code=400,
            content=f'{{"response":"The name must be between 1 and 25 characters included (actual length: {len(data.name)})"}}',
            headers={"Content-Type": "application/json"}
        )
        # Error 400: Bad Request (https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400)

    # check if the date is a valid timestamp float

    if data.date < 0 or \
            not datetime.datetime.fromtimestamp(data.date) < (datetime.datetime.now() + datetime.timedelta(minutes=1)):
        """
        Check if the date is between the 1st of January 1970 and the current date
        This allows us to avoid people from adding scores from the future
        
        A delay of 1 minute is added to the current date to avoid problems with time not beign perfectly synchronized between the server and the client
        """

        return Response(
            status_code=400,
            content=f'{{"response":"The timestamp is not valid. It must be between 0 and {ceil(datetime.datetime.now().timestamp())} (actual: {data.date})"}}',
            headers={"Content-Type": "application/json"}
        )

    if data.duration < 1 or \
            not datetime.timedelta(seconds=data.duration) < datetime.timedelta(hours=24):
        """
        Check if the duration is between 1 second and 24 hours
        
        This allow to prevent the addition of stupidly long or short durations
        """

        return Response(
            status_code=400,
            content=f'{{"response":"The duration is not valid. It must be between 1 second and 24 hours'
                    f'(actual duration: {data.duration} seconds)"}}',
            headers={"Content-Type": "application/json"}
        )
        # Error 400: Bad Request (https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400)

    elif not 0 <= data.score:
        """
        Don't allow negative scores
        """
        return Response(
            status_code=400,
            content=f'{{"response":"The score must be greater than or equal to 0 (actual score: {data.score})"}}',
            headers={"Content-Type": "application/json"}
        )
        # Error 400: Bad Request (https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400)

    else:
        dbConn.connect().add_score(data.name, data.score, data.date, data.gamemode, data.duration)

        return Response(
            status_code=202,
            content=f'{{"response":"Score added successfully"}}',
            headers={"Content-Type": "application/json"}
        )


if __name__ == '__main__':
    # perform the connection to the database
    dbConn.connect()

    # run the server
    conf = conf.load()['server']
    uvicorn.run(app, host=conf['host'], port=conf['port'])
