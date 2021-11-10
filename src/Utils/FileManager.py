import yaml

class FileManager:

    def get_yml_content(self, file_path):
        with open(file_path) as file:
            file_content = yaml.load(file, Loader = yaml.FullLoader)
            return file_content
