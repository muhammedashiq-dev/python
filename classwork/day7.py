items = ['milk','bread','eggs']
def add_item(item):
    items.insert(2,item)
add_item('mango')
print(items)
def rem_item():
    items.pop()
rem_item()
print(items)
def character_count(item):
    count = 0
    for x in item:
        for y in x:
            count = count + 1
    return count
display_items = lambda lst: [print(f'Item:{i}') for i in lst]
display_items(items)
charac_count =  character_count(items)
print('count:',charac_count)
