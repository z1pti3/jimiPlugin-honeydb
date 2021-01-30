import jimi

class _honeydb(jimi.plugin._plugin):
    version = 0.1

    def install(self):
        # Register models
        jimi.model.registerModel("honeydbBadHosts","_honeydbBadHosts","_action","plugins.honeydb.models.action")
        jimi.model.registerModel("honeydbBadHostsByService","_honeydbBadHostsByService","_action","plugins.honeydb.models.action")
        jimi.model.registerModel("honeydbIPHistory","_honeydbIPHistory","_action","plugins.honeydb.models.action")
        jimi.model.registerModel("honeydbIPLookup","_honeydbIPLookup","_action","plugins.honeydb.models.action")
        jimi.model.registerModel("honeydbIPGeolocation","_honeydbIPGeolocation","_action","plugins.honeydb.models.action")
        jimi.model.registerModel("honeydbIsInternetScanner","_honeydbIsInternetScanner","_action","plugins.honeydb.models.action")
        jimi.model.registerModel("honeydbGetNetblock","_honeydbGetNetblock","_action","plugins.honeydb.models.action")
        jimi.model.registerModel("honeydbTwitterThreatFeed","_honeydbTwitterThreatFeed","_action","plugins.honeydb.models.action")
        jimi.model.registerModel("honeydbASNPrefixes","_honeydbASNPrefixes","_action","plugins.honeydb.models.action")
        jimi.model.registerModel("honeydbGetASNName","_honeydbGetASNName","_action","plugins.honeydb.models.action")
        jimi.model.registerModel("honeydbDatacenterIPRanges","_honeydbDatacenterIPRanges","_action","plugins.honeydb.models.action")
        return True

    def uninstall(self):
        # deregister models
        jimi.model.deregisterModel("honeydbBadHosts","_honeydbBadHosts","_action","plugins.honeydb.models.action")
        jimi.model.deregisterModel("honeydbBadHostsByService","_honeydbBadHostsByService","_action","plugins.honeydb.models.action")
        jimi.model.deregisterModel("honeydbIPHistory","_honeydbIPHistory","_action","plugins.honeydb.models.action")
        jimi.model.deregisterModel("honeydbIPLookup","_honeydbIPLookup","_action","plugins.honeydb.models.action")
        jimi.model.deregisterModel("honeydbIPGeolocation","_honeydbIPGeolocation","_action","plugins.honeydb.models.action")
        jimi.model.deregisterModel("honeydbIsInternetScanner","_honeydbIsInternetScanner","_action","plugins.honeydb.models.action")
        jimi.model.deregisterModel("honeydbGetNetblock","_honeydbGetNetblock","_action","plugins.honeydb.models.action")
        jimi.model.deregisterModel("honeydbTwitterThreatFeed","_honeydbTwitterThreatFeed","_action","plugins.honeydb.models.action")
        jimi.model.deregisterModel("honeydbASNPrefixes","_honeydbASNPrefixes","_action","plugins.honeydb.models.action")
        jimi.model.deregisterModel("honeydbGetASNName","_honeydbGetASNName","_action","plugins.honeydb.models.action")
        jimi.model.deregisterModel("honeydbDatacenterIPRanges","_honeydbDatacenterIPRanges","_action","plugins.honeydb.models.action")
        return True

    def upgrade(self,LatestPluginVersion):
        pass
        #if self.version < 0.2:
