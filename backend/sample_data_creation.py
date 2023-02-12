import model
from database.database import SessionLocal, create_table, drop_table


def migrate_db():
    drop_table()
    create_table()


def insert_sample():
    session = SessionLocal()

    users: list[model.User] = [
        model.User(name="sample_user_1", email="sample_1@example.com"),
        model.User(name="sample_user_2", email="sample_2@example.com"),
        model.User(name="sample_user_3", email="sample_3@example.com"),
    ]

    items: list[model.Item] = [
        model.Item(name="sample_item_1", owner_id=1, available=True),
        model.Item(name="sample_item_2", owner_id=1, available=True),
        model.Item(name="sample_item_3", owner_id=2, available=True),
    ]

    rentals: list[model.Rental] = [
        model.Rental(
            user_id=2,
            item_id=1,
            rented_date="2023-01-01",
            return_plan_date="2023-01-10",
            returned_date="2023-01-08",
        ),
        model.Rental(
            user_id=3,
            item_id=1,
            rented_date="2023-01-30",
            return_plan_date="2023-02-10",
        ),
    ]
    session.begin()
    session.bulk_save_objects(users)
    session.bulk_save_objects(items)
    session.bulk_save_objects(rentals)
    session.commit()
    session.close()


if __name__ == "__main__":
    migrate_db()
    insert_sample()
