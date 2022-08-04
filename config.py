
import os

ENV = "DEV"
#ENV = "PROD"


## server
host = "0.0.0.0"
port = int(os.environ.get("PORT", 8081))


## info
app_name = "Food Delivery"
contacts = "https://linktr.ee/maurodp"
code = "https://github.com/mdipietro09/App_FoodDelivery"
tutorial = "..."
fontawesome = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"

about = "..."

## fs
#root = os.path.dirname(os.path.dirname(__file__)) + "/"