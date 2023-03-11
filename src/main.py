import xbmcplugin
import sys
handle = int(sys.argv[1])
xbmcplugin.endOfDirectory(handle, True, updateListing=False, False)