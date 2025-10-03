from sqlalchemy import select, update, delete    
from database.models import Product
from sqlalchemy.ext.asyncio import AsyncSession

async def add_orm_product(session: AsyncSession, data: dict):
    obj = Product(
        name=data["name"],
        description=data["description"],
        price=float(data["price"]),
        image=data["image"],
    )
    session.add(obj)
    await session.commit()  


async def orm_get_all_products(session: AsyncSession):
    query = select(Product)
    result = await session.execute(query)
    return result.scalars().all()

async def orm_get_product(session: AsyncSession, product_id: int):
    query = select(Product).where(Product.id == product_id)
    result = await session.execute(query)
    return result.scalar_one_or_none()

async def orm_update_product(session: AsyncSession, product_id: int, data: dict):
    query = (
        update(Product)
        .where(Product.id == product_id)
        .values(
            name=data.get("name"),
            description=data.get("description"),
            price=float(data.get("price")) if data.get("price") else None,
            image=data.get("image"),
        )
        .execution_options(synchronize_session="fetch")
    )
    await session.execute(query)
    await session.commit()


async def orm_delete_product(session: AsyncSession, product_id: int):
    query = delete(Product).where(Product.id == product_id)
    await session.execute(query)
    await session.commit()