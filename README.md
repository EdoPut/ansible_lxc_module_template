# Using LXC in Ansible modules

This repository provides the boilerplate to work with LXC containers in Ansible.

If you need to manage the state, configuration or network of a container the module [lxc_container][lxc_container] is a more appropriate choice or, if you need only basic interactions you can try [lilik_container][lilik_container], our Python only module to manage container state.

## Examples

### container_exists

Check if the given **name** argument maps to a container on the host.

[lxc_container]: http://docs.ansible.com/ansible/lxc_container_module.html
[lilik_container]: https://github.com/LILiK-117bis/lilik_container 
