import web

"""db_host = 'localhost'
db_name = 'ferreteria_dbp'
db_user = 'quetzal'
db_pw = 'quetzal.2019'"""

db_host = 'nj5rh9gto1v5n05t.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'gsq6mfw949qkkwst'
db_user = 'z9qsk81jk3dyfuuq'
db_pw = 'z0wcrkrivvrcm7fu'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )