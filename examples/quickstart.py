import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "python"))
from shopee_api_sdk import ShopeeClient

client = ShopeeClient()
detail = client.get_product_detail(url="https://shopee.vn/product/37251933/41412722725")
p = detail["product"]
print(f"{p['name']} | Price: {p['price']} {detail['currency']} | Exact Sold: {p['historical_sold']} | Monthly: {p['monthly_sold']}")
