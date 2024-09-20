from vk_url_scraper import VkScraper

vks = VkScraper("username", "password")



res = vks.scrape("https://vk.com/video-37307799_456245164")
print(res[0]["text"])