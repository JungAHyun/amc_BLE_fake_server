from fastapi import APIRouter
from fastapi import Body
import random
from typing import Dict

location_router = APIRouter(
    prefix="/api",
    responses={404: {"description": "4444 not found"}},
)

watch_1 = {
    "androidId": "111",
    "x": random.uniform(0, 100),
    "y": random.uniform(0, 100),
}
watch_2 = {
    "androidId": "222",
    "x": random.uniform(0, 100),
    "y": random.uniform(0, 100),
}
androidIdList = ["000"]
watchList = [watch_1, watch_2]

# from pydantic import BaseModel
# from typing import Optional

# class Roctaion(BaseModel):
#     androidId: str
#     x: str
#     y: str


@location_router.post("/register")
async def register_watch(params: Dict[str, str] = Body(...)):
    androidId = params["androidId"]
    watch = {
        "androidId": androidId,
        "x": random.uniform(0, 100),
        "y": random.uniform(0, 100),
    }

    if androidId not in androidIdList:
        androidIdList.append(androidId)
        watchList.append(watch)


global direction
direction = True


@location_router.get("/location")
async def send_location(params: Dict[str, str] = Body(...)):
    androidId = params["androidId"]
    global direction
    location = {}
    for watch in watchList:
        if watch["androidId"] == androidId:
            print(watch["androidId"], " : ", watch["x"], "  |  ", watch["y"])

            watch["x"] = 30 + random.uniform(1, 2)
            watch["y"] = 50 + random.uniform(1, 2)

            if watch["androidId"] == "635bc47c74db8b12":
                watch["x"] = 70 + random.uniform(1, 2)
                watch["y"] = 70 + random.uniform(1, 2)

            # if watch["x"] >= 72:
            #     direction = not direction
            #     watch["x"] = watch["x"] - 5
            # elif watch["x"] < 5:
            #     direction = not direction
            #     watch["x"] = watch["x"] + 5
            # else:
            #     if direction:
            #         watch["x"] = watch["x"] + random.uniform(4, 8)
            #     else:
            #         watch["x"] = watch["x"] - random.uniform(4, 8)

            # if 0 < watch["y"] < 34:
            #     if watch["x"] >= 72:
            #         direction = not direction
            #         watch["y"] = watch["y"] + 10
            #         watch["x"] = watch["x"] - 2
            #     elif watch["x"] < 5:
            #         direction = not direction
            #         watch["y"] = watch["y"] + 10
            #         watch["x"] = watch["x"] + 2
            #     else:
            #         if direction:
            #             watch["x"] = watch["x"] + random.uniform(4, 8)
            #         else:
            #             watch["x"] = watch["x"] - random.uniform(4, 8)

            # elif 34 <= watch["y"] < 90:
            #     if watch["x"] >= 90:
            #         direction = not direction
            #         watch["y"] = watch["y"] + 10
            #         watch["x"] = watch["x"] - 2
            #     elif watch["x"] < 5:
            #         direction = not direction
            #         watch["y"] = watch["y"] + 10
            #         watch["x"] = watch["x"] + 2
            #     else:
            #         if direction:
            #             watch["x"] = watch["x"] + random.uniform(4, 8)
            #         else:
            #             watch["x"] = watch["x"] - random.uniform(4, 8)

            # else:
            #     watch["x"] = random.uniform(8, 25)
            #     watch["y"] = random.uniform(4, 20)

            location = {"x": watch["x"], "y": watch["y"]}

    return location
