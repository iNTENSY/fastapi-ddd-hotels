from app.domain.users.entity import Users


async def user_from_dict_to_entity(data: dict) -> Users:
    return await Users.create(
        id=data["id"],
        email=data["email"],
        hashed_password=data["hashed_password"],
    )
