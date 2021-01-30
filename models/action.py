import jimi
from plugins.honeydb.includes import honeydb

class _honeydbBadHosts(jimi.action._action):
    apiID = str()
    apiKey = str()
    filterStr = str()

    def run(self,data,persistentData,actionResult):
        apiID = jimi.auth.getPasswordFromENC(self.apiID)
        apiKey = jimi.auth.getPasswordFromENC(self.apiKey)
        filterStr = jimi.helpers.evalString(self.filterStr,{"data" : data})

        result, statusCode = honeydb._honeydb(apiID,apiKey).badHosts(filterStr)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["badhosts"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from honeydb API"
        return actionResult 

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiID" and not value.startswith("ENC "):
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiID = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        if attr == "apiKey" and not value.startswith("ENC "):
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiKey = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        return super(_honeydbBadHosts,self).setAttribute(attr,value,sessionData=sessionData)

class _honeydbBadHostsByService(jimi.action._action):
    apiID = str()
    apiKey = str()
    filterStr = str()
    service = str()

    def run(self,data,persistentData,actionResult):
        apiID = jimi.auth.getPasswordFromENC(self.apiID)
        apiKey = jimi.auth.getPasswordFromENC(self.apiKey)
        filterStr = jimi.helpers.evalString(self.filterStr,{"data" : data})
        service = jimi.helpers.evalString(self.service,{"data" : data})

        result, statusCode = honeydb._honeydb(apiID,apiKey).badHostsByService(service,filterStr)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["badhosts"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from honeydb API"
        return actionResult 

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiID" and not value.startswith("ENC "):
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiID = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        if attr == "apiKey" and not value.startswith("ENC "):
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiKey = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        return super(_honeydbBadHostsByService,self).setAttribute(attr,value,sessionData=sessionData)

class _honeydbIPHistory(jimi.action._action):
    apiID = str()
    apiKey = str()
    ip = str()

    def run(self,data,persistentData,actionResult):
        apiID = jimi.auth.getPasswordFromENC(self.apiID)
        apiKey = jimi.auth.getPasswordFromENC(self.apiKey)
        ip = jimi.helpers.evalString(self.ip,{"data" : data})

        result, statusCode = honeydb._honeydb(apiID,apiKey).ipHistory(ip)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["ipHistory"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from honeydb API"
        return actionResult 

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiID" and not value.startswith("ENC "):
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiID = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        if attr == "apiKey" and not value.startswith("ENC "):
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiKey = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        return super(_honeydbIPHistory,self).setAttribute(attr,value,sessionData=sessionData)

class _honeydbIPLookup(jimi.action._action):
    apiID = str()
    apiKey = str()
    ip = str()

    def run(self,data,persistentData,actionResult):
        apiID = jimi.auth.getPasswordFromENC(self.apiID)
        apiKey = jimi.auth.getPasswordFromENC(self.apiKey)
        ip = jimi.helpers.evalString(self.ip,{"data" : data})

        result, statusCode = honeydb._honeydb(apiID,apiKey).ipLookup(ip)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["ipLookup"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from honeydb API"
        return actionResult 

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiID" and not value.startswith("ENC "):
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiID = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        if attr == "apiKey" and not value.startswith("ENC "):
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiKey = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        return super(_honeydbIPLookup,self).setAttribute(attr,value,sessionData=sessionData)

class _honeydbIPGeolocation(jimi.action._action):
    apiID = str()
    apiKey = str()
    ip = str()

    def run(self,data,persistentData,actionResult):
        apiID = jimi.auth.getPasswordFromENC(self.apiID)
        apiKey = jimi.auth.getPasswordFromENC(self.apiKey)
        ip = jimi.helpers.evalString(self.ip,{"data" : data})

        result, statusCode = honeydb._honeydb(apiID,apiKey).IPGeolocation(ip)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["location"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from honeydb API"
        return actionResult 

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiID" and not value.startswith("ENC "):
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiID = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        if attr == "apiKey" and not value.startswith("ENC "):
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiKey = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        return super(_honeydbIPGeolocation,self).setAttribute(attr,value,sessionData=sessionData)

class _honeydbIsInternetScanner(jimi.action._action):
    apiID = str()
    apiKey = str()
    ip = str()

    def run(self,data,persistentData,actionResult):
        apiID = jimi.auth.getPasswordFromENC(self.apiID)
        apiKey = jimi.auth.getPasswordFromENC(self.apiKey)
        ip = jimi.helpers.evalString(self.ip,{"data" : data})

        result, statusCode = honeydb._honeydb(apiID,apiKey).isInternetScanner(ip)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["internetScanner"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from honeydb API"
        return actionResult 

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiID" and not value.startswith("ENC "):
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiID = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        if attr == "apiKey" and not value.startswith("ENC "):
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiKey = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        return super(_honeydbIsInternetScanner,self).setAttribute(attr,value,sessionData=sessionData)

class _honeydbGetNetblock(jimi.action._action):
    apiID = str()
    apiKey = str()
    netblock = str()

    def run(self,data,persistentData,actionResult):
        apiID = jimi.auth.getPasswordFromENC(self.apiID)
        apiKey = jimi.auth.getPasswordFromENC(self.apiKey)
        netblock = jimi.helpers.evalString(self.netblock,{"data" : data})

        result, statusCode = honeydb._honeydb(apiID,apiKey).getNetBlock(netblock)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["netblock"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from honeydb API"
        return actionResult 

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiID" and not value.startswith("ENC "):
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiID = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        if attr == "apiKey" and not value.startswith("ENC "):
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiKey = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        return super(_honeydbGetNetblock,self).setAttribute(attr,value,sessionData=sessionData)

class _honeydbTwitterThreatFeed(jimi.action._action):
    apiID = str()
    apiKey = str()

    def run(self,data,persistentData,actionResult):
        apiID = jimi.auth.getPasswordFromENC(self.apiID)
        apiKey = jimi.auth.getPasswordFromENC(self.apiKey)

        result, statusCode = honeydb._honeydb(apiID,apiKey).twitterThreatFeed()

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["twitterThreatFeed"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from honeydb API"
        return actionResult 

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiID" and not value.startswith("ENC "):
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiID = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        if attr == "apiKey" and not value.startswith("ENC "):
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiKey = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        return super(_honeydbTwitterThreatFeed,self).setAttribute(attr,value,sessionData=sessionData)

class _honeydbASNPrefixes(jimi.action._action):
    apiID = str()
    apiKey = str()
    asn = str()

    def run(self,data,persistentData,actionResult):
        apiID = jimi.auth.getPasswordFromENC(self.apiID)
        apiKey = jimi.auth.getPasswordFromENC(self.apiKey)
        asn = jimi.helpers.evalString(self.asn,{"data" : data})

        result, statusCode = honeydb._honeydb(apiID,apiKey).getASNPrefixes(asn)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["asnPrefixes"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from honeydb API"
        return actionResult 

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiID" and not value.startswith("ENC "):
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiID = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        if attr == "apiKey" and not value.startswith("ENC "):
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiKey = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        return super(_honeydbASNPrefixes,self).setAttribute(attr,value,sessionData=sessionData)

class _honeydbGetASNName(jimi.action._action):
    apiID = str()
    apiKey = str()
    asn = str()

    def run(self,data,persistentData,actionResult):
        apiID = jimi.auth.getPasswordFromENC(self.apiID)
        apiKey = jimi.auth.getPasswordFromENC(self.apiKey)
        asn = jimi.helpers.evalString(self.asn,{"data" : data})

        result, statusCode = honeydb._honeydb(apiID,apiKey).getASNName(asn)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["asnDetails"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from honeydb API"
        return actionResult 

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiID" and not value.startswith("ENC "):
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiID = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        if attr == "apiKey" and not value.startswith("ENC "):
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiKey = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        return super(_honeydbGetASNName,self).setAttribute(attr,value,sessionData=sessionData)

class _honeydbDatacenterIPRanges(jimi.action._action):
    apiID = str()
    apiKey = str()
    datacenterName = str()

    def run(self,data,persistentData,actionResult):
        apiID = jimi.auth.getPasswordFromENC(self.apiID)
        apiKey = jimi.auth.getPasswordFromENC(self.apiKey)
        datacenterName = jimi.helpers.evalString(self.datacenterName,{"data" : data})

        result, statusCode = honeydb._honeydb(apiID,apiKey).getDatacentreIPRanges(datacenterName)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["datacenterIPs"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from honeydb API"
        return actionResult 

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiID" and not value.startswith("ENC "):
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiID = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        if attr == "apiKey" and not value.startswith("ENC "):
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiKey = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        return super(_honeydbDatacenterIPRanges,self).setAttribute(attr,value,sessionData=sessionData)