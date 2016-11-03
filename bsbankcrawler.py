from urllib import parse

import md5
from crawler import Crawler


class BsbankCrawler(Crawler):
    def craw(self):
        data = []
        tr_node = self.soup.find('table', class_='listtable').find_all('tr')
        for tr in tr_node:
            # print(tr)
            if tr.find_all('td') is not None and len(tr.find_all('td')) > 0:
                # print('hello')
                td = tr.find_all('td')
                # print(td)
                tmp_dict = {}
                tmp_dict['job_company'] = '包商银行'
                tmp_dict['job'] = td[0].find('a').get_text().strip()
                tmp_dict['job_link'] = parse.urljoin(self.base_url, td[0].find('a').get('href')).strip()
                tmp_dict['job_department'] = td[1].get_text().strip()
                tmp_dict['job_num'] = td[2].get_text().strip()
                tmp_dict['job_location'] = td[3].get('title').strip()
                tmp_dict['date'] = td[4].get_text().strip()
                tmp_dict['md5'] = md5.Md5(tmp_dict['job_link']).md5()
                data.append(tmp_dict)
        return data
