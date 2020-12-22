#!/usr/bin/env python
import snowflake.connector

ctx = snowflake.connector.connect(
        user='SridharSnowflake',
        password='Snowflake20*',
        account='ki44772.us-east-2.aws',
        warehouse="SRIDHAR",
        database="TEST_SNOWFLAKE",
        schema="TEST",
        session_parameters={
        'QUERY_TAG': 'Snowflake Testing' }
        )
       
if __name__ == "__main__":
    SnowFlake()
