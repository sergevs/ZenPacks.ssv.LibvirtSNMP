__doc__=""" LibvirtSNMPMap

maps libvirt-snmp mibs

$Id: LibvirtSNMP.py,v 1.1 2013/09/05 16:01  Exp $"""

__version__ = '$Revision: 1.1 $'

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap

class LibvirtSNMPMap(SnmpPlugin):
  """
  Map net-snmp subagent shell ping status mib to LibvirtSNMP component
  """
  maptype = "LibvirtSNMP"
# all 3 parameters are required 
  relname = "libvirtsnmp"
  compname = "os"
  modname = 'ZenPacks.ssv.LibvirtSNMP.LibvirtSNMP'

  snmpGetTableMaps = (
      GetTableMap('LibvirtSNMP', '.1.3.6.1.4.1.12345.1.1.1',
              {'.2': 'guestName',
               '.4': 'guestCpuCount',
               '.5': 'guestMemoryCurrent',
               '.6': 'guestMemoryLimit',
              }
      ),
  )

  def process(self, device, results, log):
    """collect snmp information from this device"""
    log.info('processing %s for device %s', self.name(), device.id)

    getdata, tabledata = results
    LibvirtSNMPTable = tabledata.get('LibvirtSNMP')
    log.debug(LibvirtSNMPTable)
    rm = self.relMap()
    for oid, lv in LibvirtSNMPTable.iteritems():
      om = self.objectMap(lv)
      om.id = self.prepId("LibvirtSNMP_%s" % om.guestName)
      om.title = om.guestName
#      om.pingCount = int(om.pingTransmitted)
      log.debug("oid %s" % oid )
      om.snmpindex = oid
#      log.debug("pingTransmitted %s" , om.pingTransmitted )
      rm.append(om)
    
    return rm

