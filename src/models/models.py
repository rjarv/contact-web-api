from sqlalchemy.ext.declarative import declarative_base as _declarative_base
from sqlalchemy import Column as _Column, Integer as _Integer, String as _String

_Base = _declarative_base()


class Contact(_Base):
    __tablename__ = 'address_book'
    __table_args__ = {'schema': 'address'}

    id = _Column('uid', primary_key=True)
    first_name = _Column('first_name', _String(30))
    middle_name = _Column('middle_name', _String(30))
    last_name = _Column('last_name', _String(30))
    address1 = _Column('address1', _String(75))
    address2 = _Column('address2', _String(50))
    city = _Column('city', _String(50))
    st_province = _Column('st_prvnce', _String(75))
    country = _Column('country', _String(75))
    zip_code = _Column('zip', _String(10))
    fam_key = _Column('fam_key', _Integer)
    spouse_key = _Column('spouse_key', _Integer)

    def __repr__(self):
        full_name = ['%s' % self.first_name, '%s' % self.last_name]
        return "<Contact(name='%s', city='%s', state='%s')>" % (
            ' '.join(filter(None, full_name)), self.city, self.st_province
        )


class Family(_Base):
    __tablename__ = 'family_key'
    __table_args__ = {'schema': 'address'}

    id = _Column('uid', primary_key=True)
    last_name = _Column('lastname', _String(30))

    def __repr__(self):
        return "<Family(id='%s', last_name='%s')>" % (
            self.id, self.last_name
        )


class SpousalLineage(_Base):
    __tablename__ = 'spousal_lineage_key'
    __table_args__ = {'schema': 'address'}

    id = _Column('uid', primary_key=True)
    last_name = _Column('lastname', _String(30))

    def __repr__(self):
        return "<SpousalLineage(id='%s', last_name='%s')>" % (
            self.id, self.last_name
        )