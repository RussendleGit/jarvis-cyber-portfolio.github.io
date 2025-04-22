allow_list: str = "allow_list.txt"
remove_list: str = "remove_list.txt"

with open(allow_list, 'r') as allow_file:
        whitelist = allow_file.read().split()

with open(remove_list, 'r') as remove_file:
        blacklist = remove_file.read().split()

whitelist = [ip for ip in whitelist if ip not in blacklist]
with open("allow_list.txt", 'w') as file:
        file.write("\n".join(whitelist))

allow_file.close()
remove_file.close()

