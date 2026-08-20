from fastapi import FastAPI, Form

app = FastAPI()

from meter_convert import Convert
from weight_convert import Weight_Convert
from temperature import Temperature_Convert


conversion = {
    "length_convert": Convert,
    "weight_convert": Weight_Convert,
    "temperature_convert": Temperature_Convert
}

@app.post("/{convert_to}")
async def root(
    convert_to: str,
    value: float = Form(...),
    to: str = Form(...),
    froms: str = Form(...)
):
    result = conversion[convert_to](value, froms, to)
    print(result)
    return {"result": result}