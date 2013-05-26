from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Database:

    engine = create_engine('sqlite:///nmap-logger.db', echo=True)
    Base = declarative_base()

    Session = sessionmaker(bind=engine)
    session = Session()

    class Host(Base):
        __tablename__ = 'hosts'

        id = Column(Integer, primary_key=True)
        ip = Column(String)
        mac = Column(String)
        vendor = Column(String)
        hostname = Column(String)
        os = Column(String)

        def __init__(self, ip, mac, vendor, hostname, os):
            self.ip = ip
            self.mac = mac
            self.vendor = vendor
            self.hostname = hostname
            self.os = os

        def __repr__(self):
            return self.ip

    Base.metadata.create_all(engine)

    def __init__(self):
        pass

    def add_host(self, ip, mac, vendor, hostname, os):
        new_host = self.Host(ip, mac, vendor, hostname, os)
        self.session.add(new_host)
        self.session.commit()
