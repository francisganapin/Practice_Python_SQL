import json



class ConfigLoader:
    def __init__(self,path):
        self.path = path
        with open(self.path,'r') as f:
            self.config = json.load(f)

    def get(self,key,default=None):
        return self.config.get(key,default)
    
    def save(self):
        with open(self.path,'w') as f:
            json.dump(self.config,f,indent=4)

    def update(self,key,value):
        self.config['key'] = value
        self.save()

cfg = ConfigLoader('config.json')
print('App name:',cfg.get('app_name'))
cfg.update('debug',True)