"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time

class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.bounty = 5

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            hero.coins += self.bounty
            print "%s had %d in bounty. %d added to coins." % (self.name, self.bounty, self.bounty)
            return
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)



class Shadow(Character):
    def __init__(self):
        self.name = 'shadow'
        self.health = 1
        self.power = 5
        self.bounty = 9

    def receive_damage(self, points):
        take_damage = random.random() < 0.1
        if take_damage:
            print "%s didn't receive any damage." % self.name
        super(Shadow, self).receive_damage

class Zombie(Character):
    def __init__(self):
        self.name = 'zombie'
        self.health = 6
        self.power = 2
        self.bounty = 7

    def alive(self):
        return True

class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.armor = 0
        self.backpack = True
        self.backpack_items = []

    def attack(self, enemy):
        double_damage = random.random() < 0.2
        damage=self.power
        if double_damage:
            print "%s does double damage to %s during attack" % (self.name, enemy.name)
            damage=self.power*2
        enemy.receive_damage(damage)

    def receive_damage(self, points):
        if points > self.armor:
            self.health -= (points - self.armor)
        print "%s received %d damage." % (self.name, (points-self.armor))
        if self.health <= 0:
            print "%s is dead." % self.name

    def restore(self):
        self.health += 10
        print "Hero's heath is restored to %d!" % self.health
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)


class Medic(Character):
    def __init__(self):
        self.name = 'medic'
        self.health = 50
        self.power = 1
        self.coins = 20

    def receive_damage(self, points):
           super(Medic, self).receive_damage(self, points)
           if random.random() <= .2:
               self.health += 2
class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2
        self.bounty = 6

class Wizard(Character):
    def __init__(self):
        self.name = 'wizard'
        self.health = 8
        self.power = 1
        self.bounty = 8

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print "%s swaps power with %s during attack" % (self.name, enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Battle(object):
    def do_battle(self, hero, enemy):
        print "====================="
        print "Hero faces the %s" % enemy.name
        print "====================="
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print "You have: "
            print Backpack(hero)
            print " in your backback. Did you want to take anything out for this battle?"
            print " 1. Yes"
            print " 2. No"
            input = int(raw_input())
            if input == 1:
                print "We will get back to this"
            elif input == 2:
                pass
            print "-----------------------"
            print "What do you want to do?"
            print "1. fight %s" % enemy.name
            print "2. do nothing"
            print "3. flee"
            print "> ",
            input = int(raw_input())
            if input == 1:
                hero.attack(enemy)
            elif input == 2:
                pass
            elif input == 3:
                print "Goodbye."
                exit(0)
            else:
                print "Invalid input %r" % input
                continue
            enemy.attack(hero)
        if hero.alive():
            print "You defeated the %s" % enemy.name
            return True
        else:
            print "YOU LOSE!"
            return False

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print "%s's health increased to %d." % (character.name, character.health)

class SuperTonic(Tonic):
    cost = 10
    name = 'supertonic'

    def apply(self, character):
        character.health = 10
        print "%s's health increased to %d." % (character.name, character.health)

class Armor(object):
    cost = 10
    name = 'armor'
    def apply(self, hero):
        hero.armor += 2
        print "%s's Armor increased to %d." % (hero.name, hero.armor)

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print "%s's power increased to %d." % (hero.name, hero.power)

class Backpack(object):
    name = 'backpack'
    def apply(self, hero):
        hero.backpack_items
        print "%s was added to your backpack." % store.item
        for item in self.backpack_items:
            print item.name


class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, Sword, SuperTonic, Armor]
    def do_shopping(self, hero):
        while True:
            print "====================="
            print "Welcome to the store!"
            print "====================="
            print "You have %d coins." % hero.coins
            print "What do you want to do?"
            for i in xrange(len(Store.items)):
                item = Store.items[i]
                print "%d. buy %s (%d)" % (i + 1, item.name, item.cost)
            print "10. leave"
            input = int(raw_input("> "))
            if input == 10:
                break
            else:
                if hero.coins >= 0:
                    ItemToBuy = Store.items[input - 1]
                    item = ItemToBuy()
                    hero.buy(item)
                    hero.backpack_items.append(item)
                else:
                    print "You don't have enough coins for this."

hero = Hero()
enemies = [Goblin(), Wizard(), Shadow(), Zombie(), Medic()]
battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print "YOU LOSE!"
        exit(0)
    shopping_engine.do_shopping(hero)

print "YOU WIN!"
