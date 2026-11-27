import { ShopeeClient } from "../node/index.mjs";

const client = new ShopeeClient();
const detail = await client.getProductDetail({ url: "https://shopee.vn/product/37251933/41412722725" });
console.log(detail.product.name, "| Exact Sold:", detail.product.historical_sold, "| Price:", detail.product.price);
