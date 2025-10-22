inventory = []

def add_item(item):
    inventory.append(item)

def count_items(items):
    if not items:
        return 0
    return 1 + count_items(items[1:])

show_item = lambda item: print(f"Item in Stock: {item}")

def main():
    add_item("dog food")
    add_item("cat toy")
    add_item("bird cage")
    add_item("fish tank")

    for i in inventory:
        show_item(i)

    total = count_items(inventory)
    print(f"\nTotal number of items: {total}")

main()
