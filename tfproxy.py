#!/usr/bin/env python
import jinja2

TERRAFORM_TEMPLATE_FILE = "terraform.jinja"

template_loader = jinja2.FileSystemLoader(searchpath="./")
template_env = jinja2.Environment(loader=template_loader)
terraform_template = template_env.get_template(TERRAFORM_TEMPLATE_FILE)

AWS_REGION_AMI_MAP = [
    {'name': 'eu-west-1',
     'ami': 'ami-1b791862'},
    {'name': 'eu-west-2',
     'ami': 'ami-941e04f0'},
    {'name': 'eu-west-3',
     'ami': 'ami-c1cf79bc'},
    {'name': 'us-east-2',
     'ami': 'ami-965e6bf3'},
    {'name': 'us-east-1',
     'ami': 'ami-66506c1c'},
    {'name': 'us-west-1',
     'ami': 'ami-07585467'},
    {'name': 'us-west-2',
     'ami': 'ami-79873901'},
    {'name': 'ap-south-1',
     'ami': 'ami-84e3b2eb'},
    {'name': 'ap-northeast-2',
     'ami': 'ami-ab77d4c5'},
    {'name': 'ap-southeast-1',
     'ami': 'ami-b7f388cb'},
    {'name': 'ap-southeast-2',
     'ami': 'ami-33ab5251'},
    {'name': 'ap-northeast-1',
     'ami': 'ami-48630c2e'},
    {'name': 'ca-central-1',
     'ami': 'ami-173db873'},
    {'name': 'eu-central-1',
     'ami': 'ami-5055cd3f'},
    {'name': 'sa-east-1',
     'ami': 'ami-bb9bd7d7'},
]

if __name__ == '__main__':
    terraform_output = terraform_template.render(regions=AWS_REGION_AMI_MAP)
    print(terraform_output)
