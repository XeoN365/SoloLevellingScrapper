# SoloLevellingScrapper
A simple tool to scrap all images from a website and store links to them in json format

## Purpose of it
This python code is designed to scrap image links from a website that is hosting Solo-Levelling Webtoon. 
It will go to main page and first scrape all chapter links and store them in dictionary.

Later, it will go into individual chapter and using XPATH ```"//div[@class='entry-content']/div[@class='separator']/a/img"```, identify all chapter images.
Once it has gone through whole chapter page, it will put it into same dictionary under a format of:

```json
{
  "2": {
    "url": "link_to_chapter_2",
    "images": {
      "0": "link_to_image_1",
      "1": "link_to_image_1",
      "2": "link_to_image_1",
      "3": "link_to_image_1",
      "4": "link_to_image_1",
      "5": "link_to_image_1",
      "6": "link_to_image_1",
      "7": "link_to_image_1",
      "8": "link_to_image_1",
      "9": "link_to_image_1",
      "10": "link_to_image_1"
    }
  }
}
```


## How to run it
```bash
py sololevelling.py
```
