import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from fastapi import WebSocket
from typing import Dict
from .illegal_match_access_error import IllegalMatchAccessException

from uuid import uuid4

class Player:
    def __init__(self, id: str):
        self.id = id
'''
 { session_id: [ player1_id, player2_id ] }
 { player_id: websocket }
'''

class Match:
    def __init__(self):
        #self.referee = Referee()
        self.session: dict[str, tuple[str, str ]] = {}
        self.player: dict[str, WebSocket | None] = {}

    '''
        creates and stores ids for the current match and both players.
    '''
    def create_game(self) -> tuple[str, str]:
        session_id, p1, p2 = str(uuid4()), str(uuid4()), str(uuid4())
        self.session[session_id] = (p1, p2)
        self.player[p1] = None
        self.player[p2] = None
        return  session_id, p1


    def joined(self, id: str) -> None:
        pass
    def handle_player_move(self, player_id: str, move: str):
        pass

