from datetime import date

from gazette.spiders.base.doem import DoemGazetteSpider


class BaCanudosSpider(DoemGazetteSpider):
    TERRITORY_ID = "2906824"
    name = "ba_canudos"
    start_date = date(2013, 1, 4)  # edition number 444
    state_city_url_part = "ba/canudos"
