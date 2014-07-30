import json

def handle(fname):
        f = file(fname)
        asset_dic = json.load(f)

        for k,v in  asset_dic.items():
		print k,v

asset_file ='/tmp/triaquae_asset_collection.temp.bao'
handle(asset_file)
