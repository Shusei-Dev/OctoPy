import yaml


def get_yml_content(file_path):
    with open(file_path) as file:
        file_content = yaml.load(file, Loader = yaml.FullLoader)
        return file_content

def write_yml_content(file_path, var):
    with open(file_path, "w") as file:
        yaml.dump(var, file)

def change_yml_content(file_path, t_var, content_var):
    file_content = get_yml_content(file_path)
    file_content[t_var] = content_var
    write_yml_content(file_path, file_content)
