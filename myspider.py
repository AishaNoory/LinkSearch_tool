import scrapy
import csv

class MySpider(scrapy.Spider):
    name = "myspider"
    start_urls = ["https://unfccc.int/NDCREG?field_party_region_target_id=All&field_document_ca_target_id=All&field_vd_status_target_id=5933&start_date_datepicker=&end_date_datepicker=&page=12"]

    def parse(self, response):
        # Find all anchor tags with href attribute containing 'pdf' (you can adjust the filter as needed)
        links = response.css('a[href*=pdf]::attr(href)').extract()

        # Remove duplicate links, if any
        unique_links = list(set(links))

        # Save the links to a CSV file
        with open("document_links.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for link in unique_links:
                writer.writerow([link])

        self.log(f"Scraped {len(unique_links)} document links and saved them to document_links.csv")
