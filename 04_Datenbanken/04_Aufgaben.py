import mysql.connector
import json
from typing import List, Tuple, Union

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="testxd")

mycursor = mydb.cursor()

# Getter functions
def read_tables(*, limit:int=None, sys_tables:bool=False, error:bool=True) -> List[Tuple[str]]:
  try:
    limit_str = f"LIMIT {limit}" if limit else ""
    table_filter_str = "" if sys_tables else " WHERE table_schema NOT IN ('information_schema', 'mysql', 'performance_schema', 'sys')"
    sql = f"SELECT table_name\nFROM information_schema.tables\n{limit_str}{table_filter_str};"
    mycursor.execute(sql)
    return mycursor.fetchall()

  except Exception as e:
    if error:
      raise Exception("Read Tables Error: ", e) from e

def read_columns(*, table:str, error:bool=True) -> List[Tuple[str]]:
  try:
    mycursor.execute(f"SHOW COLUMNS FROM {table }")
    return mycursor.fetchall()
  
  except Exception as e:
    if error:
      raise Exception("Read Columns Error: ", e) from e

def read_rows(*, table: str, columns: list = ['*'], limit:int = None, error:bool=True) -> List[Tuple[str]]:
  try:
    limit_str = f"LIMIT {limit}" if limit else ""
    mycursor.execute(f"SELECT {', '.join(columns)} FROM {table} {limit_str}")
    rows = mycursor.fetchall()
    return rows
    
  
  except Exception as e:
    if error:
      raise Exception("Read Rows Error: ", e) from e

# Create/Drop functions
def create_table(*, table:str, columns_config_str: Union[str, List[str]], error:bool=True) -> bool:
  try:
    columns_error = "Columns config str must be specified when creating a table. It hast to be either 1 conform mysql string or a list of strs for each column" 
    
    if not columns_error:
      raise ValueError(columns_error) 
    
    if isinstance(columns_config_str, list):
      if not any(col for col in columns_config_str):
        raise ValueError(columns_config_str)
      columns_config_str = ', '.join(columns_config_str)

    mycursor.execute(f"CREATE TABLE IF NOT EXISTS {table} ({columns_config_str})")
    return True
  
  except Exception as e:
    if error:
      raise Exception("Create Table Error: ", e) from e
    return False

def drop_table(*, table:str, error:bool=True) -> bool:
  try:
    mycursor.execute(f"DROP TABLE IF EXISTS {table}")
    return True
  
  except Exception as e:
    if error:
      raise Exception("Drop Table Error: ", e) from e
    return False

def add_row(*, table:str, args:set, error:bool=True) -> bool:
  try:
    mycursor.execute("SHOW COLUMNS FROM %s" % table)
    columns = [row[0] for row in mycursor.fetchall() if row[5] != 'auto_increment']

    if len(args) != len(columns):
        raise ValueError("The length of the args doesnt match the length of the columns")

    placeholders = ', '.join(['%s'] * len(columns))
    columns_str = ', '.join(columns)
    sql = f"INSERT INTO {table} ({columns_str}) VALUES ({placeholders})"

    mycursor.execute(sql, args)
    return True

  except Exception as e:
    if error:
      raise Exception("Add Row Error: ", e) from e
    return False

def delete_row(*, table:str, object_id:int, error:bool=True) -> bool:
  try:
    sql = f"DELETE FROM {table} WHERE id = {object_id}"
    mycursor.execute(sql)
    return True

  except Exception as e:
    if error:
      raise Exception("Delete Row Error: ", e) from e
    return False

def add_column(*, table:str, column:str, column_type:str=None, column_constraint:str="", error:bool=True) -> False:
  try:
    if not column_type:
      raise ValueError("Column type must be specified when adding a column.")
    if column not in [col[0] for col in read_columns(table=table)]:
      mycursor.execute(f"ALTER TABLE {table} ADD {column} {column_type} {column_constraint}")
    return True

  except Exception as e:
    if error:
      raise Exception("Add Column Error: ", e) from e
    return False

def drop_column(*, table:str, column:str, error:bool=True) -> bool:
  try:
    if column in [col[0] for col in read_columns(table=table)]:
      mycursor.execute(f"ALTER TABLE {table} DROP COLUMN {column}")
    return True

  except Exception as e:
    if error:
      raise Exception("Drop Column Error: ", e) from e
    return False




# Initialize tables
drop_table(table="members")
drop_table(table="squads")

create_table(
  table="squads", 
  columns_config_str="""
    id INT AUTO_INCREMENT PRIMARY KEY,
    squadName VARCHAR(255), 
    homeTown VARCHAR(255), 
    formed VARCHAR(255), 
    status VARCHAR(255), 
    secretBase VARCHAR(255), 
    active VARCHAR(255)
  """
)
create_table(
  table="members", 
  columns_config_str="""
    memberId INT AUTO_INCREMENT PRIMARY KEY,
    squad_id INT,
    name VARCHAR(255),
    age VARCHAR(255),
    secretIdentity VARCHAR(255),
    powers VARCHAR(255),
    FOREIGN KEY (squad_id) REFERENCES squads(id) ON DELETE CASCADE
  """
)


# Insert data
with open("../base.json", "r") as my_file:
    content = json.load(my_file)

squads = []
members = []

for squad in content:
    sql_add_squad = "INSERT INTO squads (squadName, homeTown, formed, status, secretBase, active) VALUES (%s, %s, %s, %s, %s, %s)"
    mycursor.execute(sql_add_squad, (squad.get('squadName'), squad.get('homeTown'), squad.get('formed'), squad.get('status'), squad.get('secretBase'), squad.get('active')))
    squad_id = mycursor.lastrowid
    for member in squad.get("members"):
        sql_add_member = "INSERT INTO members (squad_id, name, age, secretIdentity, powers) VALUES (%s, %s, %s, %s, %s)"
        mycursor.execute(sql_add_member, (squad_id, member.get('name'), member.get('age'), member.get('secretIdentity'), "testpower"))

mycursor.execute("""
SELECT 
  squads.squadName, 
  squads.homeTown, 
  members.name
FROM members
INNER JOIN squads ON members.squad_id = squads.id;
                 """)

print(json.dumps(mycursor.fetchall(), indent=4))

mycursor.execute("""
SELECT *
FROM squads, members
                 """)
print(json.dumps(mycursor.fetchall(), indent=4))

# Tests
'''
print(f"""
  create_table: {create_table(table="test_table", columns_config_str="id INT AUTO_INCREMENT PRIMARY KEY, testColumn VARCHAR(255)")} 
  \n
  read_tables {read_tables()}
  \n
  add_column: {add_column(table="test_table", column="testColumn3", column_type="VARCHAR(255)")} 
  read_columns: {read_columns(table="test_table")}
  \n
  add_row: {add_row(table="test_table", args=("testVal1", "testVal2"))}
  read_rows: {read_rows(table="test_table")}
  \n
  delete_row: {delete_row(table="test_table", object_id=1)}
  read_rows: {read_rows(table="test_table")}
  \n
  drop_column: {drop_column(table="test_table", column="testColumn3")}
  read_columns: {read_columns(table="test_table")}
  \n
  drop_table: {drop_table(table="test_table")}
  read_tables: {read_tables()}
"""
)
'''
mydb.commit()