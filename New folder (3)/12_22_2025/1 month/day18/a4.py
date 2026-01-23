def make_adder(x):
    def adder(n):
        return x + n
    return adder



adder_fn = make_adder(10)


closure_data = {
    'type':"adder",
    "x":10
}

import json
with open('closure_config.json','w') as f:
    json.dump(closure_data,f)