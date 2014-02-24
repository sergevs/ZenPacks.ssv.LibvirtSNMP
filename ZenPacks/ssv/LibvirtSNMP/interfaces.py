from Products.Zuul.interfaces import IComponentInfo
from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t


class ILibvirtSNMPInfo(IComponentInfo):
    guestName = schema.Entity(title=u"Guest name", readonly=True, group='Details')
    guestCpuCount = schema.Int(title=u"Number of CPU", readonly=True, group='Details')
    guestMemoryCurrent = schema.Int(title=u"Memory Current", readonly=True, group='Details')
    guestMemoryLimit = schema.Int(title=u"Memory Limit", readonly=True, group='Details')

