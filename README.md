# ansible-ibm-websphere
Ansible playbooks for IBM WebSphere Application Server, Connections 6 and others

# Playbooks

| Playbook name                 | Status         |           Description                                        |
|-------------------------------|----------------|--------------------------------------------------------------|
| ibm-was-nd-complete.yml       | Complete       | Install IBM HTTP Server - 8.5.5.14  |
| ibm-http-server-complete.yml  | Complete       | Install IBM WebSphere Application Server - Network Deployment - 8.5.5.14  |
| ibm-connections6.yml          | In Development | Install IBM Connections 6   |

# Roles

| Role name                       |            Description of Role                                          |
|---------------------------------|-------------------------------------------------------------------------|
| ibm-http-config-plgwct          | Configure HTTP Plugin |
| ibm-http-server-fix-install     | Install IBM HTTP Server Fixes |
| ibm-http-server-install         | Install IBM HTTP Server |
| installation-manager-install    | Install IBM Installation Manager   |
| was-dmgr-config-jvm             | Tune Java Virtual Machine of DMGR |
| was-dmgr-config-ldap            | Configure LDAP Repository (Server must be started) |
| was-dmgr-config-webserver       | Configure WebServers on DMGR |
| was-dmgr-create-profile         | Create a profile for Deployment Manager |
| was-dmgr-import-tls-cert        | Add TLS Signer Certificate to Cell Default Trust Store (Server must be started)|
| was-dmgr-restart                | Restart Deployment Manager |
| was-dmgr-start                  | Start Deployment Manager |
| was-dmgr-stop                   | Stop Deployment Manager |
| was-java-install                | Install IBM Java for WAS  |
| was-nd-fix-install              | Install IBM WAS ND Fixes  |
| was-nd-install                  | Install IBM WebSphere Application Server - Network Deployment - 8.5.5  |
| was-nodeagent-start             | Start Node Agent |
| was-nodeagent-stop              | Stop Node Agent |
| was-profile-cleanup-logs        | Delete and truncate log files for Application Servers|
| was-profile-cleanup-temps       | Delete temp files on WAS Profile (server must be stopped) |
| was-profile-create              | Create a profile for WAS Servers |
| was-profile-delete-all          | Delete all profiles on WAS Servers |
| was-server-start                | Start Applications Servers |
| was-server-stop                 | Stop Applications Servers |



# Getting start

## Prerequisites

1) Download installation files:

* IBM Installation Manager 1.8.7
* IBM WebSphere Application Server 8.5.5
* IBM WebSphere Application Server 8.5.5 Fix Pack 11

2) Copy files to Web Server

## Configure Ansible hosts file

3) Change you ansible host file like **hosts.example**


## Cloning ansible-ibm-websphere from git

```
cd /etc/ansible

git clone https://github.com/ebasso/ansible-ibm-websphere.git
```

## Running playbooks

```
cd /etc/ansible

ansible-playbooks -i environments/hosts.development -u <username> -k playbooks/ibm-was-nd-complete.yml

```

## Running specific Playbooks

```
cd /etc/ansible

ansible-playbooks -i environments/hosts.development -u <username> -k playbooks/ibm-was-nd/ibm-installation-manager.yml

ansible-playbooks -i environments/hosts.development -u <username> -k playbooks/ibm-was-nd/ibm-was-nd.yml

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
...
was_version="8.5.5009.20160225_0435"
```

# Authors

* **Enio Basso** - *Initial work* - [My Repository](https://github.com/ebasso)


See also the list of [contributors](https://github.com/ebasso/ansible-ibm-websphere/graphs/contributors) who participated in this project.

# License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
