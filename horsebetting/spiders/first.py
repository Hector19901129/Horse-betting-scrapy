# -*- coding: utf-8 -*-
import scrapy
import requests
import pandas

class FirstSpider(scrapy.Spider):
    name = 'first'
    start_urls = [
        "https://www.racingandsports.com.au/en/form-guide/index.asp"
        #'https://www.racingandsports.com.au/en/form-guide/index.asp?mdate=8/10/2018&mdiscipline=T&type=Runner+List'
    ]

    def parse(self, response):
        inp = response.xpath("//input[@type='hidden']/@value").extract()
        mdate = inp[1]
        mdiscipline = inp[2]
        gourl = response.url + '?mdate=' + mdate + '&mdiscipline=' + mdiscipline + '&type=Runner+List'
        yield scrapy.Request(url=gourl, callback=self.action2)

    def action2(self, response):
        print '****************************************************************************'
        tr = response.xpath("//div[@id='div_Discipline_T']/table/tr").extract()
        xlsx = pandas.ExcelFile("C:/test/Current.xlsx")
        bb = xlsx.parse(0)
        print bb.icol(0).real[0]
        