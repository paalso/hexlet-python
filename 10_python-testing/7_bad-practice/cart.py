import os


class Right(object):
    items = []

    def add_item(self, good, count):
        self.items.append({'good': good, 'count': count})

    def get_items(self):
        return self.items

    def get_count(self):
        return sum(good['count'] for good in self.items)

    def get_cost(self):
        return sum(good['count'] * good['good']['price'] for good in self.items)


class Wrong1(object):
    items = []

    def add_item(self, good, count):
        self.items.append({'good': good, 'count': count})

    def get_items(self):
        return self.items

    def get_count(self):
        return sum(good['count'] for good in self.items)

    def get_cost(self):
        return sum(good['good']['price'] for good in self.items)


class Wrong2(object):

    def add_item(self, good, count):
        self.items = [{'good': good, 'count': count}]

    def get_items(self):
        return self.items

    def get_count(self):
        return sum(good['count'] for good in self.items)

    def get_cost(self):
        return sum(good['count'] * good['good']['price'] for good in self.items)


class Wrong3(object):

    def add_item(self, good, count):
        self.items = [{'good': good, 'count': count}]

    def get_items(self):
        return self.items

    def get_count(self):
        return len(self.items)

    def get_cost(self):
        return sum(good['count'] * good['good']['price'] for good in self.items)


implementations = {
    "right": Right,
    "wrong1": Wrong1,
    "wrong2": Wrong2,
    "wrong3": Wrong3,
}


def get_implementations():
    name = os.environ['FUNCTION_VERSION']
    return implementations[name]
