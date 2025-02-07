from errors import TcpConnectionError


class DisconnectedState:
    def __init__(self, tcp_connection):
        self.tcp_connection = tcp_connection

    def __str__(self):
        return 'disconnected'

    def connect(self):
        self.tcp_connection.set_state('connected')

    def disconnect(self):
        raise TcpConnectionError(
            'Trying to disconnect already disconnected connection')

    def write(self, data):
        raise TcpConnectionError(
            'Trying to write while connection is disconnected')
