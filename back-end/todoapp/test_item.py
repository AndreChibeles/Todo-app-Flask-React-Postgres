
from models.item import Item
import psycopg2

item = Item.find_by_id(1)
print(item)

