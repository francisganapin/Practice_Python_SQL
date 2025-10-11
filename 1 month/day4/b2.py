from collections import ChainMap

default = {'theme':'light','lang':'en'}
env_config = {'lang':'fr'}
user_config = {'theme':'dark'}

settings = ChainMap(user_config,env_config,default)

print(settings['theme'])
print(settings['lang'])