import * as fs from 'fs';
import * as puppeteer from 'puppeteer';

async function main() {
  const browser = await puppeteer.launch({
    headless: true
  });

  const page = await browser.newPage();

  await page.goto('http://www.alternativejs.com/');

  // const closeModal = (await page.$x('//*[@id="PopupSignupForm_0"]/div[2]/div[1]'))[0];
  // await closeModal.click();

  let myElements = await page.$x('//*[@id="mainNav"]/div/a');
  let titleProp = await myElements[0].getProperty('innerText');
  let title = await titleProp.jsonValue();
  console.log({title})

  await page.screenshot({ path: './myPage.png' });

  if (typeof(title) === 'string') {
    fs.writeFileSync('./myData.txt', title);
  }

  await browser.close();
}

main();