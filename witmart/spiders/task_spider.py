# -*- coding: utf-8 -*-
"""
@author: Leo
"""


import scrapy


class JobSpider(scrapy.Spider):
    name = "witmart_jobs"
    
    start_urls = ["https://secure.witmart.com/user/sign/in"]
    login_start_url = "http://www.witmart.com/logo-design/jobs?s=3"
    
    def parse(self, response): 
        yield scrapy.FormRequest.from_response(
            response,
            formdata={
                'email': 'sheepql@hotmail.com',             
                'password': '0sheep0',
            },
            callback=self.after_login
        )
        
    def after_login(self, response, start_url=login_start_url):
        yield scrapy.Request(url=start_url, callback=self.parse_control)
        
    def parse_control(self, response):
        urls = response.xpath("//a[@class='fromtitle']/@href").extract()
#        for url in urls:
#            yield response.follow(url, callback=self.parse_job)
        yield response.follow(urls[0], callback=self.parse_job)
            
#        next_page = response.xpath("//*[text()='Next page']/@href").extract()
#        if next_page:
#            next_url = response.urljoin(next_page[0])
#            yield scrapy.Request(next_url, callback=self.parse)
            
    def parse_job(self, response):
        """
        parse job information through response.xpath("...").extract()
        """
        
        urls = response.xpath("//a[@class='bf16']/@href").extract()
        for url in urls:
            yield response.follow(url, callback=self.parse_user)

        next_page = response.xpath("//i/a/@href").extract()
        if next_page:
            next_url = response.urljoin(next_page[0])
            yield scrapy.Request(next_url, callback=self.parse_job)

    def parse_user(self, response):
        """
        parse user information
        """
        print( response.xpath("//h1[@class='usedr-name']/text()").extract() )