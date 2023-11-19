class WebPush:
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type):
        self.platform = platform
        self.optin = optin
        self.global_frequency_capping = global_frequency_capping
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.push_type = push_type

    def send_push(self):
        print(f"{self.push_type} Push gönderildi!")


class TriggerPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                 trigger_page):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.trigger_page = trigger_page


class BulkPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type, send_date):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.send_date = send_date


class SegmentPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                 segment_name):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.segment_name = segment_name


class PriceAlertPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type, price_info,
                 discount_rate):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.price_info = price_info
        self.discount_rate = discount_rate

    def discountPrice(self):
        discounted_price = self.price_info * (1 - self.discount_rate)
        return discounted_price


class InstockPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type, stock_info):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.stock_info = stock_info

    def stockUpdate(self):
        self.stock_info = not self.stock_info
        return self.stock_info


trigger_push = TriggerPush("Android", True, 2, "2023-09-10", "2023-09-15", "English", "Trigger", "home")
trigger_push.send_push()

bulk_push = BulkPush("iOS", False, 1, "2023-09-12", "2023-09-20", "Spanish", "Bulk", 1609756800)
bulk_push.send_push()

segment_push = SegmentPush("Web", True, 3, "2023-09-14", "2023-09-16", "French", "Segment", "VIP Customers")
segment_push.send_push()

price_alert_push = PriceAlertPush("iOS", True, 2, "2023-09-11", "2023-09-18", "German", "PriceAlert", 100, 0.15)
discounted_price = price_alert_push.discountPrice()
print(f"İndirimli fiyat: ${discounted_price}")

instock_push = InstockPush("Android", False, 2, "2023-09-13", "2023-09-17", "Italian", "Instock", True)
new_stock_info = instock_push.stockUpdate()
print(f"Yeni stok durumu: {new_stock_info}")
