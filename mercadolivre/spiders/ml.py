#terminal: pip install scapy
#terminal:
#para rodar: terminal: scrapy runspider ml.py
#gerar json: scrapy crawl ml -o ml.json


import scrapy

class MlSpider(scrapy.Spider):
    name = 'ml'
    start_urls = [f'https://www.mercadolivre.com.br/ofertas?page{i}' for i in range(1,210)]

    def parse(self, response,**kwards):
        for i in response.xpath('//li[@class="promotion-item"]'):
            price = i.xpath('.//span[@class="promotion-item__price"]//text() ').getall()
            title = i.xpath('.//p[@class="promotion-item__title"]//text()').get()
            link = i.xpath('./a/@href').get()

            yield{
                'price' : price,
                'title' : title,
                'link': link
            }

'''verificar se existe proxima pagina
    //a[contains(@title,"Próxima")]/href
    href pega o link

        next_page = response.xpath('//a[contains(@title,"Próxima")]/href').get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)