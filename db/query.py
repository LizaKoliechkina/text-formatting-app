from sqlalchemy import exc, orm, update

import db.schemas as sch


def save_element(text: str, db: orm.Session):
    try:
        db_obj = sch.FormatText(
            text=text,
            done=False,
        )
        db.add(db_obj)
        db.commit()
    except exc.SQLAlchemyError as ex:
        db.rollback()
        raise Exception(f'Failed to save element to database: {ex}')
    return db_obj


def get_element(id: int, db: orm.Session):
    try:
        obj = db.query(sch.FormatText).filter(sch.FormatText.id == id).first()
    except exc.SQLAlchemyError as ex:
        db.rollback()
        raise Exception(f'Failed to retrieve element {id} from database: {ex}')
    return obj


def update_request_status(id: int, db: orm.Session):
    try:
        db.query(sch.FormatText).filter(sch.FormatText.id == id).update({sch.FormatText.done: True})
        db.commit()
    except exc.SQLAlchemyError as ex:
        db.rollback()
        raise Exception(f'Failed to update status of element {id}: {ex}')
    return


def save_format_history(format_hist: sch.History, db: orm.Session):
    try:
        db_obj = format_hist
        db.add(db_obj)
        db.commit()
    except exc.SQLAlchemyError as ex:
        db.rollback()
        raise Exception(f'Failed to save format history: {ex}')
    return db_obj


def get_history(id: int, db: orm.Session):
    try:
        history = db.query(sch.History).filter(sch.History.text_id == id).order_by(sch.History.queue).all()
    except exc.SQLAlchemyError as ex:
        db.rollback()
        raise Exception(f'Failed to retrieve format history for the element {id}: {ex}')
    return history
