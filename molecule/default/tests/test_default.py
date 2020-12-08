import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_dotnet(host):
    cmd = host.run("/usr/share/dotnet/dotnet --list-sdks | wc -l")
    # 3 versions of the sdk installed
    assert cmd.stdout == "3\n"
