from sqlalchemy import *



#db = create_engine('sqlite:///tutorial.db')

db.echo =False # Try changing this to True and see What happens

metadata = BoundMEtaData(db)
