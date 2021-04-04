from Fetch import Fetch
from Config import FETCH_PACKAGE

pkg_list = Fetch.package(FETCH_PACKAGE)
if pkg_list.__len__() > 0:
    message = "Packages Successfully Fetched"
    print(message)
else:
    message = "Fetching Failed"
    print(message)

