from fastapi import FastAPI, WebSocket, WebSocketException, WebSocketDisconnect
from starlette.websockets import WebSocketClose
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from .illegal_match_access_error import IllegalMatchAccessException 
from .match_making import Match

app = FastAPI()
match = Match()


@app.get('/')
async def root():
    return { 'message': 'hello world' }

'''
    FLOW
        1. Player 1 hits /pvp/create-game, which creates a match instance and returns a session_id and player_id.
        2. Player 1 gets redirected to /pvp/{session_id}.
        3. Player 2 accepts the invite link which cointans p2_id and joins /pvp/{session_id} providing p2_id.
        4. /pvp/{session_id} handles the game until the match is over.
'''

@app.post('/pvp/create-game')
async def pvp_create_game():
    '''
        creates a game and returns both players ids.
        P1 client is then in charge of generating an invite link
        and sharing it with P2.
    '''
    session_id, player1_id = match.create_game()
    return { 'session_id': session_id, 'player_id': player1_id }


@app.websocket('/pvp/{session_id}')
async def pvp(ws: WebSocket, session_id: str, player_id: str):
    try:
        #await ws.accept()
        await match.socket_handler(session_id, player_id, ws)

        while True:
            player_data = await ws.receive_json()
            player_id = player_data.get('player_id', None)
            player_move = player_data.get('move', None)

            if player_id:
                match.joined(player_id)

            if player_id and player_move and match.ready:
                payload =match.handle_player_move(player_id, player_move)
                await ws.send_json( payload )
            

    except WebSocketException:
            print(f'WebSocketException {WebSocketException}')

    except IllegalMatchAccessException:
            print(f'{IllegalMatchAccessException}')

    except Exception as e:
            print(f'Exception {e}')

@app.get('/pve/{session_id}')
async def pve():
    return { 'message': 'hello world' }

