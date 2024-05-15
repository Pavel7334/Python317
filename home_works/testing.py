# from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
# from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base
# from datetime import datetime
#
# Base = declarative_base()
#
#
# class User(Base):
#     __tablename__ = 'users'
#
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, unique=True, index=True, nullable=False, doc="Имя пользователя")
#     password = Column(String, nullable=False, doc="Хэшированный пароль пользователя")
#     balance = Column(Float, default=0.0, doc="Баланс пользователя")
#     characters = relationship("Character", back_populates="owner", doc="Персонажи пользователя")
#     trades = relationship("Trade", back_populates="user", doc="Трейды пользователя")
#
#
# class Character(Base):
#     __tablename__ = 'characters'
#
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False, doc="Имя персонажа")
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False, doc="ID пользователя, владеющего персонажем")
#     items = relationship("Item", back_populates="character", doc="Предметы, надетые на персонажа")
#     owner = relationship("User", back_populates="characters", doc="Владелец персонажа")
#
#
# class Item(Base):
#     __tablename__ = 'items'
#
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False, doc="Название предмета")
#     description = Column(String, doc="Описание предмета")
#     character_id = Column(Integer, ForeignKey('characters.id'), nullable=False,
#                           doc="ID персонажа, который носит предмет")
#     character = relationship("Character", back_populates="items", doc="Персонаж, носящий предмет")
#     trade = relationship("Trade", uselist=False, back_populates="item", doc="Трейд, в котором участвует предмет")
#
#
# class Trade(Base):
#     __tablename__ = 'trades'
#
#     id = Column(Integer, primary_key=True, index=True)
#     sender_id = Column(Integer, ForeignKey('users.id'), nullable=False, doc="ID отправителя предмета")
#     recipient_id = Column(Integer, ForeignKey('users.id'), nullable=False, doc="ID получателя предмета")
#     item_id = Column(Integer, ForeignKey('items.id'), nullable=False, doc="ID предмета, передаваемого в трейде")
#     commission = Column(Float, default=0.0, doc="Комиссия с трейда")
#     created_at = Column(DateTime, default=datetime.utcnow, doc="Дата и время создания трейда")
#     user = relationship("User", back_populates="trades", doc="Пользователь, отправивший или получивший предмет")
#     item = relationship("Item", back_populates="trade", doc="Предмет, участвующий в трейде")
#
#
# class BalanceHistory(Base):
#     __tablename__ = 'balance_history'
#
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False, doc="ID пользователя")
#     amount = Column(Float, nullable=False, doc="Сумма изменения баланса")
#     timestamp = Column(DateTime, default=datetime.utcnow, doc="Дата и время изменения баланса")
