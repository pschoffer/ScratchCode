const { Builder, By, Key, until } = require('selenium-webdriver');

const startURL =
  'https://speedcoding.toptal.com/challenge?ch=toptal-speedcoding';

(async function example() {
  console.log('Gonna start!');
  let driver = await new Builder().forBrowser('firefox').build();
  try {
    await driver.get(startURL);
    title = await driver.getTitle();
    console.log('Filling form ' + title);
  } finally {
    await driver.quit();
  }
})();
