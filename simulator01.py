import config
from pprint import pprint
from collections import defaultdict
import random

'''

reward_per_x_box = 5
reward_drop_rate = 0.5
fragments_per_box = 5

heroes = {"tiffy":5, "kimmy":5, "yeti":10, "troll":10, "toffee":15}
'''

def has_reward():
    if random.randint(0, 1):
        return True
    else:
        return False

def make_hero_pool():
    '''英雄奖池'''
    pool = []
    for hero_name, num in config.heroes.items():
        pool += [hero_name] * num
    random.shuffle(pool)
    return pool

p = make_hero_pool()
def open_box(pool):
    reward = pool[0:config.fragments_per_box]
    new_pool = pool[config.fragments_per_box:]
    return (reward, new_pool)

def update_inventory(inventory, reward):
    for hero_name in reward:
        inventory[hero_name] += 1

def simulate_open_boxes():
    result = defaultdict(list)
    num_boxes = 0
    inventory = defaultdict(int)
    hero_pool = make_hero_pool()

    while True:
        num_boxes += 1
        if has_reward():
            reward, hero_pool = open_box(hero_pool)
            update_inventory(inventory, reward)

        update_result(result, inventory, num_boxes)

        if len(hero_pool) == 0:
            break

    return dict(result)

def update_result(result, inventory, num_boxes):
    for hero_name, num_fragments in inventory.items():
        heroes = []
        for more_heroes in result.values():
            heroes += more_heroes
        if hero_name in heroes:
            continue
        else:
            if num_fragments == config.heroes[hero_name]:
                result[num_boxes].append(hero_name)

class BoxSim():
    def __init__(self):
        self.inventory = defaultdict(int)
        self.num_boxes = 0
        self.hero_pool = make_hero_pool()

    def update_inventory(self, reward):
        self.inventory['tiffi'] = 5


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
    result = simulate(10)
    plot(result)
if __name__ == '__main__':
    main()


