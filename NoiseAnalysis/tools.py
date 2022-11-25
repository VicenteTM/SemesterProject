import os.path as op
import yaml

config_file = op.join(op.dirname(op.dirname(__file__)),'config.yaml')

def read_yaml_file(config_file:str)->dict:
    with open(config_file, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            raise Exception("Can't read config file") from exc

def extend_yaml_file(new_data:dict, yaml_file:str)->None:
    if op.isfile(yaml_file):
        yaml_file_dict = read_yaml_file(yaml_file)
        yaml_file_dict.update(new_data)
    else:
        yaml_file_dict = new_data
    with open(yaml_file,'w') as stream:
        yaml.safe_dump(yaml_file_dict, stream, sort_keys=False)