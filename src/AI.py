from src.client import GameClient
from src.grpc_stubs.hide_and_seek_pb2 import GameView


def get_thief_starting_node(view: GameView) -> int:
    # write your code here
    return 2


class Phone:
    def __init__(self, client: GameClient):
        self.client = client

    def send_message(self, message):
        self.client.send_message(message)


class AI:
    def __init__(self, phone: Phone):
        self.phone = phone

    def thief_move_ai(self, view: GameView) -> int:
        # write your code here
        self.phone.send_message('010100101')
        return 2

    def police_move_ai(self, view: GameView) -> int:
        # write your code here
        self.phone.send_message('00101001')
        return 1