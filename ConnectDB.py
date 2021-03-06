import psycopg2
try:
    connection = psycopg2.connect(user="webadmin",
                                  password="VRMxoy95713",
                                  host="10.100.2.214",
                                  #host="node8619-advweb-25.app.ruk-com.cloud",
                                  port="5432",
                                  database="CloudDB")
    cursor = connection.cursor()
    print(connection.get_dsn_parameters(), "\n")

    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to -", record, "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while connectiong to PostgreSQL", error)
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
