from urllib import parse

import md5
from crawler import Crawler


class OrdoscyyCrawler(Crawler):
    def craw(self):
        # print('=' * 50)
        data = []
        table_node = self.soup.find_all('table', {'width': '98%', 'cellpadding': '0', 'cellspacing': '0', 'border': '0'})
        #         # print(table_node[3])
        for table in table_node:
            # print(table)
            tmp_dict = {}
            tmp_dict['job_company'] = '鄂尔多斯产业园'
            tmp_dict['job_location'] = '鄂尔多斯市'
            tmp_dict['job_department'] = 'none'
            td = table.find_all('td')
            # print(td)
            if len(td) > 0 and td[1].find('a') is not None:
                tmp_dict['job'] = td[1].find('a').get('title')
                tmp_dict['job_link'] = parse.urljoin(self.base_url, td[1].find('a').get('href'))
                tmp_dict['date'] = td[2].get_text()
                tmp_dict['md5'] = md5.Md5(tmp_dict['job_link']).md5()
                data.append(tmp_dict)
        return data
