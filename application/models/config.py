import web

db_host = 'localhost'
db_name = 'contacts_kuorra'
db_user = 'kuorra'
db_pw = 'kuorra.2019'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )