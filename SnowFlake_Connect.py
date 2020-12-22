
#!/usr/bin/env python
import snowflake.connector
import PythonConnector_Validator

def  Snowflake_Connect():
# Gets the version
  PythonConnector_Validator.ctx
  print("Connected to snowflake")

def main():
  # Connect to snowflake
  print("Connect to Snowflake Account")
  Snowflake_Connect()
  cs= PythonConnector_Validator.ctx.cursor()
  try:
      cs.execute("SELECT current_version()")
      cs.execute("Alter session set query_tag='Snowflake Testing'")
      cs.execute("USE WAREHOUSE SRIDHAR")
      cs.execute("USE DATABASE TEST_SNOWFLAKE")
      cs.execute("USE SCHEMA TEST")
      one_row = cs.fetchone()
      print(one_row[0])
      col1, col2 = cs.execute("SELECT c1, c2 FROM LANGUAL").fetchone()
      print('{0}, {1}'.format(col1, col2))
      cs.execute("select c1,c2 from langual")
      for (col1, col2) in cs:
        print('{0}, {1}'.format(col1, col2))
    
      sql= "INSERT INTO LANGUAL VALUES ('Tom','Cruise')"   
      cs.execute(sql)
      cs.execute("select c1,c2 from langual")
      for (col1, col2) in cs:
        print('{0}, {1}'.format(col1, col2))
        print(cs.sfqid)  
  
  except snowflake.connector.errors.ProgrammingError as e:
      # default error message
      print(e)
      # customer error message
      print('Error {0} ({1}): {2} ({3})'.format(e.errno, e.sqlstate, e.msg, e.sfqid))

  finally:
    cs.close()
    PythonConnector_Validator.ctx.close()
  

if __name__ == "__main__":
  main()