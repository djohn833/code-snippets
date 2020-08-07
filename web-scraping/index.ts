const fs = require('fs');
const puppeteer = require('puppeteer');

async function main() {
  const browser = await puppeteer.launch({
    headless: true
  });

  const page = await browser.newPage();

  await page.goto('http://www.alternativejs.com/');

  const closeModal = (await page.$x('//*[@id="PopupSignupForm_0"]/div[2]/div[1]'))[0];
  await closeModal.click();

  let myElement = (await page.$x('//*[@id="mainNav"]/div/a'))[0];
  let titleProp = await myElement.getProperty('innerText');
  let title = await titleProp.jsonValue();
  console.log({title})

  await page.screenshot({ path: './myPage.png' });

  fs.writeFileSync('./myData.txt', title);

  await browser.close();
}

main();