import mysql.connector
from flask import current_app, g
from typing import List, Tuple

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
    res = cursor.fetchall()
    get_db().commit()
    return res

  except Exception as e:
    if error:
      raise Exception("Read Tables Error: ", e) from e

def read_rows(*, table: str, columns: list = ['*'], limit:int = None, filter_args:List[str]=None, error:bool=True, cursor=None, ) -> List[Tuple[str]]:
  try:
    if not cursor:
      cursor = get_cursor()
    limit_str = f"LIMIT {limit}" if limit else ""
    where_str = f"WHERE {' AND '.join(filter_args)}" if filter_args else ""
    cursor.execute(f"SELECT {', '.join(columns)} FROM {table} {where_str} {limit_str}")
    rows = cursor.fetchall()
    get_db().commit()
    return rows
    
  except Exception as e:
    if error:
      raise Exception("Read Rows Error: ", e) from e