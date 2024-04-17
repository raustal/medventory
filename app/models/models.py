from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from ..db.database import session


class Base(DeclarativeBase):
    pass


class Campus(Base):
    '''Campus model to store campus information.
    id: int - primary key
    campus_name: str - campus name: Ex. 'University of Texas'
    campus_abbreviation: str - campus abbreviation: Ex. 'UT'
    location: Location - location of the campus. 
    '''
    __tablename__ = 'campuses'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    campus_name: Mapped[str] = mapped_column('Campus Name', String, nullable=False)
    campus_abbreviation: Mapped[str] = mapped_column('Campus Abbreviation', String, nullable=False)
    location = relationship('Location', backref='campus')

    def __repr__(self) -> str:
        return f'{self.campus_name}'


class Location(Base):
    '''Location model to store location information.
    id: int - primary key
    '''
    __tablename__ = 'locations'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    city: Mapped[str] = mapped_column('City', String, nullable=False)
    state: Mapped[str] = mapped_column('State', String, nullable=False)
    state_abbreviation: Mapped[str] = mapped_column('State Abbreviation', String, nullable=False)
    zip_code: Mapped[str] = mapped_column('Zip Code', String, nullable=False)
    campus_id: Mapped[int] = mapped_column('Campus ID', Integer, ForeignKey('campuses.id'), nullable=False)

    def __repr__(self) -> str:
        return f'{self.city}, {self.state}'


class Medication(Base):
    '''Medication model to store medication information.
    id: int - primary key
    generic_name: str - generic name of the medication: Ex. 'acetaminophen'
    brand_name: str - brand name of the medication: Ex. 'Tylenol'
    strength: int - strength of the medication: Ex. 500
    unit: str - unit of the medication: Ex. 'mg'
    form: str - form of the medication: Ex. 'tablet', 'capsule'
    barcode: str - barcode of the medication: Ex. '0123456789'

    '''
    __tablename__ = 'medications'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    generic_name: Mapped[str] = mapped_column('Generic Name', String, nullable=False)
    brand_name: Mapped[str] = mapped_column('Brand Name', String, nullable=False)
    strength: Mapped[int] = mapped_column('Strength', Integer, nullable=False)
    unit: Mapped[str] = mapped_column('Unit', String, nullable=False)
    form: Mapped[str] = mapped_column('Form', String, nullable=False)
    barcode: Mapped[str] = mapped_column('Barcode', String, nullable=False)
    sku: Mapped[str] = mapped_column('SKU', String, nullable=False)

    def __repr__(self):
        return f'{self.generic_name} {self.strength} {self.unit} - {self.form}'


class Inventory(Base):
    '''Inventory model to store inventory information.'''
    __tablename__ = 'inventory'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    medication_id: Mapped[int] = mapped_column('Medication ID', Integer, ForeignKey('medications.id'), nullable=False)
    campus_id: Mapped[int] = mapped_column('Campus ID', Integer, ForeignKey('campuses.id'), nullable=False)
    quantity: Mapped[int] = mapped_column('Quantity', Integer, nullable=False)
    medication = relationship('Medication', backref='inventory')
    campus = relationship('Campus', backref='inventory')

    def __repr__(self) -> str:
        return f'{self.medication} - {self.quantity} count in {self.campus}'


class Vendor(Base):
    '''Vendor model to store vendor information.'''
    __tablename__ = 'vendors'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    vendor_name: Mapped[str] = mapped_column('Vendor Name', String, nullable=False)
    vendor_contact: Mapped[str] = mapped_column('Vendor Contact', String, nullable=False)
    vendor_phone: Mapped[str] = mapped_column('Vendor Phone', String, nullable=False)
    vendor_email: Mapped[str] = mapped_column('Vendor Email', String, nullable=False)
    medication = relationship('Medication', backref='vendor')

    def __repr__(self) -> str:
        return f'{self.vendor_name}'

# Create the tables in the database.
Base.metadata.drop_all(session.get_bind())
Base.metadata.create_all(session.get_bind())

