from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from sqlalchemy.orm import Session
import hashlib
from sqlalchemy import select

SQLALCHEMY_DATABASE_URL = "sqlite:///sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

Base = declarative_base(bind = engine)

class Post(Base):
    __tablename__ = "Post"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, unique=False, index=True)
    
    url = Column(String)

    def __repr__(self):
        return "<User(id='%s', content='%s', url='%s')>" % (
            self.id,
            self.content,
            self.url,
        )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()

metadata = Base.metadata
metadata.create_all(engine)



def createpost(content):
    

    u = Post(content= content, url = "none")
    session.add(u)
    session.flush()
    m = hashlib.sha256()
    
    m.update(bytes(u.id))
    u.url = m.hexdigest()
    print(u.url)
    
    session.commit()

    return u.url

def get_content(url):
    #print(Post.query.filter_by(url == url))
    x =  select(Post).where(Post.url == url)
    for content in session.query(Post).filter(Post.url == url):
        return content

