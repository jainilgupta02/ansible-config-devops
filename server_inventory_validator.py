import yaml

def validate_inventory(path="inventory.yml"):
    with open(path) as f:
        inventory = yaml.safe_load(f)

    print("🔎 Validating Ansible inventory...\n")

    for group, hosts in inventory.items():
        print(f"[{group}]")
        for host in hosts:
            print(f"- {host}")
        print()

if __name__ == "__main__":
    validate_inventory()
