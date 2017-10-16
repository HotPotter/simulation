import config
from pprint import pprint
from collections import defaultdict
import collections
import random

import pool
import inventory
import plot

def has_reward(): # FIXME need to be replaced by box giving mechanism
    if random.randint(1, 1):
        return True
    else:
        return False

def simulate_open_boxes():
    result = defaultdict(list)
    num_boxes = 0
    player_inventory = inventory.Inventory()
    hero_pool = pool.PoolFactory.create_pool(config.pool_name) # modify in Config

    while True:
        num_boxes += 1
        if has_reward():
            reward = hero_pool.random_choice(pick=config.fragments_per_box)
            player_inventory.update(reward)

        update_result(result, player_inventory, num_boxes)
        #print(player_inventory.hero_and_fragments()) # print result of each box
        #print(result) # print hero formation after each box
        #print(reward) # print fragments drawn from each box

        if num_boxes > 9: # FIXME stop condition
            break

    return dict(result)

'''update inventory, create hero if possible'''
def update_result(result, inventory, num_boxes):
    for hero_name, num_fragments in inventory.hero_and_fragments():
        formed_heroes = []

        for more_heroes in result.values():
            formed_heroes += more_heroes

        if hero_name in formed_heroes:
            continue

        if num_fragments >= config.heroes[hero_name]: # calculate the formation of a hero
            result[num_boxes].append(hero_name)
1
def simulate(num_players):
    result = []
    for _ in range(num_players):
        one_player = simulate_open_boxes()
        result.append(one_player)
    return result

def do_plot(result):
    print('Plot matplotlib:')
    pprint(result)
    first_days = []
    for days in result:
        first_days.append(min(days))

    c = collections.Counter(first_days)
    xs = []
    ys = []
    for x, y in c.items():
        xs.append(x)
        ys.append(y)
    #c1 = [(x, y) for x, y in c.items()]

    print(xs)
    print(ys)
    print(first_days)

    print('plot!')
    plot.my_plot(xs, ys)
1
def main():
    result = simulate(config.num_players)
    do_plot(result)

if __name__ == '__main__':
    main()

