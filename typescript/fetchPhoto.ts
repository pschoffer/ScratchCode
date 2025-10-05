import axios = require("axios");

const main = async () => {
    const baseUrl = "https://order.exaktaphoto.se/system/xphoto/webshop?uuid=<uid>";

    // Headers (optional but recommended)
    const headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Cookie": 'PHPSESSID=f572n60cgjbkfvhvhjf52hvp1p; _ga=GA1.1.325375108.1759564151; CookieConsent={stamp:%27xtFW9hfJwUUeaB64PUUgxmP4CzXwrcaGiW3PX6VSL/UPiGXyTHnb5w==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1759564151940%2Cregion:%27se%27}; NLLANG=en_GB; _ga_XEBX3PQ9P6=GS2.1.s1759564148$o1$g1$t1759565150$j37$l0$h0'
    };


    const startScaleVersion = 1350;
    const maxScaleVersion = 4000;
    for (let scaleversion = startScaleVersion; scaleversion < maxScaleVersion; scaleversion += 10) {
        const url = `${baseUrl}&scaleversion=${scaleversion}`;
        console.log(`Fetching URL: ${url}`);
        const response = await axios.get(url, { headers });
        console.log(response.data);
        await new Promise(resolve => setTimeout(resolve, 1000));
    }

}

main()