from database.database import SessionLocal, create_table, drop_table
from model import ItemDTO, RentalDTO, UserDTO


def migrate_db():
    drop_table()
    create_table()


def insert_sample():
    session = SessionLocal()

    users: list[UserDTO] = [
        UserDTO(name="sample_user_1", email="sample_1@example.com"),
        UserDTO(name="sample_user_2", email="sample_2@example.com"),
        UserDTO(name="sample_user_3", email="sample_3@example.com"),
    ]

    items: list[ItemDTO] = [
        ItemDTO(
            name="sample_item_1",
            owner_id=1,
            available=True,
            image_url="sample_item_1.com",
            description="sample_item_1 description",
        ),
        ItemDTO(name="sample_item_2", owner_id=1, available=True),
        ItemDTO(name="sample_item_3", owner_id=2, available=True),
        ItemDTO(
            name="sample_item_4",
            owner_id=2,
            available=False,
            image_url="sample_item_4.com",
        ),
    ]

    rentals: list[RentalDTO] = [
        RentalDTO(
            user_id=2,
            item_id=1,
            rented_date="2023-01-01",
            return_plan_date="2023-01-10",
            returned_date="2023-01-08",
        ),
        RentalDTO(
            user_id=3,
            item_id=1,
            rented_date="2023-01-30",
            return_plan_date="2023-02-10",
        ),
        RentalDTO(
            user_id=3,
            item_id=2,
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
