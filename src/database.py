# from sqlalchemy import create_engine, String
# from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
# from sqlalchemy.orm import DeclarativeBase, sessionmaker

# from config import settings

# async_engine = create_async_engine(
#     echo = False,
#     url=settings.DATABASE_URL_sqlalchemy,
# )


# async_session = async_sessionmaker(async_engine, expire_on_commit=False)

# class Base(DeclarativeBase):
#     pass