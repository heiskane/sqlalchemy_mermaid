"""Example database"""

import sys
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Date,
    Boolean,
)
from sqlalchemy.ext.declarative import declarative_base

sys.path.insert(0, "..")

# TODO: Deal with importing later
from sqlalchemy_mermaid import create_mermaid_diagram  # noqa


Base = declarative_base()


class Trip(Base):
    """
    ORM class represents trip
    """

    __tablename__ = "trips"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    description = Column(String(1024))
    advertised_price = Column(Integer)
    start_date = Column(Date)
    end_date = Column(Date)

    country_id: int = Column(ForeignKey("countries.id"))


class TripStaff(Base):
    """Many-to-Many middleman ORM class for staff in a trip"""

    __tablename__ = "trip_staff"

    trip_id: int = Column(ForeignKey("trips.id"), primary_key=True)
    staff_id: int = Column(ForeignKey("staff.id"), primary_key=True)


class Registration(Base):
    """Registration ORm class"""

    __tablename__ = "registrations"

    cancelled = Column(Boolean, default=False)
    price_paid = Column(Integer)

    customer_id: int = Column(ForeignKey("customers.id"), primary_key=True)
    trip_id: int = Column(ForeignKey("trips.id"), primary_key=True)
    hotel_id: int = Column(ForeignKey("hotels.id"), nullable=True)


class Customer(Base):
    """Customer ORM class"""

    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    fname = Column(String)
    lname = Column(String)
    phone_num = Column(String)
    email = Column(String)


class Country(Base):
    """Country ORM class"""

    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)


class Hotel(Base):
    """Hotel ORM class"""

    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone_num = Column(String)
    email = Column(String)
    address = Column(String)

    country_id: int = Column(ForeignKey("countries.id"))


class Staff(Base):
    """Staff ORM class"""

    __tablename__ = "staff"

    id = Column(Integer, primary_key=True, index=True)
    fname = Column(String)
    lname = Column(String)
    phone_num = Column(String)
    email = Column(String)

    role_id: int = Column(ForeignKey("staff_roles.id"))


class StaffRole(Base):
    """StaffRole ORM class"""

    __tablename__ = "staff_roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False, unique=True)


def main() -> None:
    mermaid_diagram = create_mermaid_diagram(Base)

    print("```mermaid")
    print(mermaid_diagram)
    print("```")


if __name__ == "__main__":
    main()
