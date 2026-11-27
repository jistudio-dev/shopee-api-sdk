"""Zero-dependency Python client for the Shopee Global E-Commerce, Live & Affiliate API (RapidAPI)."""
import json
import os
import urllib.parse
import urllib.request

DEFAULT_HOST = "shopee-e-commerce-live-affiliate-intelligence.p.rapidapi.com"


class ShopeeClient:
    def __init__(self, rapidapi_key: str | None = None, host: str = DEFAULT_HOST, timeout: int = 20):
        self.api_key = rapidapi_key or os.environ.get("RAPIDAPI_KEY", "")
        if not self.api_key:
            raise ValueError("Provide rapidapi_key or set RAPIDAPI_KEY environment variable.")
        self.host = host
        self.timeout = timeout

    def _request(self, method: str, path: str, params: dict | None = None, body: dict | None = None) -> dict:
        qs = ""
        if params:
            clean = {k: v for k, v in params.items() if v is not None and v != ""}
            if clean:
                qs = "?" + urllib.parse.urlencode(clean)
        url = f"https://{self.host}{path}{qs}"
        headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": self.host,
            "Accept": "application/json",
            "User-Agent": "jistudio-shopee-sdk-py/1.0",
        }
        data = None
        if body is not None:
            headers["Content-Type"] = "application/json"
            data = json.dumps(body).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers=headers, method=method)
        with urllib.request.urlopen(req, timeout=self.timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))

    def health(self, country: str = "vn") -> dict:
        return self._request("GET", "/v1/rapidapi/health", {"country": country})

    def get_product_detail(self, url: str = "", shop_id: str = "", item_id: str = "", country: str = "vn", affiliate_id: str = "") -> dict:
        return self._request("GET", "/v1/rapidapi/product/detail", {"url": url, "shop_id": shop_id, "item_id": item_id, "country": country, "affiliate_id": affiliate_id})

    def batch_products(self, urls: list[str], country: str = "vn", affiliate_id: str = "") -> dict:
        return self._request("POST", "/v1/rapidapi/product/batch", body={"urls": urls, "country": country, "affiliate_id": affiliate_id})

    def get_categories(self, url: str = "", shop_id: str = "", item_id: str = "", country: str = "vn") -> dict:
        return self._request("GET", "/v1/rapidapi/product/categories", {"url": url, "shop_id": shop_id, "item_id": item_id, "country": country})

    def get_daily_discover(self, country: str = "vn", limit: int = 15, offset: int = 0) -> dict:
        return self._request("GET", "/v1/rapidapi/trends/daily-discover", {"country": country, "limit": limit, "offset": offset})

    def get_hot_picks(self, country: str = "vn", preset_key: str = "beauty_hair", limit: int = 10) -> dict:
        return self._request("GET", "/v1/rapidapi/trends/hot-picks", {"country": country, "preset_key": preset_key, "limit": limit})

    def search_keywords(self, keyword: str, country: str = "vn") -> dict:
        return self._request("GET", "/v1/rapidapi/trends/search-keywords", {"keyword": keyword, "country": country})

    def get_shop_profile(self, shop_id: str, country: str = "vn") -> dict:
        return self._request("GET", "/v1/rapidapi/shop/profile", {"shop_id": shop_id, "country": country})

    def discover_live_rooms(self, country: str = "vn", limit: int = 10, offset: int = 0) -> dict:
        return self._request("GET", "/v1/rapidapi/live/discover", {"country": country, "limit": limit, "offset": offset})

    def get_live_bag_items(self, session_id: str | int, country: str = "vn", offset: int = 0) -> dict:
        return self._request("GET", "/v1/rapidapi/live/bag-items", {"session_id": str(session_id), "country": country, "offset": offset})

    def get_live_stream_info(self, session_id: str | int, country: str = "vn") -> dict:
        return self._request("GET", "/v1/rapidapi/live/stream-info", {"session_id": str(session_id), "country": country})

    def analyze_affiliate(self, urls: list[str], affiliate_id: str, country: str = "vn", sub_ids: list[str] | None = None) -> dict:
        return self._request("POST", "/v1/rapidapi/affiliate/analyze", body={"urls": urls, "affiliate_id": affiliate_id, "country": country, "sub_ids": sub_ids or []})
