from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Define the Pydantic model
class Item(BaseModel):
    id: int
    name: str
    description: str = ""
    price: float
    in_stock: bool = True

# Simulated database (dictionary)
items_db = {}

# CREATE
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    if item.id in items_db:
        raise HTTPException(status_code=400, detail="Item already exists")
    items_db[item.id] = item
    return item

# READ ALL
@app.get("/items/", response_model=List[Item])
def get_items():
    return list(items_db.values())

# READ ONE
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

# UPDATE
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = updated_item
    return updated_item

# DELETE
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return {"message": "Item deleted successfully"}
