from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, update, delete, and_

from models import User, create_async_session
from schemas import UserInDBSchema, UserSchema


class CRUDUser(object):

    @staticmethod
    @create_async_session
    async def add(user: UserSchema, session: AsyncSession = None) -> UserInDBSchema | None:
        users = User(
            **user.dict()
        )
        session.add(users)
        try:
            await session.commit()
        except IntegrityError as e:
            print(e)
        else:
            await session.refresh(users)
            return UserInDBSchema(**users.__dict__)

    @staticmethod
    @create_async_session
    async def delete(name_user: str, session: AsyncSession = None) -> None:
        await session.execute(
            delete(User)
            .where(User.name_user == name_user)
        )
        await session.commit()

    @staticmethod
    @create_async_session
    async def get(user_name: str = None,
                  session: AsyncSession = None) -> UserInDBSchema | None:
        users = await session.execute(
            select(User)
            .where(User.name_user == user_name)
        )
        if user := users.first():
            return UserInDBSchema(**user[0].__dict__)

    @staticmethod
    @create_async_session
    async def get_all(session: AsyncSession = None) -> list[UserInDBSchema]:
        users = await session.execute(
            select(User)
            .order_by(User.id)
        )
        return [UserInDBSchema(**user[0].__dict__) for user in users]

    @staticmethod
    @create_async_session
    async def update(user: UserInDBSchema, session: AsyncSession = None) -> None:
        await session.execute(
            update(User)
            .where(User.id == user.id)
            .values(**user.dict())
        )
        await session.commit()
