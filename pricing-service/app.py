from models.alert import Alert

alert = Alert("e81341d983ef47979282e13d236f73b4", 1000)
alert.save_to_mongo()
