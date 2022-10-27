import pickle
import json
import numpy as np
import pandas as pd
import config

class PuneHouseData() :
    def __init__ (self,area_type,availability,size,total_sqft,bath,balcony,site_location) :
        
        self.area_type = "area_type_" + area_type
        self.availability = availability
        self.size = size
        self.total_sqft = total_sqft
        self.bath = bath
        self.balcony = balcony
        self.site_location = "site_location_" + site_location


    def load_model (self) :
        with open (config.Pune_MODEL_FILE_PATH,"rb") as f:
            self.model = pickle.load(f)
        with open (config.Pune_JSON_FILE_PATH) as f:
            self.json_data = json.load(f)

    def get_predicted_price (self) :
        self.load_model()

        area_type_index = self.json_data["columns"].index(self.area_type)
        site_location_index = self.json_data["columns"].index(self.site_location)

        array = np.zeros(len(self.json_data["columns"]))

        array[0] = self.json_data["availability"][self.availability]
        array[1] = self.json_data["size"][self.size]
        array[2] = self.total_sqft
        array[3] = self.bath
        array[4] = self.balcony
        array[area_type_index] = 1
        array[site_location_index] = 1

        print ("Test Array :\n",array)
        predicted_price = self.model.predict([array])[0]
        print ("Predicted Price :",predicted_price)
        return np.around(predicted_price,2)

if __name__ == "__main__" :
    area_type = "Plot  Area"
    availability = "18-May"
    size = "3 BHK"
    total_sqft = 3050
    bath = 2
    balcony = 1
    site_location = "Dehu Road"

    Pune_house_data = PuneHouseData(area_type,availability,size,total_sqft,bath,balcony,site_location)
    price = Pune_house_data.get_predicted_price()
    print ()
    print (f"Price Prediction of House in Pune {price}")