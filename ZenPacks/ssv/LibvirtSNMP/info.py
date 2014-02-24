from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
from Products.Zuul.decorators import info
from ZenPacks.ssv.LibvirtSNMP import interfaces


class LibvirtSNMPInfo(ComponentInfo):
  implements(interfaces.ILibvirtSNMPInfo)
  guestName = ProxyProperty("guestName")
  guestCpuCount = ProxyProperty("guestCpuCount")
  guestMemoryCurrent = ProxyProperty("guestMemoryCurrent")
  guestMemoryLimit = ProxyProperty("guestMemoryLimit")
