# https://ru.hexlet.io/courses/python-functions/lessons/more-decorators/exercise_unit
# https://ru.hexlet.io/code_reviews/350535

# Больше о декораторах
# =====================
"""
В этот раз вы снова будете реализовывать мемоизирующий декоратор "memoizing".
Но на этот раз декоратор должен принимать аргумент, задающий максимальное
количество запоминаемых значений. При превышении количества запомненных
значений лишние должны быть отброшены, причём сначала — самые старые!

Напоминаю, мемоизируемые функции считать численными функциями одного
аргумента. И не забудьте про functools.wraps!
"""

from functools import wraps


def memoizing(max_args):
    def wrapper(func):
        memo = {}
        args = []
        @wraps(func)
        def inner(x):
            result = memo.get(x)
            if result is None:
                result = func(x)
                args.append(x)
                if len(args) > max_args:
                    del memo[args.pop(0)]
                memo[x] = result
            print(memo, args)
            return result
        return inner
    return wrapper


def memoizing(max_memoized):
    def wrapper(function):
        memoized_values = {}
        memoized_args = []
        @wraps(function)
        def inner(arg):
            if arg in memoized_values:
                return memoized_values[arg]
            result = function(arg)
            if len(memoized_args) >= max_memoized:
                oldest_arg = memoized_args.pop(0)
                memoized_values.pop(oldest_arg)
            memoized_args.append(arg)
            memoized_values[arg] = result
            return result
        return inner
    return wrapper


@memoizing(3)
def f(x):
    """Multiplying by 10"""
    print('Calculating..., x = {}'.format(x))
    return x * 10



print(f.__name__)
print(f.__doc__)
f(1)
f(2)
f(1)
f(4)
f(5)
f(6)
f(1)
f(1)
f(1)
f(7)
f(5)
