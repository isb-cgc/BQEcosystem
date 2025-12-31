"""
Copyright 2025, Institute for Systems Biology

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""
import yaml
import io
import os
import sys


#
# WJRL As of 12/31/25, there are some entries where the key does not match the term. If one
# parses the e.g. pathology_detail.yaml file, this info can be pulled out automatically.
# TODO for future work!
#
CUSTOM_REPAIR_MAP = {
    'extraocular_nodule_size': 'size_extraocular_nodule',
    'extracapsular_extension_present': None,
    'extrascleral_extension_present': 'extrascleral_extension',
    'spindle_cell_percent_range': 'spindle_cell_percent',
    'epithelioid_cell_percent_range': 'epithelioid_cell_percent'
}

'''
----------------------------------------------------------------------------------------------
The yaml reader.
'''
def load_the_yaml(yaml_stream):
    yaml_dict = None
    config_stream = io.StringIO(yaml_stream)
    try:
        yaml_dict = yaml.load(config_stream, Loader=yaml.FullLoader)
    except yaml.YAMLError as ex:
        print(ex)

    return yaml_dict

'''
----------------------------------------------------------------------------------------------
Main Control Flow
'''
def main(args):

    if len(args) != 4:
        print(" ")
        print(" Usage : {} <gdcdictionary_root> <missing_terms_log> <output_file>".format(args[0]))
        return

    gdc_dict_repo = args[1]
    missing_terms_log = args[2]
    output_file = args[3]

    fpath = os.path.join(gdc_dict_repo, 'src/gdcdictionary/schemas/_terms.yaml')

    with open(fpath, mode='r') as yaml_file:
        terms_dict = load_the_yaml(yaml_file.read())

    result_set = set()
    with open(missing_terms_log, mode='r') as file:
        for line in file:
            term = line.rstrip()
            term_chunk = term.split("__")[-1]
            term_chunk = CUSTOM_REPAIR_MAP[term_chunk] if term_chunk in CUSTOM_REPAIR_MAP else term_chunk
            if term_chunk is None:
                print("****************MISSING DEFINITION:", term)
            elif term_chunk in terms_dict:
                desc = terms_dict[term_chunk]['common']['description']
                result_set.add(f'  "{term}": "{desc}",\n')
            else:
                print("****************MISSING TERM:", term_chunk)

    with open(output_file, mode='w') as results:
        for line in sorted(result_set):
            results.write(line)

if __name__ == "__main__":
    main(sys.argv)

