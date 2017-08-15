# ansible-ibm-websphere
Ansible playbooks for IBM WebSphere Application Server, Connections 6 and others

# Getting start

## Prerequisites

1) Download installation files:

* IBM Installation Manager
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
iim_bin_file=agent.installer.linux.gtk.x86_64_1.8.6000.20161118_1611.zip
iim_bin_file_sha256=b253a06bccace5934b108632487182f6a6f659082fea69372242b9865a64e4f3
#
was_repository_url=http://192.168.1.1/was/8.5.5
was_bin_file01=WAS_ND_V8.5.5_1_OF_3.zip
was_bin_file01_sha256=b1333962ba4b25c8632c7e4c82b472350337e99febac8f70ffbd551ca3905e83
was_bin_file02=WAS_ND_V8.5.5_2_OF_3.zip
was_bin_file02_sha256=440b7ed82089d43b1d45c1e908bf0a1951fed98f2542b6d37c8b5e7274c6b1c9
was_bin_file03=WAS_ND_V8.5.5_3_OF_3.zip
was_bin_file03_sha256=b73ae070656bed6399a113c2db9fb0abaf5505b0d41c564bf2a58ce0b1e0dcd2
#
was_fixes_repository_url=http://192.168.1.1/was/8.5.5
was_fixes_bin_file01=8.5.5-WS-WAS-FP011-part1.zip
was_fixes_bin_file01_sha256=bd9b51bd6a8522da8a6a19fcb0cf0ccc9980b13f5da2a1bcd4db2242ae555a66
was_fixes_bin_file02=8.5.5-WS-WAS-FP011-part2.zip
was_fixes_bin_file02_sha256=0ab936b38ebee485471ce9f6fdbf5c0a609f0ffa837247fb81db6935f5cc061c
```

# Authors

* **Enio Basso** - *Initial work* - [My Repository](https://github.com/ebasso)


See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

# License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
