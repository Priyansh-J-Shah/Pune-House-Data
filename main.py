from distutils.command.config import config
from flask import Flask,render_template,jsonify,request
from Model.utils import PuneHouseData
import config

app = Flask(__name__)

@app.route("/")
def hello_flask() :
    print ("Welcome to House Price Prediction in Pune")
    return render_template ("index.html")

@app.route("/predict_price",methods = ["POST","GET"])
def House_price () :

    if request.method == "GET" :
        print ("We are using GET Method")

        area_type = request.args.get("area_type")
        availability = request.args.get("availability")
        size = request.args.get("size")
        total_sqft = float(request.args.get("total_sqft"))
        bath = float(request.args.get("bath"))
        balcony = float(request.args.get("balcony"))
        site_location = request.args.get("site_location")

        print ("""area_type,availability,size,total_sqft,bath,balcony,site_location\n""",
        area_type,availability,size,total_sqft,bath,balcony,site_location)

        Pune_house_data = PuneHouseData(area_type,availability,size,total_sqft,bath,balcony,site_location)
        price = Pune_house_data.get_predicted_price()

        return render_template("index.html",prediction = price)

    else : 
        print ("We are using Post Method")

        area_type = request.form.get("area_type")
        availability = request.form.get("availability")
        size = request.form.get("size")
        total_sqft = float(request.form.get("total_sqft"))
        bath = float(request.form.get("bath"))
        balcony = float(request.form.get("balcony"))
        site_location = request.form.get("site_location")

        print ("""area_type,availability,size,total_sqft,bath,balcony,site_location\n""",
        area_type,availability,size,total_sqft,bath,balcony,site_location)

        Pune_house_data = PuneHouseData(area_type,availability,size,total_sqft,bath,balcony,site_location)
        price = Pune_house_data.get_predicted_price()

        return render_template("index.html",prediction = price)

if __name__ == "__main__" :
    app.run(host = "0.0.0.0",port = config.PORT_NUMBER , debug = True)