# SoloLevellingScrapper

A simple tool to scrap all images from a website and store links to them in json format

## Purpose of it

This python code is designed to scrap image links from a website that is hosting Solo-Levelling Webtoon.
It will go to main page and first scrape all chapter links and store them in dictionary.

Later, it will go into individual chapter and using XPATH `"//div[@class='entry-content']/div[@class='separator']/a/img"`, identify all chapter images.
Once it has gone through whole chapter page, it will put it into same dictionary under a format of:

```json
{
  "2": {
    "url": "link_to_chapter_2",
    "images": {
      "0": "link_to_image_1",
      "1": "link_to_image_2",
      "2": "link_to_image_3",
      "3": "link_to_image_4",
      "4": "link_to_image_5",
      "5": "link_to_image_6",
      "6": "link_to_image_7",
      "7": "link_to_image_8",
      "8": "link_to_image_9",
      "9": "link_to_image_10",
      "10": "link_to_image_11"
    }
  }
}
```

## How to run it

```bash
py sololevelling.py
```
