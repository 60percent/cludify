import zipfile
import urllib
import requests
import string
import json
import random
import yaml
import os
CMDB='http://192.168.33.1:5000'
CMDB_HEADER={'Content-Type': 'application/json', 'Authorization':'Basic cm9vdDpyb290cHdk'}
CMDB_GET_HEADER={'Authorization':'Basic cm9vdDpyb290cHdk'}
CONFIG_TYPE_URL="{CMDB}/api/v1/ConfigType".format(CMDB=CMDB)
CONFIG_ITEM_URL="{CMDB}/api/v1/ConfigItem".format(CMDB=CMDB)
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def create_config_type_per_bf(ctx, archive_url, blueprint_id, blueprint_file_name):
    resp = requests.get("%s/ppc-%s-1.0.0" % (CONFIG_TYPE_URL, blueprint_id), headers = CMDB_GET_HEADER).json()
    if 'data' in resp:
        ctx.logger.info("%s exist" % resp['data']['id'])
        ctx.instance.runtime_properties['config_type'] = resp['data']['id']
        return
    zipname = '/tmp/%s.zip' % id_generator()
    folder = '/tmp/%s' % id_generator()

    urllib.urlretrieve(archive_url, zipname)
    with zipfile.ZipFile(zipname, 'r') as zip_ref:
        for n in zip_ref.namelist():
            fname = os.path.join(folder, n)
            if n.endswith(blueprint_file_name) and fname.endswith('/' + blueprint_file_name):
                zip_ref.extract(n, folder)
                with open(fname, 'r') as bf:
                    content = yaml.load(bf)
                    inputs = content.get('inputs', {})
                    outputs = content.get('outputs', {})
                    props = [p for p in inputs] + [p for p in outputs]
                    props.append('deployment_id')
                    payload = {
                            'name': blueprint_id,
                            'namespace': 'ppc',
                            'inheritance': 'Vertex',
                            'properties': [{'name': p, 'type': 'STRING'} for p in props]
                            }
                    ctx.logger.info(payload)
                    resp = requests.post(CONFIG_TYPE_URL, data=json.dumps(payload), headers=CMDB_HEADER).json()
                    ctx.logger.info(resp)
                    ctx.instance.runtime_properties['config_type'] = resp['data']['id']

def create_config_type_per_node(ctx, **kwarg):
    pass

def create_config_item_per_bf(ctx, deployment_id, props):
    config_type = ctx.instance.runtime_properties['config_type']
    resp = requests.get("%s?type=%s&filter=deployment_id='%s'" % (CONFIG_ITEM_URL, config_type, deployment_id), headers=CMDB_GET_HEADER).json()
    if 'data' in resp and len(resp['data']) > 0:
        ctx.instance.runtime_properties['config_item_id'] = resp['data'][0]['id']
        return
    payload = {
            'type': config_type,
            'properties': props.copy()
            }
    payload['properties']['deployment_id'] = deployment_id
    ctx.logger.info(payload)
    resp = requests.post(CONFIG_ITEM_URL, data=json.dumps(payload), headers=CMDB_HEADER).json()
    ctx.logger.info(resp)
    ctx.instance.runtime_properties['config_item_id'] = resp['data']['id']

def update_config_item_per_bf(ctx, props):
    config_item_id = ctx.instance.runtime_properties['config_item_id']
    payload = {
            'properties': props
            }
    ctx.logger.info(payload)
    resp = requests.patch("%s/%s" % (CONFIG_ITEM_URL,config_item_id), json.dumps(payload), headers=CMDB_HEADER).json()
    ctx.logger.info(resp)

def delete_config_item(ctx, deployment_id):
    pass

def create_config_item_per_node(ctx, blueprint_id, node_id, props):
    pass

def update_config_item_per_node(ctx, blueprint_id, deployment_id, node_id, props):
    pass
