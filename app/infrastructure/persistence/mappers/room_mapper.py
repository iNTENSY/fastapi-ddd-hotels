from app.application.contracts.rooms.create_room_request import CreateRoomRequest
from app.domain.rooms.entity import Rooms, RoomId, RoomHotelId, RoomName, RoomDescription, RoomPrice, RoomServices, \
    RoomQuantity, RoomImageId


async def room_from_dict_to_entity(data: dict) -> Rooms:
    return Rooms(
        id=RoomId(data["id"]),
        hotel_id=RoomHotelId(data["hotel_id"]),
        name=RoomName(data["name"]),
        description=RoomDescription(data["description"]),
        price=RoomPrice(data["price"]),
        services=RoomServices(data["services"]),
        quantity=RoomQuantity(data["quantity"]),
        image_id=RoomImageId(data["image_id"]),
    )


async def room_from_dataclass_to_dict(data: CreateRoomRequest) -> dict:
    converted_data = {"hotel_id": data.hotel_id}
    converted_data.update(vars(data.content))
    return converted_data
