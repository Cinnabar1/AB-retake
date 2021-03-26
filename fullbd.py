from managers.DatabaseManager import DatabaseManager


from app import db
from models.interval import Interval


db_manager = DatabaseManager(db)


db_manager.add_interval(interval="9:30 - 11:05")
db_manager.add_interval(interval="11:20 - 12:55")
db_manager.add_interval(interval="13:10 - 14:45")
db_manager.add_interval(interval="15:25 - 17:00")
db_manager.add_interval(interval="17:15 - 18:45")
