from datetime import datetime

import bsbankcrawler
import nmgbankcrawler
import ordoscyycrawler
import yilicrawler


class CrawlerMain(object):
    def __init__(self):
        self.yili_crawler = yilicrawler.YiliCrawler('http://zhaopin.yili.com/social/posList.do?province=150000', 'http://zhaopin.yili.com/')
        self.nmgbank_crawler = nmgbankcrawler.NmgbankCrawler('http://www.boimc.com.cn/aboutus/zhaopin/notice/', 'http://www.boimc.com.cn')
        self.bsbank_crawler = bsbankcrawler.BsbankCrawler('http://zhaopin.zhiye.com/social?r=&p=&c=1500&d=&k=#jlt', 'http://zhaopin.zhiye.com')
        self.ordoscyy_crawler_1 = ordoscyycrawler.OrdoscyyCrawler('http://www.ordosgxq.gov.cn/rsrc/dtxx/', 'http://www.ordosgxq.gov.cn/rsrc/dtxx/')
        self.ordoscyy_crawler_2 = ordoscyycrawler.OrdoscyyCrawler('http://www.ordosgxq.gov.cn/zwgk/tzgg/', 'http://www.ordosgxq.gov.cn/zwgk/tzgg/')

    def craw(self):
        yili_data = self.yili_crawler.craw()
        # print(yili_data)
        nmgbank_data = self.nmgbank_crawler.craw()
        # print(nmgbank_data)
        bsbank_data = self.bsbank_crawler.craw()
        # print(bsbank_data)
        ordoscyy_data_1 = self.ordoscyy_crawler_1.craw()
        # print(ordoscyy_data_1)
        ordoscyy_data_2 = self.ordoscyy_crawler_2.craw()
        # print(ordoscyy_data_2)
        data = yili_data + nmgbank_data + bsbank_data + ordoscyy_data_1 + ordoscyy_data_2
        for item in data:
            item['etl_date'] = datetime.now().strftime("%Y-%m-%d")
        return data
