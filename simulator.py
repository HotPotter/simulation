import config
from pprint import pprint
from collections import defaultdict
import random

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
    result = simulate(1)
    plot(result)

'''
if __name__ == '__main__':
    main()
'''

import random

class PickAndReturnHeroPool():
    def __init__(self, hero_config):
        self.heroes = []
        self.ps = []
        for hero, p in hero_config:
            self.heroes.append(hero)
            self.ps.append(p)

    def random_choice(self, pick=1):
        return random.choices(self.heroes, self.ps, k=pick)

class PickAndDropHeroPool():
    def __init__(self, hero_config):
        pool = []
        for hero_name, num in hero_config:
            pool += [hero_name] * num
        random.shuffle(pool)
        self.pool = pool

    def random_choice(self, pick=1):
        reward = self.pool[0:pick]
        self.pool = self.pool[pick:]
        return reward



#heroes = {"tiffy":5, "kimmy":5, "yeti":10, "troll":10, "toffee":15}
heroes_config_list = [t for t in config.heroes.items()]
print(heroes_config_list)
#pool = PickAndReturnHeroPool([('tiffi', 3), ('kimmy', 2), ('yeti', 1)])
pool = PickAndReturnHeroPool(heroes_config_list)
print('pick and return 5')
print(pool.random_choice(5))
pool = PickAndDropHeroPool(heroes_config_list)
print('pick and drop 5')
print(pool.random_choice(5))

class PoolFactory():
    @classmethod
    def create_pool(cls, pool_name):
        if pool_name == 'drop':
            pool = PickAndDropHeroPool(heroes_config_list)
        elif pool_name == 'return':
            pool = PickAndReturnHeroPool(heroes_config_list)
        else:
            raise 'invalid pool name'
        return pool

'''
pool_name = config.pool_name
if pool_name == 'drop':
    pool = PickAndDropHeroPool(heroes_config_list)
elif pool_name == 'return':
    pool = PickAndReturnHeroPool(heroes_config_list)
else:
    raise 'invalid pool name'
'''

for _ in range(10):
    print(pool.random_choice(5))

random.choices(['tiffi', 'kimmy', 'yeti'], [3, 2, 1], k=10)




pool = PoolFactory.create_pool(config.pool_name)


