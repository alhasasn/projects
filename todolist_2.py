todolist =[]
modifiers=['k','r']
while True :
    item=input('enter a list item or enter \'k\' to see list items and types \'r\' to remove an item ').lower()
    if item in modifiers and item=='k':
        for item in todolist:
            print(item)
    elif item in modifiers and item =='r':
        try:
             for item in todolist:
                  print(item)
             remove_item=input("Type the item_____")
             todolist.remove(remove_item)
        except:
            print('Item not in list')       
    elif item == 'exit':
        todolist.remove('exit')
        for item in todolist:
            print(item)
        break
    else:
        todolist.append(item)