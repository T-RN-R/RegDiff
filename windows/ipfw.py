TEST_STR = """{'FirewallRules': {
'Microsoft-Windows-HomeGroup-ProvSvc-TCP3587-In': 
    'v2.30|Action=Allow|Active=FALSE|Dir=In|Protocol=6|Profile=Private|LPort=3587|RA4=LocalSubnet|RA6=LocalSubnet|App=%%systemroot%%\\system32\\svchost.exe|Svc=p2psvc|Name=@%%systemroot%%\\system32\\provsvc.dll,-200|Desc=@%%systemroot%%\\system32\\provsvc.dll,-201|EmbedCtxt=@%%systemroot%%\\system32\\provsvc.dll,-202|', 
'Microsoft-Windows-HomeGroup-ProvSvc-TCP3587-Out': 
    'v2.30|Action=Allow|Active=FALSE|Dir=Out|Protocol=6|Profile=Private|RPort=3587|RA4=LocalSubnet|RA6=LocalSubnet|App=%%systemroot%%\\system32\\svchost.exe|Svc=p2psvc|Name=@%%systemroot%%\\system32\\provsvc.dll,-203|Desc=@%%systemroot%%\\system32\\provsvc.dll,-204|EmbedCtxt=@%%systemroot%%\\system32\\provsvc.dll,-202|',
 'Microsoft-Windows-HomeGroup-ProvSvc-UDP3540-In': 
    'v2.30|Action=Allow|Active=FALSE|Dir=In|Protocol=17|Profile=Private|LPort=3540|RA4=LocalSubnet|RA6=LocalSubnet|App=%%systemroot%%\\system32\\svchost.exe|Svc=pnrpsvc|Name=@%%systemroot%%\\system32\\provsvc.dll,-205|Desc=@%%systemroot%%\\system32\\provsvc.dll,-206|EmbedCtxt=@%%systemroot%%\\system32\\provsvc.dll,-202|', 
 'Microsoft-Windows-HomeGroup-ProvSvc-UDP3540-Out': 
    'v2.30|Action=Allow|Active=FALSE|Dir=Out|Protocol=17|Profile=Private|RPort=3540|RA4=LocalSubnet|RA6=LocalSubnet|App=%%systemroot%%\\system32\\svchost.exe|Svc=pnrpsvc|Name=@%%systemroot%%\\system32\\provsvc.dll,-207|Desc=@%%systemroot%%\\system32\\provsvc.dll,-208|EmbedCtxt=@%%systemroot%%\\system32\\provsvc.dll,-202|'}, 
 
 'RestrictedServices': 
    {'Static': 
        {'System': 
            {'HomeGroup Allow In':'v2.0|Action=Allow|Dir=In|App=%%SystemRoot%%\\system32\\svchost.exe|Svc=HomeGroupProvider|LPort=3587|Protocol=6|Name=Allow Grouping to receive from port 3587|',
            'HomeGroup Allow In (PRNP)': 'v2.0|Action=Allow|Dir=In|App=%%SystemRoot%%\\system32\\svchost.exe|Svc=HomeGroupProvider|LPort=3540|Protocol=17|Name=Allow PNRP to receive from port 3540|', 
            'HomeGroup Allow Out': 'v2.0|Action=Allow|Dir=Out|App=%%SystemRoot%%\\system32\\svchost.exe|Svc=HomeGroupProvider|RPort=3587|Protocol=6|Name=Allow Grouping to send to port 3587|',
            'HomeGroup Allow Out (PRNP)': 'v2.0|Action=Allow|Dir=Out|App=%%SystemRoot%%\\system32\\svchost.exe|Svc=HomeGroupProvider|RPort=3540|Protocol=17|Name=Allow PNRP to send from port 3540|',
            'HomeGroup Block In': 'V2.0|Action=Block|Dir=In|App=%%SystemRoot%%\\system32\\svchost.exe|Svc=HomeGroupProvider|Name=Block homegroup incoming|', 
            'HomeGroup Block Out': 'V2.0|Action=Block|Dir=Out|App=%%SystemRoot%%\\system32\\svchost.exe|Svc=HomeGroupProvider|Name=Block homegroup outgoing|',
            'HomeGroup Listener Block In': 'V2.0|Action=Block|Dir=In|App=%%SystemRoot%%\\system32\\svchost.exe|Svc=HomeGroupListener|Name=Block all incoming|',
            'HomeGroup Listener Block Out': 'V2.0|Action=Block|Dir=Out|App=%%SystemRoot%%\\system32\\svchost.exe|Svc=HomeGroupListener|Name=Block all outgoing|',
            'SettingSyncHost': 'V2.0|Action=Block|Dir=In|App=%%SystemRoot%%\\system32\\settingsynchost.exe|Name=Block IP traffic to SettingSyncHost|'}}}}"""


fw_rule_list = [
    'v2.30|Action=Allow|Active=FALSE|Dir=In|Protocol=6|Profile=Private|LPort=3587|RA4=LocalSubnet|RA6=LocalSubnet|App=%%systemroot%%\\system32\\svchost.exe|Svc=p2psvc|Name=@%%systemroot%%\\system32\\provsvc.dll,-200|Desc=@%%systemroot%%\\system32\\provsvc.dll,-201|EmbedCtxt=@%%systemroot%%\\system32\\provsvc.dll,-202|', 
    'v2.30|Action=Allow|Active=FALSE|Dir=Out|Protocol=6|Profile=Private|RPort=3587|RA4=LocalSubnet|RA6=LocalSubnet|App=%%systemroot%%\\system32\\svchost.exe|Svc=p2psvc|Name=@%%systemroot%%\\system32\\provsvc.dll,-203|Desc=@%%systemroot%%\\system32\\provsvc.dll,-204|EmbedCtxt=@%%systemroot%%\\system32\\provsvc.dll,-202|',
    'v2.30|Action=Allow|Active=FALSE|Dir=In|Protocol=17|Profile=Private|LPort=3540|RA4=LocalSubnet|RA6=LocalSubnet|App=%%systemroot%%\\system32\\svchost.exe|Svc=pnrpsvc|Name=@%%systemroot%%\\system32\\provsvc.dll,-205|Desc=@%%systemroot%%\\system32\\provsvc.dll,-206|EmbedCtxt=@%%systemroot%%\\system32\\provsvc.dll,-202|', 
    'v2.30|Action=Allow|Active=FALSE|Dir=Out|Protocol=17|Profile=Private|RPort=3540|RA4=LocalSubnet|RA6=LocalSubnet|App=%%systemroot%%\\system32\\svchost.exe|Svc=pnrpsvc|Name=@%%systemroot%%\\system32\\provsvc.dll,-207|Desc=@%%systemroot%%\\system32\\provsvc.dll,-208|EmbedCtxt=@%%systemroot%%\\system32\\provsvc.dll,-202|' 
]
res_rule_list = [
'v2.0|Action=Allow|Dir=In|App=%%SystemRoot%%\\system32\\svchost.exe|Svc=HomeGroupProvider|LPort=3587|Protocol=6|Name=Allow Grouping to receive from port 3587|',
'v2.0|Action=Allow|Dir=In|App=%%SystemRoot%%\\system32\\svchost.exe|Svc=HomeGroupProvider|LPort=3540|Protocol=17|Name=Allow PNRP to receive from port 3540|',
'v2.0|Action=Allow|Dir=Out|App=%%SystemRoot%%\\system32\\svchost.exe|Svc=HomeGroupProvider|RPort=3587|Protocol=6|Name=Allow Grouping to send to port 3587|',
'v2.0|Action=Allow|Dir=Out|App=%%SystemRoot%%\\system32\\svchost.exe|Svc=HomeGroupProvider|RPort=3540|Protocol=17|Name=Allow PNRP to send from port 3540|',
'V2.0|Action=Block|Dir=In|App=%%SystemRoot%%\\system32\\svchost.exe|Svc=HomeGroupProvider|Name=Block homegroup incoming|', 
'V2.0|Action=Block|Dir=Out|App=%%SystemRoot%%\\system32\\svchost.exe|Svc=HomeGroupProvider|Name=Block homegroup outgoing|',
'V2.0|Action=Block|Dir=In|App=%%SystemRoot%%\\system32\\svchost.exe|Svc=HomeGroupListener|Name=Block all incoming|',
'V2.0|Action=Block|Dir=Out|App=%%SystemRoot%%\\system32\\svchost.exe|Svc=HomeGroupListener|Name=Block all outgoing|',
'V2.0|Action=Block|Dir=In|App=%%SystemRoot%%\\system32\\settingsynchost.exe|Name=Block IP traffic to SettingSyncHost|'
]

class FirewallRuleString():
    def __init__(self, raw_rule):   
        self._raw_rule = raw_rule
        if raw_rule.endswith("|"):
            self._raw_rule= self._raw_rule[:-1]
    def parse(self):
        entries = self._raw_rule.split("|")
        if len(entries) == 0:
            return 
        dat = {}
        dat["Version"] = entries[0]
        entries = entries[1:]
        for e in entries:
            k,v = self.entry_tuple(e)
            dat[k] = v
        return dat
    def entry_tuple(self, entry):
        if "=" not in entry:
            print(entry)
        k,v = entry.split("=",1)
        return (k, v)


def test():
    for rule in fw_rule_list:
        print( FirewallRuleString(rule).parse())

    for rule in res_rule_list:
        print( FirewallRuleString(rule).parse())