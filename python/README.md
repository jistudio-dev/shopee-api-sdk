# Shopee API SDK — 8 Markets, Exact Unrounded Sold Count, Live Bags & Affiliate (Python / Node.js / n8n)

[![Shopee Global API — 13 Live Endpoints across 8 Markets](https://api.apify.com/v2/key-value-stores/0J5jsCbmj4kPfyj6H/records/rapid-shopee-hero-v1.png)](https://rapidapi.com/Techssss/api/shopee-e-commerce-live-affiliate-intelligence/playground)

Zero-dependency **Python** and **Node.js (ESM)** SDK + ready-to-import **n8n price tracker workflow** for the **Shopee Global E-Commerce, Live & Affiliate API** across all 8 Shopee markets (`VN, ID, TH, PH, MY, SG, TW, BR`).

- **Exact unrounded sales**: Receive `historical_sold: 1096754` and `monthly_sold: 27202` instead of `"10k+ sold"`.
- **All 8 countries**: `vn`, `id`, `th`, `ph`, `my`, `sg`, `tw`, `br` (auto-detected when passing a product URL or shortlink).
- **13 endpoints**: Product detail, 20x batch fetch, category tree, Daily Discover, Hot Picks, buyer search autocomplete, Shop profile, Shopee Live rooms/bags/HLS streams, and 8-format affiliate link & commission calculator.
- **Zero cookies, zero browser setup, zero pip/npm dependency bloat.**

<p>
<a href="https://rapidapi.com/Techssss/api/shopee-e-commerce-live-affiliate-intelligence/playground"><img src="https://api.apify.com/v2/key-value-stores/0J5jsCbmj4kPfyj6H/records/rapid-shopee-cta-v1.png" width="268" height="48" alt="Test Shopee Global API on RapidAPI →"></a>
</p>

> Need bulk scheduled dataset exports (CSV / Excel / Google Sheets)? Also available on [Apify Store (`jistudio/shopee-scraper`)](https://apify.com/jistudio/shopee-scraper).

---

## How It Works

<p align="center">
  <img src="https://api.apify.com/v2/key-value-stores/0J5jsCbmj4kPfyj6H/records/rapid-shopee-step1-v1.png" width="820" alt="Step 1: Pass any Shopee URL or IDs"/><br/>
  <img src="https://api.apify.com/v2/key-value-stores/0J5jsCbmj4kPfyj6H/records/step-arrow-down.svg" width="40" alt=""/><br/>
  <img src="https://api.apify.com/v2/key-value-stores/0J5jsCbmj4kPfyj6H/records/rapid-shopee-step2-v1.png" width="820" alt="Step 2: Receive structured JSON with exact unrounded sold count"/>
</p>

---

## Quickstart

### 1. Python (Zero Dependencies — Standard Library Only)

```bash
export RAPIDAPI_KEY="YOUR_RAPIDAPI_KEY"
python examples/quickstart.py
```

```python
from python.shopee_api_sdk import ShopeeClient

client = ShopeeClient(rapidapi_key="YOUR_RAPIDAPI_KEY")

# 1. Exact product detail (auto-detects country, shop_id, item_id)
detail = client.get_product_detail(url="https://shopee.vn/product/37251933/41412722725")
p = detail["product"]
print(p["name"], "| Price:", p["price"], "| Exact Sold:", p["historical_sold"])

# 2. Indonesia Daily Discover trending products
id_trends = client.get_daily_discover(country="id", limit=5)
print("Top ID item:", id_trends["items"][0]["name"])

# 3. Affiliate commission & 8 tracking link formats
aff = client.analyze_affiliate(
    urls=["https://shopee.vn/product/37251933/41412722725"],
    affiliate_id="17321010010",
    country="vn",
)
print("Commission:", aff["items"][0]["affiliate_commission"])
```

### 2. Node.js 18+ (Zero Dependencies — Native `fetch`)

```bash
export RAPIDAPI_KEY="YOUR_RAPIDAPI_KEY"
node examples/quickstart.mjs
```

```javascript
import { ShopeeClient } from "./node/index.mjs";

const client = new ShopeeClient(process.env.RAPIDAPI_KEY);
const res = await client.getProductDetail({ url: "https://shopee.vn/product/37251933/41412722725" });
console.log(res.product.name, "Exact Sold:", res.product.historical_sold);
```

### 3. n8n Automated Price & Sales Tracker

Import [`workflows/n8n-shopee-price-tracker.json`](./workflows/n8n-shopee-price-tracker.json) into n8n, set your `RAPIDAPI_KEY` header on the HTTP Request node, and schedule hourly price & sold-velocity tracking.

---

## Supported 8 Marketplaces

| Code | Country | Domain | Currency |
| :-: | :--- | :--- | :-: |
| `vn` | Vietnam | `shopee.vn` | `VND` |
| `id` | Indonesia | `shopee.co.id` | `IDR` |
| `th` | Thailand | `shopee.co.th` | `THB` |
| `ph` | Philippines | `shopee.ph` | `PHP` |
| `my` | Malaysia | `shopee.com.my` | `MYR` |
| `sg` | Singapore | `shopee.sg` | `SGD` |
| `tw` | Taiwan | `shopee.tw` | `TWD` |
| `br` | Brazil | `shopee.com.br` | `BRL` |

---

## JiStudio Ecosystem

- **RapidAPI**: [Shopee Global API](https://rapidapi.com/Techssss/api/shopee-e-commerce-live-affiliate-intelligence) · [TikTok & Shop API](https://rapidapi.com/Techssss/api/tiktok-data-tiktok-shop-no-watermark-video) · [Twitter (X) & Crypto API](https://rapidapi.com/Techssss/api/twitter-x-real-time-data-crypto-x-intel)
- **GitHub Org**: [github.com/jistudio-dev](https://github.com/jistudio-dev) · **Apify Store**: [apify.com/jistudio](https://apify.com/jistudio)
- **License**: MIT — Independent public market research & affiliate SDK; not affiliated with Shopee or Sea Limited.
