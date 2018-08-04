How to build cloudify-utility-plugin
====================================

# Files changed

```
setup.py
cloudify_deployment_proxy/__init__.py
cloudify_deployment_proxy/cmdb.py
```

# Prepare wagon build env

```
sudo yum install python-devel gcc
sudo pip install wagon
```

# Build package

```
zip -r cloudify-utilities-plugin.zip cloudify-utilities-plugin
wagon create -a '--no-cache-dir -c cloudify-utilities-plugin/constraints.txt' cloudify-utilities-plugin.zip
```

