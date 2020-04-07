
from models.item import Item
import psycopg2

item = Item.find_by_id(1)
print(item)
#Item.create_item("Teste 3")
#item2 = Item.find_by_id(8)

item_update = Item.find_by_id(4)
data = ["Update Teste", True]
item_update.update_item(4, data)
#Item.delete_item(10)



