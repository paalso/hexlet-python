class FakeClient:
    def __init__(self, data):
        self.data = data

    def list_for_users(self, user_name):
        return self.data
