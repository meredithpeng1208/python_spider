# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    district_id = scrapy.Field()
    lng = scrapy.Field()
    lat = scrapy.Field()
    name = scrapy.Field()
    project_name = scrapy.Field()
    min_frame_area = scrapy.Field()
    max_frame_area = scrapy.Field()
    price = scrapy.Field()
    average_price = scrapy.Field()
    image_url = scrapy.Field()
    rooms = scrapy.Field()
    frame_area = scrapy.Field()
    house_type = scrapy.Field()
    price_show_config = scrapy.Field()
    show_price_unit = scrapy.Field()
    show_price_desc = scrapy.Field()


# 行政区
class LJDistrictItem(scrapy.Item):
    # define the fields for your item here like:
    district_id = scrapy.Field()
    lng = scrapy.Field()
    lat = scrapy.Field()
    district_name = scrapy.Field()
    quanpin = scrapy.Field()
    position_border = scrapy.Field()
    count = scrapy.Field()


# 区域商圈
class LJBizCircleItem(scrapy.Item):
    house_count = scrapy.Field()
    min_price_total = scrapy.Field()
    area_id = scrapy.Field()
    area_name = scrapy.Field()
    position_border = scrapy.Field()
    lng = scrapy.Field()
    lat = scrapy.Field()
    avg_unit_price = scrapy.Field()


# 房天下城市区域数据
class FangDistAreaItem(scrapy.Item):
    source_id = scrapy.Field()
    name = scrapy.Field()
    # x
    lng = scrapy.Field()
    # y
    lat = scrapy.Field()
    quanpin = scrapy.Field()
    position_border = scrapy.Field()
    area_list = scrapy.Field()


# 房天下学校列表
class FangSchoolListItem(scrapy.Item):
    short_name = scrapy.Field()
    name = scrapy.Field()
    img_url = scrapy.Field()
    address = scrapy.Field()
    community_count = scrapy.Field()
    school_note_tag = scrapy.Field()
    # 先将特色标签放入到 feature中
    tags = scrapy.Field()
    tel_number = scrapy.Field()
    guide = scrapy.Field()
    students_scope = scrapy.Field()
    conditions = scrapy.Field()
    intro = scrapy.Field()
    feature = scrapy.Field()
    detail_link = scrapy.Field()
