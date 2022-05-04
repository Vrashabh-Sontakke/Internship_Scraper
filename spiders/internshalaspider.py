import scrapy
class InternshalaSpider(scrapy.Spider):
    name = 'internshala'
    start_urls = ['https://internshala.com/internships/keywords-DevOps']

    def parse(self, response):
        for internships in response.css('div.container-fluid.individual_internship'):
            yield {
                'company': internships.css('a.link_display_like_text::text').get().replace('\n                        ','').replace('                    ',''),
                'stipend': internships.css('span.stipend::text').get(),
                'link': internships.css('a.view_detail_button').attrib['href'].replace('/internship','https://internshala.com/internship'),
            }