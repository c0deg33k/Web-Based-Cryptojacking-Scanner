# Web-Based-Cryptojacking-Scanner

This is a simple project to crawl and scan websites for known cryptojacking scripts embedded in their source code.
It works simply by catching the keywords mostly used by browser mining vendors.

## Activating the environment

`crypto` is the environment name in use here. To activate(windows) use the following;

```
crypto\Scripts\activate
```

Afterwards proceed as follows;

## Project requirements

This project uses sites from majestic(find the csv in the site-lists folder) and the scrapy framework.
You can install scrapy as follows.

```
pip install scrapy
```

Or

```
pip install -r requirements.txt
```

## Usage

Below is an example of how to run the project.

```
cd scanner
```

```
scrapy crawl majestic
```

To save the output of flagged sites for use with extensions e.g. Ublock origin, pipe the output to a csv file as below.

```
scrapy crawl majestic > <filename>.csv
```
