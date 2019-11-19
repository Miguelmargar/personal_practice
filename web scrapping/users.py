from passw import *
import pymysql


class Users:
    
    def __init__(self):
        pass
    
    def sign_user_up(self, name, email, password):
        user = 'root'
        password = db_key
        host = '127.0.0.1'
        database = 'myfinance'
        
        try:
            con = pymysql.connect(host=host, database=database, user=user, password=password)
        except Exception as e:
            sys.exit(e)
            
        query = """SELECT user_name, user_email
                FROM myfinance.users
                WHERE myfinance.users.user_name = %s
                    and myfinance.users.user_email = %s"""
                
        cur = con.cursor()
        cur.execute(query, (name, email),)
        data = cur.fetchall()
        cur.close()
        
        if len(data) > 0:
            return False
        elif len(data) == 0:
            try:
                insert = """INSERT INTO users ( user_name, user_email, user_password)
                            VALUES
                            (%s, %s, %s);"""
                
                cur = con.cursor()
                cur.execute(insert, (name, email, password),)
                cur.close()
                con.commit()
                
                return True
            except:
                return False
            
            
        