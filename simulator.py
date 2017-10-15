import config
from pprint import pprint
from collections import defaultdict
import random

import pool
import inventory
#from inventory import Inventory

def has_reward():
    if random.randint(0, 1):
        return True
    else:
        return False

def simulate_open_boxes():
    result = defaultdict(list)
    num_boxes = 0
    player_inventory = inventory.Inventory()
    hero_pool = pool.PoolFactory.create_pool('return')

    while True:
        num_boxes += 1
        if has_reward():
            reward = hero_pool.random_choice(pick=config.fragments_per_box)
            player_inventory.update(reward)

        update_result(result, player_inventory, num_boxes)

        if num_boxes > 5000:
            break

    return dict(result)

def update_result(result, inventory, num_boxes):
    for hero_name, num_fragments in inventory.hero_and_fragments():
        formed_heroes = []

        for more_heroes in result.values():
            formed_heroes += more_heroes

        if hero_name in formed_heroes:
            continue

        if num_fragments >= config.heroes[hero_name]:
            result[num_boxes].append(hero_name)

def simulate(num_players):
    result = []
    for _ in range(num_players):
        days = simulate_open_boxes()
        result.append(days)
    return result

def plot(result):
    print('Plot matplotlib:')
    pprint(result)

def main():
    result = simulate(1)
    plot(result)

if __name__ == '__main__':
    main()

