const { Builder, By, Key, until } = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');

const startURL =
  'https://speedcoding.toptal.com/challenge?ch=toptal-speedcoding';

chrome.setDefaultService(
  new chrome.ServiceBuilder(
    './node_modules/chromedriver/bin/chromedriver'
  ).build()
);

(async function example() {
  console.log('Gonna start!');
  try {
    let driver = await new Builder().forBrowser('chrome').build();
    await driver.get(startURL);
    title = await driver.getTitle();
    console.log('Filling form ' + title);
  } catch (e) {
    console.log('ERRORR', e);
  } finally {
    await driver.quit();
  }
})();
