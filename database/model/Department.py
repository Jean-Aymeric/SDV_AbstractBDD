from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, Session

from database import Engine
from database.model.AbstractEntity import AbstractEntity


class Department(AbstractEntity):
    __tablename__ = "departments_info"
    dept_no: Mapped[str] = mapped_column(primary_key=True)
    dept_name: Mapped[str] = mapped_column(String(40))
    emp_no: Mapped[int] = mapped_column(ForeignKey('employees_info.emp_no'))

    @property
    def Dept_no(self) -> str:
        return self.dept_no

    @property
    def Dept_name(self) -> str:
        return self.dept_name

    @property
    def Emp_no(self) -> int:
        return self.emp_no

    @classmethod
    def getAll(cls):
        with Session(Engine.getEngine()) as session:
            return session.query(cls).all()

    def __repr__(self):
        return f"Department(dept_no={self.dept_no}, dept_name={self.dept_name}, emp_no={self.emp_no})"
