#!/usr/bin/env python3
# filename.py — Short description of project goes here.
# For more information, see README.md

from inventory import display_inventory
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
logging.disable(logging.CRITICAL)  # Note out to enable logging.


def add_to_inventory(inventory, added_items):
    for i, _ in enumerate(added_items):
        if added_items[i] in inventory.keys():
            inventory[added_items[i]] = inventory.get(added_items[i], 0) + 1
        else:
            inventory.setdefault(str(added_items[i]), 1)
    return inventory


starting_inventory_1 = {"gold coin": 42, "rope": 1}
starting_inventory_2 = {"rope": 2, "gold coin": 1337}
starting_inventory_3 = {"vorpal sword": 1, "rope": 3, "gold coin": 42}

dragon_loot_1 = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
dragon_loot_2 = ["dagger", "ruby", "gold coin", "gold coin", "ruby"]
dragon_loot_3 = ["broken dagger", "gold coin", "ruby", "vorpal sword"]

finalInv = add_to_inventory(starting_inventory_1, dragon_loot_2)
display_inventory(finalInv)
