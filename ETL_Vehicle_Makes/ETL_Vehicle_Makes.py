import glob
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime

###########################################################################
log_file = "log_file.txt"
target_file = "transformed_data.csv"

###########################################################################

def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    return dataframe

def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process, lines=True)
    return dataframe

def extract_from_xml(file_to_process):
    dataframe = pd.DataFrame(columns=["car_model", "year_of_manufacture", "price", "fuel"])
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for vehicle in root:
        car_name = vehicle.find("car_model").text
        car_manufactured_year = int(vehicle.find("year_of_manufacture").text)
        price_of_car = float(vehicle.find("price").text)
        fuel = vehicle.find("fuel").text
        dataframe = pd.concat([dataframe, pd.DataFrame([
            {"car_model": car_name, "year_of_manufacture": car_manufactured_year, "price": price_of_car, "fuel": fuel}])],
                              ignore_index=True)
    return dataframe

###########################################################################

def extract():
    extracted_data = pd.DataFrame(columns=['car_model','year_of_manufacture', 'price', 'fuel'])

    # process all csv files
    for csvfile in glob.glob("./Data/*.csv"):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_csv(csvfile))], ignore_index=True)

        # process all json files
    for jsonfile in glob.glob("./Data/*.json"):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_json(jsonfile))], ignore_index=True)

        # process all xml files
    for xmlfile in glob.glob("./Data/*.xml"):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_xml(xmlfile))], ignore_index=True)

    return extracted_data

###########################################################################

def transform(data):
    # Convert Price from USD to INR
    data['price'] = round(data.price * 83.61, 2)
    return data

###########################################################################

def load(target_file, data_to_load):
    data_to_load.to_csv(target_file, index=False)

###########################################################################

def log(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(log_file, "a") as file:
        file.write(timestamp + ',' + message + '\n')

###########################################################################

if __name__ == "__main__":
    log("ETL Job Started")
    log("Extract phase Started")
    data = extract()
    log("Extract phase Ended")
    log("Transform phase Started")
    data = transform(data)
    log("Transform phase Ended")
    log("Load phase Started")
    load(target_file, data)
    log("Load phase Ended")
    log("ETL Job Completed")