import sqlite3
from datetime import datetime

DB_FILE = "weather.db"

def init_db():
    """如果queries表不存在就创建新表"""
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("create table if not exists queries(id integer primary key autoincrement,city text not null,temp real not null,queried_at text not null)")
    conn.close()

def save_query(city,temp):
    """插入记录"""
    try:
        fTemp = float(temp)
    except (ValueError, TypeError):
        print("请检查输入温度的类型")
        return None
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    try:
        cur.execute("insert into queries(city,temp,queried_at) values(?,?,?)",(city,fTemp,datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()
        return True;
    except sqlite3.Error as e:
        conn.rollback();
        return False
    finally:
        conn.close()

def get_history(limit=10):
    """查询最新的limit条,最新的排最前"""
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("select city,temp,queried_at from queries order by id desc limit ?",(limit,))
    rows = cur.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    init_db()
    save_query("北京",12.5)
    save_query("南京",22.5)
    save_query("测试", "abc")

    for history in get_history():
        print(history)


