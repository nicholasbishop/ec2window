#!/usr/bin/env python3

import argparse
import logging

import boto3
import ec2window

LOG = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('instance_id')
    return parser.parse_args()


def get_instance(instance_id):
    ec2_resource = boto3.resource('ec2')
    instances = ec2_resource.instances.filter(InstanceIds=[instance_id])
    return list(instances)[0]


def main():
    logging.basicConfig(level=logging.INFO)

    args = parse_args()

    instance = get_instance(args.instance_id)

    with ec2window.run_ec2_instance(instance):
        LOG.info('hello world!')


if __name__ == '__main__':
    main()
