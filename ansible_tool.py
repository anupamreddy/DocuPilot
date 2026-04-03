import os
import tempfile
import yaml
import ansible_runner

def run_ansible_playbook_with_password(hosts: list, playbook_data: list, password: str) -> str:
    """This tool can access any host using ansible script and password provided to ssh.. this creates inventory file from hosts list in the format: [1.1.1.1, 2.2.2.2, ..] and playbook.yml file from playbook_data list."""
    if not password:
        print("Password not provided. Skipping execution.")
        return

    tmp_dir = tempfile.mkdtemp()
    playbook_path = os.path.join(tmp_dir, "playbook.yml")
    inventory_path = os.path.join(tmp_dir, "inventory.ini")
    env_dir = os.path.join(tmp_dir, "env")

    try:
        # Write the playbook to a temporary file
        with open(playbook_path, "w") as f:
            yaml.dump(playbook_data, f)

        # Write the inventory
        with open(inventory_path, "w") as f:
            f.write("[all]\n")
            for host in hosts:
                f.write(f"{host} ansible_ssh_pass={password} ansible_user=root ansible_port=2222 ansible_ssh_common_args='-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null'\n")

        # Prepare environment directory with passwords
        os.makedirs(env_dir)
        with open(os.path.join(env_dir, "envvars"), "w") as f:
            f.write("ANSIBLE_HOST_KEY_CHECKING=False\n")

        result = ansible_runner.run(
            private_data_dir=tmp_dir,
            inventory=inventory_path,
            playbook=playbook_path,
            extravars={"ansible_ssh_pass": password},
            quiet=False
        )

        print("Ansible run status:", result.status)
        print("Ansible return code:", result.rc)

        if result.rc != 0:
            print("Ansible execution failed.")
        else:
            print("Ansible execution succeeded.")
        output = result.stdout.read()

    finally:
        # Clean up temp files and directories
        for root, dirs, files in os.walk(tmp_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(tmp_dir)
    
    return output
