import ipfshttpclient

client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')

res = client.add('test.txt')
print(res)

#print(client.get('https://ipfs.io/ipfs/QmdjGhZVXRY9YRQSc86mpeD5L9ae49a6v3DF69VntDLWC9?filename=QmdjGhZVXRY9YRQSc86mpeD5L9ae49a6v3DF69VntDLWC9'))

import urllib.request
import json

with urllib.request.urlopen(f'https://ipfs.io/ipfs/QmdjGhZVXRY9YRQSc86mpeD5L9ae49a6v3DF69VntDLWC9?filename=QmdjGhZVXRY9YRQSc86mpeD5L9ae49a6v3DF69VntDLWC9') as url:
    data = json.loads(url.read())
