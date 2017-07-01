#-*_coding:utf8-*-

import scrapy
from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from shenZhouCars.items import shenZhouCarsItem

class fieldsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    car_brand = scrapy.Field()
    car_series = scrapy.Field()
    car_fuel_type = scrapy.Field()
    car_issue_date = scrapy.Field()
    car_config_model = scrapy.Field()
    car_seats_num = scrapy.Field()
    car_doors = scrapy.Field()
    car_gearbox_type = scrapy.Field()
    car_displacement = scrapy.Field()
    car_fuel_num = scrapy.Field()
    car_drive_way = scrapy.Field()
    car_engine_intake = scrapy.Field()
    car_skylight = scrapy.Field()
    car_tank_capa = scrapy.Field()
    car_voicebox = scrapy.Field()
    car_seats_type = scrapy.Field()
    car_reverse_radar = scrapy.Field()
    car_airbag = scrapy.Field()
    car_dvd = scrapy.Field()
    car_gps = scrapy.Field()
    car_deposit = scrapy.Field()
    car_day_price = scrapy.Field()
    car_time_out_price = scrapy.Field()
    car_over_kilo_price = scrapy.Field()

class shenZhouSpider(Spider):
    name="shenZhouCars" 
    start_urls = ['https://order.zuche.com/cardetail-%d' %n for n in range(1, 1000)]

    def parse(self, response):
        # print response.body
        value = shenZhouCarsItem()
        item = fieldsItem()
        selector = Selector(response)
        cars = selector.xpath('//ul[@class="carInfor-xj clearfix"]')
        for index in range(0, len(cars), 2):
            basic = cars[index]
            specific = cars[index+1]
            item['car_brand'] = basic.xpath('li[1]/span[1]/text()').re(r'\s+(.*)')[0]
            item['car_series'] = basic.xpath('li[2]/span/text()').re(r'\s+(.*)')[0]
            item['car_issue_date'] = basic.xpath('li[3]/span/text()').re(r'\s+(.*)')[0]
            item['car_config_model'] = basic.xpath('li[4]/span/text()').re(r'\s+(.*)')[0]
            item['car_seats_num'] = specific.xpath('li[1]/span/text()').re(r'\s+(.*)')[0]
            item['car_doors'] = specific.xpath('li[2]/span/text()').re(r'\s+(.*)')[0]
            item['car_fuel_type'] = specific.xpath('li[3]/span/text()').re(r'\s+(.*)')[0]
            item['car_gearbox_type'] = specific.xpath('li[4]/span/text()').re(r'\s+(.*)')[0]
            item['car_displacement'] = specific.xpath('li[5]/span/text()').extract()[0]
            item['car_fuel_num'] = specific.xpath('li[6]/span/text()').re(r'\s+(.*)')[0]
            item['car_drive_way'] = specific.xpath('li[7]/span/text()').re(r'\s+(.*)')[0]
            item['car_engine_intake'] = specific.xpath('li[8]/span/text()').re(r'\s+(.*)')[0]
            item['car_skylight'] = specific.xpath('li[9]/span/text()').re(r'\s+(.*)')[0]
            item['car_tank_capa'] = specific.xpath('li[10]/span/text()').re(r'\s+(.*)')[0]
            item['car_voicebox'] = specific.xpath('li[11]/span/text()').re(r'^\s+(\w*)')[0]
            item['car_seats_type'] = specific.xpath('li[12]/span/text()').re(r'\s+(.*)')[0]
            item['car_reverse_radar'] = specific.xpath('li[13]/span/text()').re(r'\s+(.*)')[0]
            item['car_airbag'] = specific.xpath('li[14]/span/text()').re(r'\s+(\w*)')[0]
            item['car_dvd'] = specific.xpath('li[15]/span/text()').re(r'\s+(.*)')[0]
            item['car_gps'] = specific.xpath('li[16]/span/text()').re(r'\s+(.*)')[0]
            if item['car_airbag'] == u'6510'
                item['car_airbag'] = "0"

            value['model'] = 'RentMe.model_info'
            value['pk'] = item['car_brand']+item['car_series']+item['car_issue_date']+item['car_config_model']
            value['fields'] = {'car_brand': item['car_brand'], 'car_series': item['car_series'], 'car_issue_date': item['car_issue_date'], 'car_config_model': item['car_config_model'], 'car_seats_num': item['car_seats_num'], 'car_doors': item['car_doors'], 'car_fuel_type': item['car_fuel_type'], 'car_gearbox_type': item['car_gearbox_type'], 'car_displacement': item['car_displacement'], 'car_fuel_num': item['car_fuel_num'], 'car_drive_way': item['car_drive_way'], 'car_engine_intake': item['car_engine_intake'], 'car_skylight': item['car_skylight'], 'car_tank_capa': item['car_tank_capa'], 'car_voicebox': item['car_voicebox'], 'car_seats_type': item['car_seats_type'], 'car_reverse_radar': item['car_reverse_radar'], 'car_airbag': item['car_airbag'], 'car_dvd': item['car_dvd'], 'car_gps': item['car_gps'], 'car_deposit': 5000, 'car_day_price': 100, 'car_time_out_price': 150, 'car_over_kilo_price': 0.5}
        yield value
