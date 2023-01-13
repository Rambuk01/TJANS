import asyncio
import os
from pyppeteer import launch
from u import *
cookies = 0;
async def main():
    global cookies
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://nordborgslot.viggo.dk')
    await page.type('#UserName', user)
    await page.type('#Password', pw)
    await page.evaluate("document.querySelector('.unknown-user').submit()")
    await page.screenshot({'path': 'example.png'})
    await page.waitForNavigation()
    cookies = await page.cookies()

    #print("Cookies: {}".format(cookies))
    cookies = cookies[1]['value']
    print("Cookie value: {}".format(cookies))
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())