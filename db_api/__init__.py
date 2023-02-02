import logging

from peewee import SqliteDatabase

from data import DATABASE_PATH

db = SqliteDatabase(database=DATABASE_PATH, pragmas={'foreign_keys': 1})

from .db_models import TempHumSensor, TempHumValues, GroundSensor, GroundValues


def on_startup_sqlite():
    db.connect()
    db.create_tables([
        TempHumSensor,
        TempHumValues,
        GroundSensor,
        GroundValues
    ], safe=True)
    logging.info('DB is connected successfully')


def on_shutdown_sqlite():
    db.close()
    logging.info('DB connection closed successfully')


__all__ = [on_startup_sqlite, on_shutdown_sqlite, TempHumSensor, TempHumValues, GroundSensor, GroundValues]
