# Example  
# to use lambda expression to perform sorting

# What to do
# ==========
# refer to the remarks below

menu1 = [
 ('b', '$1.50'),
 ('a', '$2.00'),
 ('c', '$2.50'),
]

# develop a sorting method by name
def sortbyname(menu):
    menu.sort(key = lambda i:i[0], reverse = True)
    return menu

# develop a sorting method by price
def sortbyprice(menu):
    menu.sort(key = lambda i:i[0], reverse = True)
    return menu

print (sortbyprice(menu1));