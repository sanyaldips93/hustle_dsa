const axios = require('axios');

// Configuration
const delayBetweenRequests = 100;
const channelName = 'deliveroo';
const itemIds = ["MPR632856722"];
const variantIds = [];
const addonIds = [];
const status = 1; // 0 for deactivate

const createProductToggleRequestBody = () => {
    const items = [];
    const variants = [];
    const addons = [];
    for (let j=0; j< itemIds.length; j++) {
        items.push({
            "item_id": itemIds[j],
            "status": status
        });
    }
    for (let j=0; j< variantIds.length; j++) {
      variants.push({
          "variant_id": variantIds[j],
          "status": status
      });
    }
    for (let j=0; j< addonIds.length; j++) {
      addons.push({
          "addon_id": addonIds[j],
          "status": status
      });
    }
    const body = {
        "data": [
            {
                "channel": channelName,
                "items": items
            }
        ]
    }
    return body;
}

const runProductToggleScript = async () => {
    const body = createProductToggleRequestBody();
    let url = `https://moss-staging6.rebelfoods.com/VST935166226/product-toggle`;
    // let url = `http://localhost:3035/VST935166226/product-toggle`;
    for (let i = 0; i < 20; i++) {
      try {
        const res = axios.post(url, body, {
          headers: { "api-key": "ma0c34fe2e7111edb242060cb931d70f" },
          timeout: 5000
        });
  
        // console.log(i);
        // console.log(res?.data);
  
        // await new Promise(resolve => setTimeout(resolve, delayBetweenRequests));
      } catch (error) {
        // console.log("Error :: ", i);
        console.log(error?.message);
      }
    }
    console.log("Completed All requests");
}

module.exports = { runProductToggleScript };