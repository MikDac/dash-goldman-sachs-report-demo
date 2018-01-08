import pandas as pd
import requests
from io import StringIO

# Read remote csv files (outside SEB firewall)
def readRemoteCsvToDf(urlToCsv):
    """ Read a csv from outside the SEB firewall specifying proxy server
    and by setting SSL Verify to False
    
    Args:
        urlToCsv: string with full path to the csv file
    
    Returns:
        A pandas dataframe of the content in urlToCsv
    """
    
    # Set proxy 
    sebProxy = {"https" : "https://gia.sebank.se:8080"}
    
    # Call the url using requests
    r = requests.get(url = urlToCsv, proxies = sebProxy, verify = False)
    
    # Return as pandas dataframe
    return pd.read_csv(StringIO(r.text))