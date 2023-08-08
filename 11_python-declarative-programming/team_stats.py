# https://ru.hexlet.io/courses/python-declarative-programming/lessons/generator-expressions/exercise_unit

# Статистика матчей по командам
# ==============================

# реализовать функцию wins_by_team(), которая должна принимать перечень
# (iterable) матчей в качестве единственного аргумента и возвращать словарь,
# ключами которого выступали бы имена команд, а значениями множества названий
# команд которых данная команда-ключ обыграла хотя бы раз.


def wins_by_team(game_results):
    return {
        hero: set(loser for winner, loser in game_results if winner == hero)
        for hero, _ in game_results
    }


assert wins_by_team(
    [("A", "B"), ("B", "C"), ("A", "C")]
) == {'A': {'B', 'C'}, 'B': {'C'}}


'''
# Hexlet version
def wins_by_team(games):
    winners = {team for team, _ in games}
    return {
        team: {looser for winner, looser in games if winner == team}
        for team in winners
    }
'''
