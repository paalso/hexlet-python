from errors import TcpConnectionError


class ConnectedState:
    def __init__(self, tcp_connection):
        self.tcp_connection = tcp_connection

    def __str__(self):
        return 'connected'

    def connect(self):
        raise TcpConnectionError('Trying to connect already connected connection')

    def disconnect(self):
        self.tcp_connection.set_state('disconnected')

    def write(self, data):
        print(f'Written data: {data}')
