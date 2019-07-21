#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader

import os, yaml, logging
logging.basicConfig(level=logging.INFO)
#CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET
logger = logging.getLogger(__name__)


def render_jinja(definitions):
    """
    definitions - dictionary of config definitions for VM preparetion
    prints data feeded into Jinja2 template
    """
    #Load Jinja2 template
    env = Environment(loader = FileSystemLoader('./roles/common/templates'),
        trim_blocks=True, lstrip_blocks=True)
    template = env.get_template('inventory.j2')

    #Render the template with data and print the output
    print(template.render(definitions))
    return template.render(definitions)

path = os.path.dirname(__file__)
logger.info(path)

definitions_file_path = os.path.dirname(__file__)+'/group_vars/all/definitions.yml'
inventory_file_path = os.path.dirname(__file__)+'/inventory'

with open(definitions_file_path) as definitions_file:
    #definitions = yaml.safe_load_all(definitions_file)
    #for index, data in enumerate(definitions):
    #    logger.info(str(index)+' : '+str(data))
    definitions = next(yaml.safe_load_all(definitions_file))

if (definitions['source'] == 'source') or ((definitions['nodes'] == definitions['source']) and (
    definitions['source_ip_address'] == definitions['first_ip_address'])):
    #use only only VM in also inventory as in definitions
    with open(inventory_file_path, 'w') as inventory_file:
        inventory_file.write(render_jinja(definitions))
else:
    logger.error("If source should not be created used for cloning"
                " the name of source has to be the same as the only one node name,"
                " and ip addresses have to be also same", exc_info=True)
    raise ValueError()
