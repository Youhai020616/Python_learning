


from pymysql import Connection

conn = Connection (
    host ="localhost",
    port = 3306,
    user = "root",
    password = "258369",
    database = "test",
    charset = "utf8"
)
# print(conn.get_server_info())

#执行sql语句
#获取游标对象
cursor = conn.cursor()

#选择数据库
conn.select_db("test")

#执行sql语句
cursor.execute("create table test_pymysql(id int)")
