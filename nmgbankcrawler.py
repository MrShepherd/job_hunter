from urllib import parse

import md5
from crawler import Crawler


class NmgbankCrawler(Crawler):
    def craw(self):
        data = []
        li_node = self.soup.find('div', class_='m5list').find_all('li')
        for li in li_node:
            # print(li)
            tmp_dict = {}
            tmp_dict['job_company'] = '内蒙古银行'
            tmp_dict['job_location'] = '内蒙古'
            tmp_dict['job_department'] = 'none'
            tmp_dict['job'] = li.find('a').get_text()
            tmp_dict['job_link'] = parse.urljoin(self.base_url, li.find('a').get('href'))
            tmp_dict['date'] = li.find('span', class_='fr').get_text()
            tmp_dict['md5'] = md5.Md5(tmp_dict['job_link']).md5()
            # print(tmp_dict)
            data.append(tmp_dict)
        return data
