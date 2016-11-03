from urllib import parse

import md5
from crawler import Crawler


class YiliCrawler(Crawler):
    def craw(self):
        data = []
        tr_node = self.soup.find('div', class_='lst').find_all('tr')
        # print(tr_node)
        for tr in tr_node:
            # print(tr)
            tmp_dict = {}
            td = tr.find_all('td')
            # print(td)
            tmp_dict['job_company'] = '伊利'
            if td[0].get('title') is not None:
                tmp_dict['job'] = td[0].get('title')
                link = td[0].find('a').get('href')
                tmp_dict['job_link'] = parse.urljoin(self.base_url, link)
                tmp_dict['job_department'] = td[1].get('title')
                tmp_dict['job_category'] = td[2].get_text()
                tmp_dict['number'] = td[3].get_text()
                tmp_dict['job_location'] = td[4].get('title')
                tmp_dict['date'] = td[5].get_text()
                tmp_dict['md5'] = md5.Md5(tmp_dict['job'] + tmp_dict['job_department'] + tmp_dict['date']).md5()
                # print(tmp_dict)
                data.append(tmp_dict)
        return data
