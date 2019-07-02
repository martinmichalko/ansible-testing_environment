## Create testing virtual environment

### Basics

tool to create set of testing virtual machines based on ansible playbooks  in KVM virtualization for debian 9.

used:
* kvm - for virtualization
* library libvirt - for creation of vm's from prepared images
* openvirtual switch - for networking

### Features

* Fully automated installation procedure based on commands `virt-install` and `preseed.cfg` file
* Authentication based on SSH public key and not on a password.
* vm's creation starts with master preparation all other vm's are cloned to save the time

### Prerequisites

system packages requirements:
openvswitch-switch curl libvirt-bin virtinst qemu-utils


### Usage
in the project directory - change values for variables in group_vars and as root fire command:
```bash
ansible-playbook -i inventory create-update-config.yml
```

Separate your own file of test environment variables `group_vars/all/test-env-definitions.yml` change them for new project and create whole environment with working directory in the project testing environment as root with command:

```bash
ansible-playbook -i {{path_to_your_new_project_dir}}/inventory {{path_to_your_ansible_test_env_project_dir}}/create-update-config.yml --extra-vars "@{{path_to_your_new_project_dir}}/group_vars/all/test-env-definitions.yml" --extra-vars "ansible_python_interpreter=/usr/bin/python"
```
