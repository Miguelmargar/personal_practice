from passw import *
import pymysql, hashlib, binascii, os


class Users:
    
    def __init__(self):
        pass
    
    def sign_user_up(self, name, email, passw):
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
                passw = self.hash_password(passw)
                insert = """INSERT INTO users ( user_name, user_email, user_password)
                            VALUES
                            (%s, %s, %s);"""
                
                cur = con.cursor()
                cur.execute(insert, (name, email, passw),)
                cur.close()
                con.commit()
                
                return True
            except:
                return False
            
            
    def hash_password(self, password):
        """Hash a password for storing."""
        
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
        
        pwdhash = binascii.hexlify(pwdhash)
        
        return (salt + pwdhash).decode('ascii')
    
    
    def verify_password(self, stored_password, provided_password):
        """Verify a stored password against one provided by user"""
        
        salt = stored_password[:64]
        
        stored_password = stored_password[64:]
        
        pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), 
                salt.encode('ascii'), 100000)
        
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        
        return pwdhash == stored_password
    
    
    
    
    
        