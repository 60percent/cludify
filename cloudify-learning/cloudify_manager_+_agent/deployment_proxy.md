Deployment Proxy
================

download and install utility plugin from:

https://github.com/cloudify-incubator/cloudify-utilities-plugin/archive/1.9.0.zip

install deployment_proxy.yml

cfy install deployment_proxy.xml -d one -b one

use `cfy deployments inputs` to check the outputs of first step are passed to inputs of second step.

more example:

https://cloudify.co/2018/04/25/how-to-use-cloudifys-deployment-proxy-to-pass-parameters-between-deployments-and-more
