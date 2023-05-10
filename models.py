from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase
 
class Base(DeclarativeBase):
    pass


class Phone(Base):
    __tablename__="phone"

    id: Mapped[int] = mapped_column(primary_key=True)
    add_id: Mapped[Optional[int]]
    add_link: Mapped[Optional[str]]
    title: Mapped[Optional[str]]
    image: Mapped[Optional[str]]
    price: Mapped[Optional[str]]

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, add_id={self.add_id!r}, link={self.add_link!r}, title={self.title!r}, price={self.price})"