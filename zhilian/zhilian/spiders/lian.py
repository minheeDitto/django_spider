# -*- coding: utf-8 -*-
import scrapy
import json


class LianSpider(scrapy.Spider):
    name = 'lian'
    allowed_domains = ['zhaopin.com']
    start_urls = ['https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=638&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&_v=0.61013651&x-zp-page-request-id=3e033c1ae68d4acfbf526c510c7bbd4c-1574437770471-950180&x-zp-client-id=ab3cfcd1-793c-49c2-89c8-499a807d537c&MmEwMD=4ZhHtMUhu.Rm9BTY5arhKcHgdKJgnb1_xmuogA.34L1B40.R2NIul3LgR2sk8WroDYDFFRLfDbcCPE5O2Iw4FyH.WsMfQ0rqZQJIVNOoR8NINMwYOjbA4QMBqr9WKzY3kAoXksZH3bCnpeLwYC6J3g7fex02h1xVvBg.7nR7ex1Wha1wPqVHPEXl5XpHOmJ_pwJVW4h.60ryejLzb5L2GU6xNC931AC4sIiGuuTCSMOcnWOZXOmmOwP.AzonnRIswnAPMIubqCTJg_2q6Sv.9kjEM8cWeojgNHVShfNgqa7TZ5gVnF7z_KZduJ7ui3Z4zdNG9W.YUAJMwGFd199n5WtmlggTDGPuO3NhyZzNN7_0_mX2afXjMl9ffc2ce9PnHMRWk7_HPvmxTRHtyS_j.KjGbOPax4bICIH3cautyKOl3VcaQXsZQt4mWWLfb4NkvNs5']
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}

    def start_requests(self):
        yield scrapy.Request(
            url=self.start_urls[0],
            headers=self.headers
        )

    def parse(self, response):
        datas = json.loads(response.text)["data"]["results"]
        for data in datas:
            data_dict = {}
            data_dict["jobName"] = data["jobName"]
            data_dict["exp"] = data["workingExp"]["name"]
            data_dict["salary"] = data["salary"]
            data_dict["edu"] = data["eduLevel"]
            print(data_dict)

