import  pymysql as ps

try:
    cn=ps.connect(host='localhost',user='sa',password='Demon.2000',db='Python')
    
    cmd=cn.cursor()
    
    query="select * from products"
    
    cmd.execute(query)
    
    rows=cmd.fetchall()
    
    # print(rows)
    for row in rows:
        for col in row:
            print(col,end=' ')
        print()
    
    cn.close()

except Exception as e:
    print(e)