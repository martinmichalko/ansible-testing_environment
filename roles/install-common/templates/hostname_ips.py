#!/usr/bin/env python
import json
import click
import os

working_dir='hosts/'

@click.command()
@click.option('-i', '--input_dir', required=True, type=str, help='directory with the input files to process relative path!!!')
def generate_hosts_file(input_dir):

    os.chdir(os.path.dirname(__file__))
    working_dir=os.getcwd()

    outputfile=(working_dir+'/'+input_dir+"/hosts.txt")

    with open(input_dir+'hostname_ips.json') as json_data:
        ip_list = json.load(json_data)

    with open(input_dir+'hostnames.json') as json_data:
        host_list = json.load(json_data)

    host_dict=(dict(zip(host_list, ip_list)))

    output_text=""
    for host, ip_address in host_dict.items():
        short_name=host.split('.')[0]
        output_text=output_text+("{}  {}  {}\n".format(ip_address,host,short_name))

    print(output_text)
#with open(outputfile, 'w') as out:
#    out.write(output_text)


if __name__ == '__main__':
    generate_hosts_file()
