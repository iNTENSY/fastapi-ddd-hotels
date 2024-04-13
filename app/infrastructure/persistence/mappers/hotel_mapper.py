from app.domain.hotels.entity import Hotels


async def hotel_from_dict_to_entity(data: dict) -> Hotels:
    return await Hotels.create(
        id=data["id"],
        name=data["name"],
        location=data["location"],
        services=data["services"],
        rooms_quantity=data["rooms_quantity"],
        image_id=data["image_id"]
    )
