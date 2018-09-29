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

Separate your own file of test environment variables `group_vars/test-env-all.yml` change them for new project and create whole environment with working directory testing environment with command:

```bash
ansible-playbook -i {{ path to docker-icinga files }}/inventory create-update-config.yml --extra-vars "@{{ path to docker-icinga files }}//group_vars/test-env-all.yml"
```
