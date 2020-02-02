import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_terraform_installation(host):
    for item in ['0.13.2', '0.13.1', '0.13.0']:
        c = host.run('terraform-{version} -version'.format(version=item))
        assert c.succeeded
        assert item in c.stdout
