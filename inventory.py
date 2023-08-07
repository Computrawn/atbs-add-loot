#!/usr/bin/env python3
# inventory.py — An exercise in understanding dictionaries.
# For more information, see README.md

import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
logging.disable(logging.CRITICAL)  # Note out to enable logging.


stuff = {
    "rope": 1,
    "torch": 6,
    "gold coin": 42,
    "dagger": 1,
    "arrow": 12,
}


def main() -> None:
    display_inventory(stuff)


def display_inventory(inventory: dict) -> None:
    print("Inventory:")
    item_total = 0
    for k, v in sorted(inventory.items()):
        if k != "dagger":
            print(str(v), k)
    for k, v in inventory.items():
        if k == "dagger":
            print(str(v), k)
        item_total += v
    print(f"Total number of items: {item_total}")


if __name__ == "__main__":
    main()
