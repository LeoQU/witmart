# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 20:20:50 2017

@author: Leo
"""


import scrapy


class JobSpider(scrapy.Spider):
    name = "witmart_jobs"
    
    initial_url = "http://www.witmart.com"
    job_category = "logo-design"
    job_param = "jobs?s=3"
    
    start_urls = [initial_url + "/" + job_category + "/" + job_param]
    print(start_urls)
    
    def parse(self, response):
        urls = response.xpath("//a[@class='fromtitle']/@href").extract()
        print(urls)
        
#        next_page = response.xpath("//*[text()='Next page']/@href").extract()[0]
#        if next_page is not None:
#            next_url = response.urljoin(next_page)
#            yield scrapy.Request(next_url, callback=self.parse)