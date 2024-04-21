from app.domain.hotels.entity import Hotels, HotelId, HotelName, HotelLocation, HotelServices, HotelRoomQuantity, \
    HotelImageId


async def hotel_from_dict_to_entity(data: dict) -> Hotels:
    return Hotels(
        id=HotelId(data["id"]),
        name=HotelName(data["name"]),
        location=HotelLocation(data["location"]),
        services=HotelServices(data["services"]),
        rooms_quantity=HotelRoomQuantity(data["rooms_quantity"]),
        image_id=HotelImageId(data["image_id"])
    )
