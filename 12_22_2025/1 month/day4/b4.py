from collections import ChainMap

defaults = {'debug':False,'port':8000 }
env = {'debug':True }
cli = {'port':9090}


settings = ChainMap(cli,env,defaults)
print(settings['debug'])
print(settings['port'])