import tqdm
import requests
import fastadd

import libs.common.util as util

print(fastadd.add(1, 2))
print(util.add(3, 4))
util.tq()
print('service tqdm', tqdm.__version__)
print('service requests', requests.__version__)