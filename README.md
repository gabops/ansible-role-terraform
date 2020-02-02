gabops.terraform
================

![Molecule CI](https://github.com/gabops/ansible-role-terraform/workflows/Molecule%20CI/badge.svg?branch=master)

Installs Hashicorp Terraform.

Requirements
------------

None.

Role Variables
--------------

| Variable | Default value | Description |
| :--- | :--- | :--- |
| terraform_version | 0.13.2 | Defines the version of Terraform to be installed. |
| terraform_verify_checksum | true | Controls if the role should verify the sha256 sum of the downloaded Terraform package. |
| terraform_installation_path | /usr/local/bin | Defines the path where the Terraform binary will be installed. |
| terraform_force_download | false | Controls if the role should overwrite a package (Terraform's zip file) that has been already downloaded in a previous run. |
| terraform_bin_name | terraform | Defines the name of the executable. Useful if you want to install several versions and want to customize the name by appending the version or something similar. See `Example Playbook` |
| terraform_bin_mode | 0755 | Defines the permissions that will be set to the executable. |
| terraform_bin_owner | root | Defines the owner that will be set to the executable. |
| terraform_bin_group | root | Defines the group that will be set to the executable. |

Dependencies
------------

None.

Example Playbook
----------------

### Simple installation:
```yaml
- hosts: servers
  tasks:
    - name: Install Terraform
      import_role:
        name: gabops.terraform
      vars:
        terraform_version: 0.12.18
```
### Multiple installations:
```yaml
- hosts: servers
  tasks:
    - name: Install several versions of Terraform
      include_role:
        name: gabops.terraform
      vars:
        terraform_version: "{{ item }}"
        terraform_bin_name: "terraform-{{ item }}"
      loop:
        - '0.13.2'
        - '0.13.1'
        - '0.13.0'
```

License
-------

[MIT]((./LICENSE))

Author Information
------------------

Gabriel Suarez ([Gabops](https://github.com/gabops))
