#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_pi_cloud_instance_info
short_description: Retrieve IBM Cloud 'ibm_pi_cloud_instance' resource

version_added: "2.8"

description:
    - Retrieve an IBM Cloud 'ibm_pi_cloud_instance' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.8.1
    - Terraform v0.12.20

options:
    tenant_id:
        description:
            - None
        required: False
        type: str
    region:
        description:
            - None
        required: False
        type: str
    capabilities:
        description:
            - None
        required: False
        type: list
        elements: str
    total_processors_consumed:
        description:
            - None
        required: False
        type: float
    total_instances:
        description:
            - None
        required: False
        type: float
    total_ssd_storage_consumed:
        description:
            - None
        required: False
        type: float
    pi_cloud_instance_id:
        description:
            - None
        required: True
        type: str
    enabled:
        description:
            - None
        required: False
        type: bool
    pvm_instances:
        description:
            - None
        required: False
        type: list
        elements: dict
    total_standard_storage_consumed:
        description:
            - None
        required: False
        type: float
    creation_date:
        description:
            - None
        required: False
        type: str
    total_memory_consumed:
        description:
            - None
        required: False
        type: float
    zone:
        description:
            - Denotes which IBM Cloud zone to connect to in multizone
              environment. This can also be provided via the environment
              variable 'IC_ZONE'.
        required: False
        type: str
    region:
        description:
            - The IBM Cloud region where you want to create your
              resources. If this value is not specified, us-south is
              used by default. This can also be provided via the
              environment variable 'IC_REGION'.
        default: us-south
        required: False
        type: str
    ibmcloud_api_key:
        description:
            - The IBM Cloud API key to authenticate with the IBM Cloud
              platform. This can also be provided via the environment
              variable 'IC_API_KEY'.
        required: True

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('pi_cloud_instance_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'tenant_id',
    'region',
    'capabilities',
    'total_processors_consumed',
    'total_instances',
    'total_ssd_storage_consumed',
    'pi_cloud_instance_id',
    'enabled',
    'pvm_instances',
    'total_standard_storage_consumed',
    'creation_date',
    'total_memory_consumed',
]

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    tenant_id=dict(
        required=False,
        type='str'),
    region=dict(
        required=False,
        type='str'),
    capabilities=dict(
        required=False,
        elements='',
        type='list'),
    total_processors_consumed=dict(
        required=False,
        type='float'),
    total_instances=dict(
        required=False,
        type='float'),
    total_ssd_storage_consumed=dict(
        required=False,
        type='float'),
    pi_cloud_instance_id=dict(
        required=True,
        type='str'),
    enabled=dict(
        required=False,
        type='bool'),
    pvm_instances=dict(
        required=False,
        elements='',
        type='list'),
    total_standard_storage_consumed=dict(
        required=False,
        type='float'),
    creation_date=dict(
        required=False,
        type='str'),
    total_memory_consumed=dict(
        required=False,
        type='float'),
    zone=dict(
        type='str',
        fallback=(env_fallback, ['IC_ZONE'])),
    region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south'),
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True)
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    result = ibmcloud_terraform(
        resource_type='ibm_pi_cloud_instance',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.8.1',
        tl_required_params=TL_REQUIRED_PARAMETERS,
        tl_all_params=TL_ALL_PARAMETERS)

    if result['rc'] > 0:
        module.fail_json(
            msg=Terraform.parse_stderr(result['stderr']), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()