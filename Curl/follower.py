import pycurl
from io import BytesIO
import re
import sys

def get_redirect(url):
    print("READ  %s" % url)
    buffer = BytesIO()
    curl = pycurl.Curl()
    curl.setopt(curl.URL, url)
    curl.setopt(curl.WRITEDATA, buffer)
    curl.perform()
    redirect = curl.getinfo(pycurl.REDIRECT_URL)
    if redirect is not None:
        print("      ↳ [{1}] {0}".format(redirect, curl.getinfo(pycurl.HTTP_CODE)))
        curl.close()
        return redirect
    body = buffer.getvalue().decode()
    reg = re.compile(r"^.+window\.location\.href='(.+)'.+$", re.MULTILINE|re.DOTALL)
    result = reg.findall(body)
    if len(result) != 0:
        print("      ↳ [JS] %s" % result[0])
        curl.close()
        return result[0]
    curl.close()

redirect = sys.argv[1]
while redirect is not None:
    redirect = get_redirect(redirect)
    print()
