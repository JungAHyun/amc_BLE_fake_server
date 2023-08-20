from fastapi import APIRouter
from fastapi import Body
import random
from typing import Dict
import pandas as pd

location_router = APIRouter(
    prefix="/api",
    responses={404: {"description": "4444 not found"}},
)


androidIdList = []
watchList = []
scannerLocation = []


def getScannerLocation():
    # 읽어올 엑셀 파일 지정
    filename = "아산병원_BLEScanner.xlsx"

    # 엑셀 파일 읽어 오기
    df = pd.read_excel(filename, engine="openpyxl", header=0)
    for i in range(40):
        x = df.iloc[i, 2]
        y = df.iloc[i, 3]
        scannerLocation.append({"x": x, "y": y})

    return scannerLocation


@location_router.post("/register")
async def register_watch(params: Dict[str, str] = Body(...)):
    scannerLocation = getScannerLocation()

    androidId = params["androidId"]
    index = random.randint(0, 20)
    watch = {
        "androidId": androidId,
        "scannerIndex": index,
        "x": scannerLocation[index]["x"],
        "y": scannerLocation[index]["y"],
    }

    if androidId not in androidIdList:
        androidIdList.append(androidId)
        watchList.append(watch)


global direction
direction = True


@location_router.get("/location")
async def send_location(params: Dict[str, str] = Body(...)):
    scannerLocation = getScannerLocation()
    androidId = params["androidId"]
    global direction
    location = {}
    for watch in watchList:
        if watch["androidId"] == androidId:
            print(
                watch["androidId"],
                " : ",
                watch["scannerIndex"],
                "  |  ",
                watch["x"],
                "  |  ",
                watch["y"],
            )

            # if watch["androidId"] == "635bc47c74db8b12":
            if watch["scannerIndex"] == 39:
                watch["scannerIndex"] = 0
            else:
                watch["scannerIndex"] = watch["scannerIndex"] + 1

            watch["x"] = scannerLocation[watch["scannerIndex"]]["x"]
            watch["y"] = scannerLocation[watch["scannerIndex"]]["y"]

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
