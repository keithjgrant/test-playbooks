#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule
def main():
    module = AnsibleModule(
        argument_spec=dict(
            message=dict(type='str', required=True),
            version=dict(type='str', default='2.23'),
        ),
        supports_check_mode=True,
    )
    module.deprecate(
        msg=module.params['message'],
        version=module.params['version'],
    )
    module.exit_json(changed=False)
if __name__ == '__main__':
    main()
