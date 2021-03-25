import uuid
from typing import Dict, List
from models.item import Item
from common.database import Database


class Alert:
    def __init__(self, item_id: str, price_limit: float, _id: str = None):
        self.item_id = _id
        self.item = Item.get_by_id(item_id)
        self.price_limit = price_limit
        self.collection = "alerts"
        self._id = _id or uuid.uuid4().hex

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "price_limit": self.price_limit,
            "item_id": self.item_id
        }

    def save_to_mongo(self):
        Database.insert(self.collection, self.json())

    def load_item_price(self) -> float:
        self.item.load_price()
        return self.item.price

    def notify_if_price_reached(self):
        if self.item.price < self.price_limit:
            print(f"Item{self.item} has reached a price under {self.price_limit}. Latest price: {self.item.price}. ")

    @classmethod
    def all(cls) -> List:
        alert_from_db = Database.find("alerts", {})
        return [cls(**alert) for alert in alert_from_db]
