#!/usr/bin/env python
# -*- coding: utf-8 -*-

DOCUMENTATION = '''
---
module: your module name here
author: your name here
short_description: a short description
description:
    - a longer description
options:
    name:
        required: true
        description:
            - Name of the container
    other_arg:
        description:
            - the other_arg description
'''

from ansible.module_utils.basic import *


def main():
    module = AnsibleModule(
            argument_spec = dict(
                name = dict(
                    required= True,
                    type = 'str',
                    ),
                other_arg = dict(
                    # provide a default if
                    # not required
                    default = 'spam',
                    required = False,
                    # always add the type
                    # to let ansible check
                    # your module call
                    type = 'str',
                    ),
            ),
            # can you predict if there will
            # be any changes?
            supports_check_mode=True
    )
    
    try:
        import lxc
    except ImportError:
        module.fail_json(
                changed = False,
                # A task can also fail
                # and stop the playbook
                # execution
                #failure = True,
                msg = 'Error importing lxc, is python-lxc installed?',
                )

    container_name = module.params.get('name')
    other_arg = module.params.get('other_arg')

    result = {}
    result['name'] = container_name
    result['other_arg'] = other_arg

    if container_name in lxc.list_containers():
        result['exists'] = True
        # do other things in here
    else:
        result['exists'] = False
        module.exit_json(**result)

    result['changed'] = True
    module.exit_json(**result)

if __name__ == '__main__':
    main()
