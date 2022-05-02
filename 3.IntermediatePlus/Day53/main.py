from pprint import pprint
from ZillowRenting import ZillowRenting
from RfRentingResearch import RfRentingResearch


zillowRenting = ZillowRenting()
rfRentingResearch = RfRentingResearch()

for property_ in zillowRenting.properties_dict.values():
    rfRentingResearch.insert_property(property_["address"], property_["price"], property_["link"])
