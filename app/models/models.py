from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from app.db.database import session


class Base(DeclarativeBase):
    pass


class Campus(Base):
    '''Campus model to store campus information.'''
    __tablename__ = 'campuses'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    campus_name: Mapped[str] = mapped_column('Campus Name', String, nullable=False)
    campus_abbreviation: Mapped[str] = mapped_column('Campus Abbreviation', String, nullable=False)

    def __repr__(self) -> str:
        return f'{self.campus_name}'


class Medication(Base):
    '''Medication model to store medication information.'''
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

    def __repr__(self) -> str:
        return f'{self.vendor_name}'