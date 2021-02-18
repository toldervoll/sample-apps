#!/usr/bin/env python3

# Copyright Verizon Media. Licensed under the terms of the Apache 2.0 license. See LICENSE in the project root.

import json
import sys

fbenchfile = open("fbench-queries", "w")

def print_fbench_line(question):
  request_body = {
    'type': 'any',
    'hits': 10,
    'query': question,
    'retriever': retriever_model
  }
  url = '/search/'
  fbenchfile.write('{}\n{}\n'.format(url, json.dumps(request_body)))  

def process_entry(q):
  question = q['question']
  print(question)
  print_fbench_line(question)

input_file = sys.argv[1]
retriever_model = sys.argv[2]

with open(input_file) as f:
  for line in f:
    entry = json.loads(line)
    process_entry(entry)

fbenchfile.close()
