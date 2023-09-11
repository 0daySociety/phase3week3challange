from models import Restaurant,Review,Customer,Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__=="__main__":


    try:
        engine=create_engine('sqlite:///hotelDatabase.db')
        Base.metadata.create_all(engine)
        Session=sessionmaker(bind=engine)
        session=Session()


        
    except Exception as e:
        print("we got this error ", str(e))



