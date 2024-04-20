from app.application.contracts.rooms.create_room_request import CreateRoomRequest
from app.domain.rooms.entity import Rooms


async def room_from_dict_to_entity(data: dict) -> Rooms:
    return await Rooms.create(
        id=data["id"],
        hotel_id=data["hotel_id"],
        name=data["name"],
        description=data["description"],
        price=data["price"],
        services=data["services"],
        quantity=data["quantity"],
        image_id=data["image_id"],
    )


async def room_from_dataclass_to_dict(data: CreateRoomRequest) -> dict:
    converted_data = {"hotel_id": data.hotel_id}
    converted_data.update(vars(data.content))
    return converted_data
