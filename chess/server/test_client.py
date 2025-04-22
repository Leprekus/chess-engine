from .main import app
from fastapi.testclient import TestClient

BACKEND = 'http://localhost:8000'
create_game, join_game, session = [ '/pvp/create-game', '/pvp/join-game', '/pvp/{session_id}',  ]

game = {
        'sessionid': '',
        'p1': '',
        'p2': '',
}
def test_create_game():
    client = TestClient(app)
    response = client.post(BACKEND + create_game)
    data = response.json()
    game['sessionid'] = data['session_id']
    game['p1'] = data['player_id']
    print(game)

def test_join_game():
    client = TestClient(app)
    response = client.post(BACKEND + join_game)
    print(response.json())

#def test_session():
#    client = TestClient(app)
#    response = client.post(BACKEND + session)
#    print(response.json())
#
#def test_create_match():
#    client = TestClient(app)
#    initial_player_state = {
#            'session_id': '',
#            'player_id': '',
#    }
#    client_data =  initial_player_state
#    session_id, player_id  = client.post(BACKEND + create_game).json()
#    client_data['session_id'] = session_id
#    client_data['player_id'] = player_id
#    endpoint = BACKEND.replace('http', 'ws') + session.replace('{session_id}', session_id)
#    with client.websocket_connect(endpoint) as ws:
#        data = ws.receive_json()
#        print('connected')
#
#
#
#def test_websocket():
#    client = TestClient(app)
