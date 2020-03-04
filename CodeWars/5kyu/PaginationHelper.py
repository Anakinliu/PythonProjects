# https://www.codewars.com/kata/515bb423de843ea99400000a/train/python
from math import  ceil

class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.col = collection
        self.ipp = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.col)

    # returns the number of pages
    def page_count(self):
        return int(ceil(self.item_count() / self.ipp))
    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        # page_index页面有几个元素
        if page_index >= self.page_count():
            return -1
        if page_index < self.page_count() - 1:
            # return self.col[self.ipp * page_index: self.ipp * (page_index + 1)]
            return self.ipp
        else:
            # return self.col[self.item_count() - self.item_count() % self.ipp:]
            return self.item_count() % self.ipp

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index < 0 or item_index >= self.item_count():
            return -1
        return item_index // self.ipp

helper = PaginationHelper(['a','b','c','d','e','f'], 4)

# print(helper.page_count()) # should == 2
# print(helper.item_count()) # should == 6
# print(helper.page_item_count(0))  # should == 4
# print(helper.page_item_count(1)) # last page - should == 2
# print(helper.page_item_count(2)) # should == -1 since the page is invalid

print(helper.page_index(5)) # should == 1 (zero based index)
print(helper.page_index(2)) # should == 0
print(helper.page_index(20))# should == -1
print(helper.page_index(-10)) # should == -1 because negative indexes are invalid