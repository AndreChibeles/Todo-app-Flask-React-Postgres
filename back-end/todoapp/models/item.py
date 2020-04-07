import psycopg2

def sql_query(query, *args):
    conn = psycopg2.connect("dbname=Todo-app user=postgres password=123")
    cur = conn.cursor()
    cur.execute(query, args)
    result = cur.fetchone()
    print(result)
    cur.close()
    conn.close()
    return result

class Item():

    def __init__(self, item_id, item_name, item_state):
        self.item_id = item_id
        self.item_name = item_name
        self.item_state = item_state

    def __str__(self):
        return f"{self.item_id}, {self.item_name}, {self.item_state}"

    @classmethod
    def find_by_id(cls, id):
        query = "SELECT * FROM items WHERE item_id=%s"
        result = sql_query(query, (id,))
        print(result)
        return cls(*result)




class Items():
    
    def __init__(self):
        self.item_list = []

