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
import requests

#*********************************************
#*****************API CALLS*******************
#*********************************************

#===================================
# Get Digimon [ONE] Info
#===================================
async def get_digimon_info(req):
    url = f'http://digi-api.com/api/v1/digimon/{req}'
    digimon_info = requests.get(url)
    digimon_info = digimon_info.json()
    print("Grabbed digi info")

    return digimon_info
