#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader
import click, os, yaml

import logging
logging.basicConfig(level=logging.INFO)
#CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET
logger = logging.getLogger(__name__)


def render_jinja(definitions, template_file_path):
    """
    definitions - dictionary of config definitions for VM preparation
    template_file_path - string path for template jinja2 file
    returns data feeded into Jinja2 template as string
    """
    #Load Jinja2 template
    templates_searchpath = '/'.join(template_file_path.split('/')[:-1])
    template_file_name = template_file_path.split('/')[-1]
    env = Environment(loader = FileSystemLoader(templates_searchpath),
        trim_blocks=True, lstrip_blocks=True)
    template = env.get_template(template_file_name)

    #Render the template with data and print the output
    #print(template.render(definitions))
    logger.info(template.render(definitions))
    return template.render(definitions)

@click.command()
@click.option('-d','--definitions_file_path', default='./group_vars/all/definitions.yml',
    help='file path and name for definitions in Yaml')
#For an option with ('-f', '--foo-bar'), the parameter name is foo_bar.
@click.option('-t','--template_file_path', default='./roles/common/templates/inventory.j2',
    help='file path and name for result file')
@click.option('-i','--inventory_file_path', default='./inventory',
    help='file path and name for result file')
def create_from_j2(definitions_file_path, inventory_file_path, template_file_path):
    """
    all three inputs are strings: relative paths (or absolute if needed) for files:
        definitions_file_path  - file with Yaml variables
        template_file_path - file with jinja definition
        inventory_file_path - result file with created inventory list
        if variables are ok - file is created if not Value error is raised with detailed information
    """
    logger.info('definitions_file_path: '+definitions_file_path)
    logger.info('inventory_file_path: '+inventory_file_path)
    logger.info('inventory_file_path: '+template_file_path)

    with open(definitions_file_path) as definitions_file:
        #definitions = yaml.safe_load_all(definitions_file)
        #for index, data in enumerate(definitions):
        #    logger.info(str(index)+' : '+str(data))
        definitions = next(yaml.safe_load_all(definitions_file))

    logger.info('definitions["source"]: '+definitions['source'])
    logger.info('definitions["nodes"]: '+'-'.join(definitions['nodes']))
    logger.info('definitions["nodes"][0]: '+definitions['nodes'][0])
    logger.info('definitions["source_ip_address"]: '+str(definitions['source_ip_address']))
    logger.info('definitions["first_ip_address"]: '+str(definitions['first_ip_address']))

    if (definitions['source'] == 'source') or ((definitions['source'] == definitions['nodes'][0]) and (
        definitions['source_ip_address'] == definitions['first_ip_address'])):
        #use only only VM in also inventory as in definitions
        with open(inventory_file_path, 'w') as inventory_file:
            inventory_file.write(render_jinja(definitions,template_file_path))
    else:
        logger.error("If source should not be created and then used for cloning"
                    " the name of source has to be the same as the only one node name,"
                    " and ip addresses have to be also same", exc_info=True)
        raise ValueError()

if __name__ == '__main__':
    create_from_j2()
