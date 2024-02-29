def read_properties_file(file_path):
    config_data = {}
    with open(file_path, "r") as config_file:
        for line in config_file:
            line = line.strip()  
            if not line or line.startswith("#"):  
                continue
            key, value = line.split("=", 1)
            config_data[key.strip()] = value.strip()
    return config_data
