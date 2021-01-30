import requests
import json
import time
from pathlib import Path

class _honeydb():
    url = "https://honeydb.io/api"
    
    def __init__(self, apiID, apiKey, ca=None, requestTimeout=30):
        self.requestTimeout = requestTimeout
        self.headers = {
            "X-HoneyDb-ApiId" : apiID,
            "X-HoneyDb-ApiKey" : apiKey
        }
        if ca:
            self.ca = Path(ca)
        else:
            self.ca = None

    def apiCall(self,endpoint,methord="GET",data=None):
        kwargs={}
        kwargs["headers"] = self.headers
        kwargs["timeout"] = self.requestTimeout
        if self.ca:
            kwargs["verify"] = self.ca
        try:
            if methord == "GET":
                response = requests.get("{0}/{1}".format(self.url,endpoint), **kwargs)
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            return 0, "Connection Timeout"
        if response.status_code == 200:
            return json.loads(response.text), response.status_code
        if response.status_code == 429:
            return "Too Many Requests", response.status_code
        return None, response.status_code

    def badHosts(self,filterStr=""):
        if filterStr:
            response, statusCode = self.apiCall("bad-hosts/{0}".format(filterStr))
        else:
            response, statusCode = self.apiCall("bad-hosts")
        return response, statusCode

    def badHostsByService(self,service,filterStr=""):
        if filterStr:
            response, statusCode = self.apiCall("bad-hosts/{0}/{1}".format(service,filterStr))
        else:
            response, statusCode = self.apiCall("bad-hosts/{0}".format(service))
        return response, statusCode

    def ipHistory(self,ip):
        response, statusCode = self.apiCall("ip-history/{0}".format(ip))
        return response, statusCode

    def twitterThreatFeed(self):
        response, statusCode = self.apiCall("twitter-threat-feed")
        return response, statusCode

    def ipLookup(self,ip):
        response, statusCode = self.apiCall("netinfo/lookup/{0}".format(ip))
        return response, statusCode

    def getNetBlock(self,netblock):
        response, statusCode = self.apiCall("netinfo/network-addresses/{0}".format(netblock))
        return response, statusCode

    def getASNPrefixes(self,asn):
        response, statusCode = self.apiCall("netinfo/prefixes/{0}".format(asn))
        return response, statusCode

    def getASNName(self,asn):
        response, statusCode = self.apiCall("netinfo/as-name/{0}".format(asn))
        return response, statusCode

    def IPGeolocation(self,ip):
        response, statusCode = self.apiCall("netinfo/geolocation/{0}".format(ip))
        return response, statusCode

    def isInternetScanner(self,ip):
        response, statusCode = self.apiCall("internet-scanner/{0}".format(ip))
        return response, statusCode

    def getDatacentreIPRanges(self,dataCentre):
        response, statusCode = self.apiCall("datacenter/{0}".format(dataCentre))
        return response, statusCode
