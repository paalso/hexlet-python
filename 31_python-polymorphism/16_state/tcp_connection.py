from states.connected import ConnectedState
from states.disconnected import DisconnectedState


class TcpConnection:
    states = {
        'connected': ConnectedState,
        'disconnected': DisconnectedState,
    }

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.set_state('disconnected')

    def __str__(self):
        return f'{self.__class__.__name__}' + \
            f', ip: {self.ip}, port: {self.port}, {self.state}'

    def get_current_state(self):
        return str(self.state)

    def connect(self):
        self.state.connect()

    def disconnect(self):
        self.state.disconnect()

    def write(self, data):
        self.state.write(data)

    def set_state(self, state_name):
        self.state = self.__class__.states[state_name](self)
