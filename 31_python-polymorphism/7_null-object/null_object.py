# https://ru.hexlet.io/courses/python-polymorphism/lessons/null-object/exercise_unit
# https://ru.hexlet.io/code_reviews/1145343

# Python: Полиморфизм
# 7. Null Object Pattern

from subscription import Subscription
from user import User

user1 = User('vasya@email.com', Subscription('premium'))
user1.get_current_subscription().has_premium_access()       # True
user1.get_current_subscription().has_professional_access()  # False

user2 = User('vasya@email.com', Subscription('professional'))
user2.get_current_subscription().has_premium_access()       # False
user2.get_current_subscription().has_professional_access()  # True

print(type(user1.get_current_subscription()))
print(type(user2.get_current_subscription()))

# Внутри создается фейковая, потому что подписка не передается
user3 = User('vasya@email.com')
user3.get_current_subscription().has_premium_access()       # False
user3.get_current_subscription().has_professional_access()  # False

user4 = User('rakhim@hexlet.io')    # администратор, проверяется по емейлу
user4.get_current_subscription().has_premium_access()       # True
user4.get_current_subscription().has_professional_access()  # True

print(type(user3.get_current_subscription()))
print(type(user4.get_current_subscription()))
