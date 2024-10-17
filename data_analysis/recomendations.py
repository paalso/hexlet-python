#!/usr/bin/env python3

from collections import Counter
import numpy as np


def get_recommendation(purchases, user_id, similar_goods_count=3, similar_purchases_count=5):
    top_similar_goods = _get_top_similar_goods(purchases, user_id, similar_purchases_count).sum(axis=0)
    top_similar_goods_ids = np.argsort(-top_similar_goods)
    filtered_top_similar_goods_ids = top_similar_goods_ids[top_similar_goods[top_similar_goods_ids] != 0]
    return filtered_top_similar_goods_ids[:similar_goods_count]


def _get_top_similar_goods(purchases, user_id, similar_purchases_count):
    user_purchases = purchases[user_id]
    user_goods = np.where(user_purchases > 0, 1, 0)

    top_similar_purchases = _get_top_similar_purchases(purchases, user_id, similar_purchases_count)
    top_similar_goods = np.where(top_similar_purchases > 0, 1, 0)
    top_similar_goods[:, user_goods == 1] = 0
    return top_similar_goods


def _get_top_similar_purchases(purchases, user_id, count):
    users_purchases = purchases[user_id]
    corrcoefs = np.corrcoef(users_purchases, purchases)[0,1:]

    sorted_ids = np.argsort(-corrcoefs)
    top_similar_ids = sorted_ids[sorted_ids != user_id][:count]
    top_similar_purchases = purchases[top_similar_ids]
    return top_similar_purchases


def main():
    # паттерны покупок для двух архетипов
    archetype_1 = np.array([5, 0, 3, 0, 2, 0, 4, 0, 1, 0])
    archetype_2 = np.array([0, 4, 0, 2, 0, 5, 0, 3, 0, 1])

    num_users = 12
    num_products = 10
    data = np.zeros((num_users, num_products))
    data[0] = archetype_1
    data[1:6, :] = archetype_1 + np.random.randint(1, 3, (5, num_products))
    data[6] = archetype_2
    data[7:, :] = archetype_2 + np.random.randint(1, 3, (5, num_products))

    recs = get_recommendation(data, 0)
    print(data)
    print(recs)
    # assert sorted(recs) == [1, 3, 5]
    print()

    recs = get_recommendation(data, 6)
    print(recs)
    # assert sorted(recs) == [0, 2, 4]


if __name__ == '__main__':
    main()
