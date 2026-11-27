/** Zero-dependency Node.js 18+ ESM SDK for Shopee Global API (8 countries) on RapidAPI. */
const DEFAULT_HOST = "shopee-e-commerce-live-affiliate-intelligence.p.rapidapi.com";

export class ShopeeClient {
  constructor(rapidapiKey = process.env.RAPIDAPI_KEY || "", host = DEFAULT_HOST) {
    if (!rapidapiKey) throw new Error("Provide rapidapiKey or set RAPIDAPI_KEY.");
    this.apiKey = rapidapiKey;
    this.host = host;
  }

  async _request(method, path, params = null, body = null) {
    const url = new URL(`https://${this.host}${path}`);
    if (params) {
      for (const [k, v] of Object.entries(params)) {
        if (v !== undefined && v !== null && v !== "") url.searchParams.set(k, String(v));
      }
    }
    const headers = {
      "X-RapidAPI-Key": this.apiKey,
      "X-RapidAPI-Host": this.host,
      Accept: "application/json",
    };
    const init = { method, headers };
    if (body !== null) {
      headers["Content-Type"] = "application/json";
      init.body = JSON.stringify(body);
    }
    const res = await fetch(url, init);
    if (!res.ok) throw new Error(`HTTP ${res.status}: ${await res.text()}`);
    return res.json();
  }

  health(country = "vn") { return this._request("GET", "/v1/rapidapi/health", { country }); }
  getProductDetail({ url, shop_id, item_id, country = "vn", affiliate_id } = {}) {
    return this._request("GET", "/v1/rapidapi/product/detail", { url, shop_id, item_id, country, affiliate_id });
  }
  batchProducts({ urls, country = "vn", affiliate_id } = {}) {
    return this._request("POST", "/v1/rapidapi/product/batch", null, { urls, country, affiliate_id });
  }
  getCategories({ url, shop_id, item_id, country = "vn" } = {}) {
    return this._request("GET", "/v1/rapidapi/product/categories", { url, shop_id, item_id, country });
  }
  getDailyDiscover({ country = "vn", limit = 15, offset = 0 } = {}) {
    return this._request("GET", "/v1/rapidapi/trends/daily-discover", { country, limit, offset });
  }
  getHotPicks({ country = "vn", preset_key = "beauty_hair", limit = 10 } = {}) {
    return this._request("GET", "/v1/rapidapi/trends/hot-picks", { country, preset_key, limit });
  }
  searchKeywords({ keyword, country = "vn" }) {
    return this._request("GET", "/v1/rapidapi/trends/search-keywords", { keyword, country });
  }
  getShopProfile({ shop_id, country = "vn" }) {
    return this._request("GET", "/v1/rapidapi/shop/profile", { shop_id, country });
  }
  discoverLiveRooms({ country = "vn", limit = 10, offset = 0 } = {}) {
    return this._request("GET", "/v1/rapidapi/live/discover", { country, limit, offset });
  }
  getLiveBagItems({ session_id, country = "vn", offset = 0 }) {
    return this._request("GET", "/v1/rapidapi/live/bag-items", { session_id, country, offset });
  }
  analyzeAffiliate({ urls, affiliate_id, country = "vn", sub_ids = [] }) {
    return this._request("POST", "/v1/rapidapi/affiliate/analyze", null, { urls, affiliate_id, country, sub_ids });
  }
}
