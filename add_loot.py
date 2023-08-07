#!/usr/bin/env python3
# add_loot.py — An exercise in uderstanding dictionaries.
# For more information, see README.md

from inventory import display_inventory
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
logging.disable(logging.CRITICAL)  # Note out to enable logging.


starting_inventory_1 = {"gold coin": 42, "rope": 1}
starting_inventory_2 = {"rope": 2, "gold coin": 1337}
starting_inventory_3 = {"vorpal sword": 1, "rope": 3, "gold coin": 42}

dragon_loot_1 = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
dragon_loot_2 = ["dagger", "ruby", "gold coin", "gold coin", "ruby"]
dragon_loot_3 = ["broken dagger", "gold coin", "ruby", "vorpal sword"]


def main():
    final_inventory = add_to_inventory(starting_inventory_1, dragon_loot_2)
    display_inventory(final_inventory)


def add_to_inventory(inventory, loot):
    for item in loot:
        if item in inventory.keys():
            inventory[item] = inventory.get(item, 0) + 1
        else:
            inventory.setdefault(str(item), 1)
    return inventory


if __name__ == "__main__":
    main()
