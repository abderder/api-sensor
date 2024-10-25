from datetime import date

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import logging

from starlette.routing import request_response

from fake_data_app import create_app


store_dict = create_app()


app = FastAPI()

@app.get("/vimderder")

def visit(
        store_name: str, year: int, month: int, day: int, sensor_id: int | None = None
         ) -> JSONResponse:
    if store_name not in store_dict.keys():
        return JSONResponse(status_code=404, content={"message": "Store not found"})
    try:
        request_date = date(year, month, day)
    except ValueError as e:
        logging.error(f"Could not cast date: {e}")
        return JSONResponse(status_code=400, content="Enter a valid date")


    if year < 2019 :
        return JSONResponse(status_code=404, content={"message": "no data before 2019"})
    if request_date > date.today() :
        return JSONResponse(status_code=404, content={"message": "no data"})
    if sensor_id is None:
        visit_count = store_dict[store_name].get_all_traffic(request_date)
    else:
        visit_count = store_dict[store_name].get_sensor_traffic(sensor_id, request_date )
    if visit_count < 0:
        return JSONResponse(status_code=404, content={"message": "store was closed"})
    return JSONResponse(status_code=200, content=visit_count)



