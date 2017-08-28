# ansible-ibm-websphere
Ansible playbooks for IBM WebSphere Application Server, Connections 6 and others

# Getting start

## Prerequisites

1) Download installation files:

* IBM Installation Manager 1.8.7
* IBM WebSphere Application Server 8.5.5
* IBM WebSphere Application Server 8.5.5 Fix Pack 11

2) Copy files to Web Server

## Configure Ansible hosts file

3) Change you ansible host file like

```
[was-servers]
was1.company.com

[was-servers:vars]
iim_repository_url=http://192.168.1.1/installation
#
was_repository_url=http://192.168.1.1/was/8.5.5
#
was_fixes_repository_url=http://192.168.1.1/was/8.5.5
```

## Cloning ansible-ibm-websphere from git

```
cd /etc/ansible

git clone https://github.com/ebasso/ansible-ibm-websphere.git
```

## Running playbooks

```
cd /etc/ansible

ansible-playbooks ansible-ibm-websphere/playbooks/ibm-installation-manager.yml

ansible-playbooks ansible-ibm-websphere/playbooks/ibm-was-nd.yml

```

# For other versions of IIM, WAS and WAS fixes

1) If you are using a different Fix Pack than FP 11, you must change
generate sha256 hashes.

```
Example: sha256sum  WAS_ND_V8.5.5_1_OF_3.zip
```
and set variables:

4) Change you ansible host file like

```
[was-servers]
was1.company.com

[was-servers:vars]
iim_repository_url=http://192.168.1.1/installation
#
was_repository_url=http://192.168.1.1/was/8.5.5
#
was_fixes_repository_url=http://192.168.1.1/was/8.5.5
was_version="8.5.5009.20160225_0435"
```

# Authors

* **Enio Basso** - *Initial work* - [My Repository](https://github.com/ebasso)


See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

# License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
