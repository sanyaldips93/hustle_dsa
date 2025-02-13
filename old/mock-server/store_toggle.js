const axios = require('axios');

const delayBetweenRequests = 100;
const virtualStoreCodes = ['VST178949082'];
// const virtualStoreCodes = ['VST316284167'];
const channelNames = ['swiggy'];
const status = true; // false for Deactivate

const runStoreToggleScript = async () => {
    let url = `https://moss-staging7.rebelfoods.com/${virtualStoreCodes[0]}/store-toggle`;
    // let url = `http://localhost:3035/${virtualStoreCodes[0]}/store-toggle`;
    for (let i = 0; i < 115; i++) {
      try {
        const res = axios.post(url, {
          "channel": channelNames,
          "status": status
        }, {
          headers: { "api-key": "ma0c34fe2e7111edb242060cb931d70f" },
          timeout: 5000
        });
  
        // await new Promise(resolve => setTimeout(resolve, delayBetweenRequests));
        console.log('success');
      } catch (error) {
        // console.log("Error ::", virtualStoreCodes[i]);
        console.log(error?.message);
      }
    }
    console.log("Completed All requests");
}

module.exports = { runStoreToggleScript };