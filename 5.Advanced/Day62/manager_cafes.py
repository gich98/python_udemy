import pandas
from cafe import Cafe

CAFE_CSV_PATH = "cafe-data.csv"


class ManagerCafes:

    def __init__(self):
        self.data = None
        self.cafes = self.get_cafes()

    def get_cafes(self):
        self.data = pandas.read_csv(CAFE_CSV_PATH)
        print()
        cafes = [
            Cafe(
                name=row.get("Cafe Name"),
                location=row.get("Location"),
                open_cafe=row.get("Open"),
                close_cafe=row.get("Close"),
                coffee=row.get("Coffee"),
                wifi=row.get("Wifi"),
                power=row.get("Power"))
            for (index, row) in self.data.iterrows()]
        return cafes

    def add_cafe(self, new_cafe: Cafe):
        self.cafes.append(new_cafe)
        cafe_name_list = [cafe.name for cafe in self.cafes]
        cafe_location_list = [cafe.location for cafe in self.cafes]
        cafe_open_list = [cafe.open_cafe for cafe in self.cafes]
        cafe_close_list = [cafe.close_cafe for cafe in self.cafes]
        cafe_coffee_list = [cafe.coffee for cafe in self.cafes]
        cafe_wifi_list = [cafe.wifi for cafe in self.cafes]
        cafe_power_list = [cafe.power for cafe in self.cafes]
        cafe_dict = {
            "Cafe Name": cafe_name_list,
            "Location": cafe_location_list,
            "Open": cafe_open_list,
            "Close": cafe_close_list,
            "Coffee": cafe_coffee_list,
            "Wifi": cafe_wifi_list,
            "Power": cafe_power_list,
        }
        cafes_df = pandas.DataFrame(cafe_dict)
        cafes_df.to_csv(CAFE_CSV_PATH)
