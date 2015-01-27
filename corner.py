

class Corner:

  def __init__(self):
    return
  def query(self, query):
    return
  def lastInsert(self):
    query = "SELECT LAST_INSERT_ID() as id;"
    result = self.query(query)
