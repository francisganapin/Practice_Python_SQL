from collections import OrderedDict

class RecentlyViewed:
    def __init__(self,limit=5):
        self.viewed = OrderedDict()
        self.limit = limit

    def view(self,product_id):
        if product_id in self.viewed:
            self.viewed.pop(product_id)
        self.viewed[product_id] = True

        if len(self.viewed) > self.limit:
            self.viewed.popitem(last=False)
    
    def get_recently_viewed(self):
        return list(self.viewed.keys())[::-1]
    

recent = RecentlyViewed(limit=2)
recent.view('Whey001')
recent.view('Crea001')
recent.view('Pre001')
recent.view('Bcaa001')
recent.view('Multi001')
recent.view('Crea001')
recent.view('Fish001')

print(recent.get_recently_viewed())