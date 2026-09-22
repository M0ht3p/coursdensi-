import subprocess

profiles = subprocess.check_output("netsh wlan show profiles", shell=True).decode()
names = [line.split(":")[1].strip() for line in profiles.split("\n") if "All User Profile" in line]

for i, name in enumerate(names, 1):
    print(f"[{i}] {name}")

ch = int(input("\nChoose WiFi number: "))
wifi = names[ch - 1]

result = subprocess.check_output(
    f'netsh wlan show profile "{wifi}" key=clear',
    shell=True
).decode()

password_line = [line for line in result.split("\n") if "Key Content" in line]

if password_line:
    password = password_line[0].split(":")[1].strip()
    print(f"\nPassword: {password}")
else:
    print("\nPassword: No password found or profile is open.")
