import json
import os

# edit data
data=json.loads(open('.data/data.json').read())
data['classname']=input('classname >> ')
data['loc']=input('aula >> ')
f=open('.data/data.json', 'w')
f.write(json.dumps(data))
f.close()

print('[*] Successfully setted')
print('[..] press enter to delete the config file.')
input()
os.remove("setup.py")