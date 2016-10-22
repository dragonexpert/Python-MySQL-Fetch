import re
import MySQLdb

def fieldconverter( result ):
    # First check if its a select all
    if re.search("\*", result):
        # Get the table structure
        tablename = re.sub(r'\A(SELECT\s){1}(.*?){1,}\sFROM\s|WHERE(.*?)\Z', "", result)
        sql2 = "DESCRIBE " + tablename
        cursor.execute(sql2)
        sqlresult = cursor.fetchall()
        z = 0
        result = {}
        for looper in sqlresult:
            fieldname = sqlresult[z][0]
            result[fieldname] = data[z]
            z += 1

    else:
        statement = re.sub(r'\A(SELECT\s){1}|FROM(.*?)\Z', "", result)
        # Now we have  a list of fields.  Loop through them
        splitstatement = statement.split(", ")
        x = 0
        result = {}
        for a in splitstatement:
            fieldname = re.sub(r'\s', "", a)
            result[fieldname] = data[x]
            x += 1

    return result

# Connect to the database
db = MySQLdb.connect(hostname, database user, password, database name)

cursor = db.cursor()
# usage example
sql = "SELECT uid, username, email FROM users WHERE username='dragonexpert'"
sql = "SELECT * FROM users WHERE username='dragonexpert'"
cursor.execute(sql)
data = cursor.fetchone()
result = fieldconverter(sql)
print "Username: %s " % result['username'] + " Uid: %i" % result['uid'] + " Email: %s " % result['email']
db.close()
