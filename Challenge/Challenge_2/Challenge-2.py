import os
import requests

def main(req):
    metadata_url = "http://169.254.169.254/metadata/instance?api-version=2017-12-01"
    metadata = requests.get(metadata_url).json()

    data_key = req.params.get("data_key")
    if data_key:
        # Return the value for the specific data key
        return {
            "value": metadata.get(data_key)
        }
    else:
        # Return the full metadata
        return {
            "metadata": metadata
        }
##https://learn.microsoft.com/en-us/azure/virtual-machines/windows/instance-metadata-service?tabs=windows - this link is used for learning ##
