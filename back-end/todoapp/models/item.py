import psycopg2

def sql_query(query, *args):
    conn = psycopg2.connect("dbname=Todo-app user=postgres password=123")
    cur = conn.cursor()
    cur.execute(query, args)
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result

def sql_query_insert(query, args):
    try:
        conn = psycopg2.connect("dbname=Todo-app user=postgres password=123")
        cur = conn.cursor()
        cur.execute(query, args)
        conn.commit()
        cur.close()
        conn.close()
        return True
    except Exception as e:
        print(e)
        return False


class Item():

    def __init__(self, item_id, item_name, item_state):
        self.item_id = item_id
        self.item_name = item_name
        self.item_state = item_state

    def __str__(self):
        return f"{self.item_id}, {self.item_name}, {self.item_state}"

    @classmethod
    def find_by_id(cls, id):
        """Finds a row from the dB based on the id
        
        Keyword arguments:
        id: id
        Return: an object from type Item
        """
        
        query = "SELECT * FROM items WHERE item_id=%s"
        result = sql_query(query, (id,))
        print(result)
        return cls(*result)
    
    def create_item(item_name):
        query = "INSERT INTO items (item_name, item_state) VALUES (%s, %s)"
        if sql_query_insert(query, (item_name, False)):
            print("Item inserted with success")
            return 
        print("A problem in insertion")
    
    def update_item(self, id, data):
        query = "UPDATE items SET item_name=%s, item_state=%s WHERE item_id=%s"
        print("update_item")
        print(data)
        if sql_query_insert(query, (data[0], data[1], id)):
            print("Item Updated with success")
            return
        print("Problem in update")

    def delete_item(item_id):
        query = "DELETE FROM items WHERE item_id=%s"
        if sql_query_insert(query, (item_id,)):
            print("Item Deleted with success")
            return
        print("Problem deleting item")





class Items():
    
    def __init__(self):
        self.item_list = []

