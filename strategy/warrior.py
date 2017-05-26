#!/usr/bin/env python3
"""Strategy Pattern example"""


class BaseWeapon(object):
    """Base class for weapons."""

    def name(self):
        print(self.__name__)

    def use_weapon(self):
        """Use weapon."""
        # explicitly set it up so this can't be called directly
        raise NotImplementedError('Exception raised, BaseWeapon is supposed to be an interface / abstract class!')


class Axe(BaseWeapon):
    def use_weapon(self):
        print('Chop with an axe.')


class Knife(BaseWeapon):
    def use_weapon(self):
        print('Cut with a knife')

class Character(object):
    """Base class for fighting characters."""

    def __init__(self, name):
        """Init class with character name."""
        self.name = name
        self.weapon = BaseWeapon

    def display(self):
        """Display character name."""
        print("I'm a {}".format(self.name))

    def fight(self):
        """Use defined weapon."""
        self.weapon.use_weapon(self)

    def set_weapon(self, weapon_behavior):
        """Define weapon behavior."""
        if (issubclass(weapon_behavior, BaseWeapon)):
            self.weapon = weapon_behavior
        else:
            raise TypeError("Expected argument with base class of BaseWeapon")

    def weapon_check(self):
        if (self.weapon.__name__ == BaseWeapon.__name__):
            return False
        print(self.weapon.__name__)
        return self.weapon.__name__



if __name__ == '__main__':
    king = Character("King")
    king.set_weapon(Axe)
    king.fight()
    king.weapon_check()

    queen = Character("Queen")
    if (not queen.weapon_check()):
        queen.set_weapon(Knife)
    queen.fight()
