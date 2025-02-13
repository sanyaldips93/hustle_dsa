const axios = require('axios');

// Configuration
const delayBetweenRequests = 100;
const virtualStoreCodes = [
  'VST935166226'
];
const channelName = 'deliveroo';
const channelCode = 'CHN487690740';


const runMenuPushScript = async () => {
    let url = `https://moss-staging7.rebelfoods.com/${virtualStoreCodes[0]}/menu-trigger/${channelName}`;
    // let url = `http://localhost:3035/${virtualStoreCodes[0]}/menu-trigger/${channelName}`;
    for (let i = 0; i < 4; i++) {
      try {
        const res = await axios.post(url, {
          "channel_code": `${channelCode}`
        }, {
          headers: { "api-key": "ma0c34fe2e7111edb242060cb931d70f" },
          timeout: 5000
        });
  
        // console.log(i, virtualStoreCodes[i]);
        // console.log(res?.data);
        console.log('SUCCESS');
  
        await new Promise(resolve => setTimeout(resolve, delayBetweenRequests));
      } catch (error) {
        // console.log("Error ::", virtualStoreCodes[i]);
        console.log(error?.message);
      }
    }
    console.log("Completed All requests");
}

module.exports = {runMenuPushScript};