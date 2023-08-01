# List to Dictionary Function for Fantasy Game Inventory


def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        if addedItems[i] in inventory.keys():
            inventory[addedItems[i]] = inventory.get(addedItems[i], 0) + 1
        else:
            inventory.setdefault(str(addedItems[i]), 1)
    return inventory


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in sorted(inventory.items()):
        if k != "dagger":
            print(f"{v} {k}")
    for k, v in inventory.items():
        if k == "dagger":
            print(f"{v} {k}")
        item_total += v
    print(f"Total number of items: {item_total}")


initInv_1 = {"gold coin": 42, "rope": 1}
initInv_2 = {"rope": 2, "gold coin": 1337}
initInv_3 = {"vorpal sword": 1, "rope": 3, "gold coin": 42}

dragonLoot_1 = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
dragonLoot_2 = ["dagger", "ruby", "gold coin", "gold coin", "ruby"]
dragonLoot_3 = ["broken dagger", "gold coin", "ruby", "vorpal sword"]

finalInv = addToInventory(initInv_1, dragonLoot_2)
displayInventory(finalInv)
