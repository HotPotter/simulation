import config
import random

class PoolFactory():
    @classmethod
    def create_pool(cls, pool_name='remove'):
        heroes_config_list = [t for t in config.heroes.items()]
        if pool_name == 'remove':
            pool = PickAndRemoveHeroPool(heroes_config_list)
        elif pool_name == 'return':
            pool = PickAndReturnHeroPool(heroes_config_list)
        else:
            raise ValueError('invalid pool name')
        return pool


class PickAndReturnHeroPool():
    def __init__(self, hero_config):
        self.heroes = []
        self.ps = []
        for hero, p in hero_config:
            self.heroes.append(hero)
            self.ps.append(p)

    def random_choice(self, pick=1):
        return random.choices(self.heroes, self.ps, k=pick)

class PickAndRemoveHeroPool():
    def __init__(self, hero_config):
        pool = []
        for hero_name, num in hero_config:
            pool += [hero_name] * num
        #random.shuffle(pool)
        self.pool = pool

    def random_choice(self, pick=1):
        reward = self.pool[0:pick]
        self.pool = self.pool[pick:]
        return reward

    '''
    #heroes = {"tiffy":5, "kimmy":5, "yeti":10, "troll":10, "toffee":15}
    heroes_config_list = [t for t in config.heroes.items()]
    print(heroes_config_list)
    #pool = PickAndReturnHeroPool([('tiffi', 3), ('kimmy', 2), ('yeti', 1)])
    pool = PickAndReturnHeroPool(heroes_config_list)
    print('pick and return 5')
    print(pool.random_choice(5))
    pool = PickAndRemoveHeroPool(heroes_config_list)
    print('pick and  5')
    print(pool.random_choice(5))
    '''
