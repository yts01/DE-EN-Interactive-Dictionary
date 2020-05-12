import mysql.connector



def translate(w):
    global value

    db = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='#####'
    )
    mycursor = db.cursor()

    mycursor.execute('''
    SELECT translation
    FROM deutch.dict
    WHERE word = '{}'
    '''.format(w))


    for x in mycursor:
        return x[0]

def insert_val(tag,word,gender,plural,translation):
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='#####'
    )
    mycursor = db.cursor()

    mycursor.execute('''
    INSERT INTO deutch.dict(tag,word,gender,plural,translation)
    VALUES (%s,%s,%s,%s,%s)
    ''',(tag,word,gender,plural,translation))
    db.commit()

#translate('angst')

#insert_val('r','tryy','g','ytryyyy','yrtrt')