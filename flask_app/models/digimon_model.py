#*********************************************
#******************IMPORTS********************
#*********************************************

#===================================
# Import App
#===================================
from flask_app import app

#===================================
# Import Packages/Modules
#===================================
import requests, json

#*********************************************
#*****************API CALLS*******************
#*********************************************

#===================================
# Get Digimon [ONE] Info
#===================================
async def get_digimon_info(req):

    if type(req)==list:
        digimon_info = []
        for digimon_number in req:
            url = f'http://digi-api.com/api/v1/digimon/{digimon_number}'
            one_digimon = requests.get(url).json()
            digimon_info.append(one_digimon)

    else:
        url = f'http://digi-api.com/api/v1/digimon/{req}'
        digimon_info = requests.get(url)
        digimon_info = digimon_info.json()

    return digimon_info
