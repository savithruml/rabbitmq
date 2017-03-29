#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: SAVITHRU M LOKANATH
# Contact: SAVITHRU AT JUNIPER.NET
# Copyright (c) 2017 Juniper Networks, Inc. All rights reserved.


import pika
import argparse

def connect(host, queue, message):

        connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        channel = connection.channel()

        channel.queue_declare(queue=queue)
        channel.basic_publish(exchange='', routing_key=queue, body=message)
        print 'Message: {0} successfully sent to queue: {1}'.format(message, queue)

        connection.close()

def main():

        """ FUNCTION INIT """

        parser = argparse.ArgumentParser(add_help=True)

        parser.add_argument("-s", action="store",
                            help="Specify rabbit-server name")
        parser.add_argument("-q", action="store",
                            help="Specify a name for the queue")
        parser.add_argument("-m", action="store",
                            help="Specify the message to be sent")

        args = parser.parse_args()

        if args.s:
		rabbit_server = args.s

        if args.q:
                queue = args.q

        if args.m:
                message = args.m
	print rabbit_server, queue, message
#	try:
	connect(rabbit_server, queue, message)
#	except:
#		print 'Please specify arguments'

if __name__=='__main__':

	main()
