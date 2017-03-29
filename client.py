#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: SAVITHRU M LOKANATH
# Contact: SAVITHRU AT JUNIPER.NET
# Copyright (c) 2017 Juniper Networks, Inc. All rights reserved.


import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='10.84.18.1'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
