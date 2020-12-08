Ansible role for dotnet
==================================

Installs dotnet from official script

[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-dotnet/workflows/Molecule%20Test/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-dotnet/actions?query=workflow%3A%22Molecule+Test%22)
[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-dotnet/workflows/Release/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-dotnet/actions?query=workflow%3A%22Release%22)

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| `dotnet_versions` | Versions of dotnet to install | list | none | yes |

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: ansible-role-dotnet
      vars:
        dotnet_versions:
          - 1.1
          - 2.1
          - 3.0
```

License
-------

[Apache License](LICENSE)
