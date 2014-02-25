# ZenReports.Utils contains some useful helpers for creating records to return.
from Products.ZenReports.Utils import Record
from Products.ZenReports.AliasPlugin import AliasPlugin
import re
import logging
log = logging.getLogger("zen.Reports")


# The class name must match the filename.
class  LibvirtSNMP_plugin(AliasPlugin):

    # The run method will be executed when your report calls the plugin.
    def run(self, dmd, args):
        report = []
        for device in dmd.Devices.getSubDevicesGen():
            if device.os.libvirtsnmp():
                for lcomp in sorted( device.os.libvirtsnmp(), key=lambda x: x.guestName ):
                  guestUrl=dmd.Devices.findDevice(lcomp.guestName).getPrimaryUrlPath() if dmd.Devices.findDevice(lcomp.guestName) else ''
                  report.append(Record( device=device, deviceName=device.titleOrId(), guestName = lcomp.guestName, guestUrl = guestUrl, guestCpuCount = lcomp.guestCpuCount, guestMemory = lcomp.guestMemoryCurrent)) 

        return report
