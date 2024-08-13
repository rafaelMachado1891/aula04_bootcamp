from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.sql import func
from database import Base

class ProductModel(Base):
    __tablename__ = "obras"

    id = Column(Integer, primary_key=True)
    filial = Column(String)
    postes = Column(Boolean)
    ligacao = Column(Boolean)
    inauguracao = Column(String)
    obra = Column(String)
    responsavel = (String)
    link = (String)
    projetos = (String)
    orcamento =(String)
    material =(String)
    ti = (Boolean)
    equipe = (String)
    orcamento_final = (String)
    status = (String)
    created = Column(DateTime(timezone=True),default=func.now())