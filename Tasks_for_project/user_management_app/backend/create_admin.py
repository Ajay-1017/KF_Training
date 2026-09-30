from getpass import getpass

from sqlalchemy import select

from database import sessionLocal
from models import User, UserInfo
from auth import hash_password


def create_admin():

    email = input("Enter admin email: ").strip()
    password = getpass("Enter admin password: ")
    full_name = input("Enter admin full name: ").strip()
    phone = input("Enter admin phone: ").strip()

    with sessionLocal() as db:

        existing_user = db.execute(
            select(User).where(User.email == email)
        ).scalars().first()

        if existing_user:
            print("User already exists.")
            return

        try:
            user = User(
                email=email,
                hash_password=hash_password(password),
                is_active=True
            )

            db.add(user)
            db.flush()

            user_info = UserInfo(
                user_id=user.id,
                full_name=full_name,
                phone=phone,
                role="admin"
            )

            db.add(user_info)

            db.commit()

            print("Admin created successfully.")

        except Exception:
            db.rollback()
            print("Failed to create admin.")
            raise


if __name__ == "__main__":
    create_admin()