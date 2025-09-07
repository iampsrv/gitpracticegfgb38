import os

def display_env_variables(env_file='aabc.env'):
    if not os.path.isfile(env_file):
        print(f"File '{env_file}' not found.")
        return
    with open(env_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                if '=' in line:
                    key, value = line.split('=', 1)
                    print(f"{key.strip()} = {value.strip()}")

    
# Example usage:
# display_env_variables()