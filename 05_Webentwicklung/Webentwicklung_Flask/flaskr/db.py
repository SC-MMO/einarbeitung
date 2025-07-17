import mysql.connector
from flask import current_app, g
from typing import List, Tuple, Union, Any

#* init funcs

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host=current_app.config['DB_HOST'],
            user=current_app.config['DB_USER'],
            passwd=current_app.config['DB_PASSWORD'],
            database=current_app.config['DB_NAME']
        )
    return g.db

def get_cursor():
    return get_db().cursor()

#* Read funcs

def read_tables(*, limit:int=None, sys_tables:bool=False, error:bool=True, cursor=None) -> List[Tuple[str]]:
  try:
    if not cursor:
      cursor = get_cursor()
    limit_str = f"LIMIT {limit}" if limit else ""
    table_filter_str = "" if sys_tables else " WHERE table_schema NOT IN ('information_schema', 'mysql', 'performance_schema', 'sys')"
    sql = f"SELECT table_name\nFROM information_schema.tables\n{limit_str}{table_filter_str};"
    cursor.execute(sql)
    return cursor.fetchall()

  except Exception as e:
    if error:
      raise Exception("Read Tables Error: ", e) from e

def read_columns(*, table:str, only_name:bool=False, error:bool=True, cursor=None) -> Union[List[Tuple[str]], List[str]]:
  try:
    if not cursor:
      cursor = get_cursor()
    cursor.execute(f"SHOW COLUMNS FROM {table }")
    res = cursor.fetchall()
    if only_name:
      #res = [row[0] for row in res]
      #map is cooler
      res = list(map(lambda x: x[0], res))
    return res
  
  except Exception as e:
    if error:
      raise Exception("Read Columns Error: ", e) from e

def read_rows(*, table: str, columns: list = ['*'], limit:int = None, error:bool=True, cursor=None, filter_args:List[str]=None) -> List[Tuple[str]]:
  try:
    if not cursor:
      cursor = get_cursor()
    limit_str = f"LIMIT {limit}" if limit else ""
    where_str = f"WHERE {', '.join(filter_args)}" if filter_args else ""
    cursor.execute(f"SELECT {', '.join(columns)} FROM {table} {where_str} {limit_str}")
    rows = cursor.fetchall()
    return rows
    
  
  except Exception as e:
    if error:
      raise Exception("Read Rows Error: ", e) from e

#* Create/Drop functions

def create_table(*, table:str, columns_config_str: Union[str, List[str]], error:bool=True, cursor=None) -> bool:
  try:
    if not cursor:
      cursor = get_cursor()
    columns_error = "Columns config str must be specified when creating a table. It hast to be either 1 conform mysql string or a list of strs for each column" 
    
    if not columns_error:
      raise ValueError(columns_error) 
    
    if isinstance(columns_config_str, list):
      if not any(col for col in columns_config_str):
        raise ValueError(columns_config_str)
      columns_config_str = ', '.join(columns_config_str)

    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table} ({columns_config_str})")
    return True
  
  except Exception as e:
    if error:
      raise Exception("Create Table Error: ", e) from e
    return False

def drop_table(*, table:str, error:bool=True, cursor=None) -> bool:
  try:
    if not cursor:
      cursor = get_cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {table}")
    return True
  
  except Exception as e:
    if error:
      raise Exception("Drop Table Error: ", e) from e
    return False

def add_row(*, table:str, args:set, error:bool=True, cursor=None) -> bool:
  try:
    if not cursor:
      cursor = get_cursor()
    cursor.execute("SHOW COLUMNS FROM %s" % table)
    columns = [row[0] for row in cursor.fetchall() if row[5] != 'auto_increment']

    if len(args) != len(columns):
        raise ValueError("The length of the args doesnt match the length of the columns")

    placeholders = ', '.join(['%s'] * len(columns))
    columns_str = ', '.join(columns)
    sql = f"INSERT INTO {table} ({columns_str}) VALUES ({placeholders})"

    cursor.execute(sql, args)
    return True

  except Exception as e:
    if error:
      raise Exception("Add Row Error: ", e) from e
    return False

def delete_row(*, table:str, object_id:int, error:bool=True, cursor=None) -> bool:
  try:
    if not cursor:
      cursor = get_cursor()
    sql = f"DELETE FROM {table} WHERE id = {object_id}"
    cursor.execute(sql)
    return True

  except Exception as e:
    if error:
      raise Exception("Delete Row Error: ", e) from e
    return False

def add_column(*, table:str, column:str, column_type:str=None, column_constraint:str="", error:bool=True, cursor=None) -> False:
  try:
    if not cursor:
      cursor = get_cursor()
    if not column_type:
      raise ValueError("Column type must be specified when adding a column.")
    if column not in [col[0] for col in read_columns(table=table)]:
      cursor.execute(f"ALTER TABLE {table} ADD {column} {column_type} {column_constraint}")
    return True

  except Exception as e:
    if error:
      raise Exception("Add Column Error: ", e) from e
    return False

def drop_column(*, table:str, column:str, error:bool=True, cursor=None) -> bool:
  try:
    if not cursor:
      cursor = get_cursor()
    if column in [col[0] for col in read_columns(table=table)]:
      cursor.execute(f"ALTER TABLE {table} DROP COLUMN {column}")
    return True

  except Exception as e:
    if error:
      raise Exception("Drop Column Error: ", e) from e
    return False

#* Special funcs ig

def exec_cmd(*, sql_str: str, error:bool=True, cursor=None) -> Any:
  try:
    if not cursor:
      cursor = get_cursor()
    cursor.execute(sql_str)
    return cursor.fetchall()
  
  except Exception as e:
    if error:
      raise Exception("Exec Cmd Error: ", e) from e