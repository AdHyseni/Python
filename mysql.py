import pyodbc
try:
    cnxn_str = ("Driver={SQL Server Native Client 11.0};"
                "Server=localhost;"
                "Database=Python;"
                "Trusted_Connection=yes;")
    cnxn = pyodbc.connect(cnxn_str)
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM test")
    table = cursor.fetchall()
    for i in table:
        print(i)
    cnxn.commit()
    print("Sukses")
except Exception as e:
    print(e)
