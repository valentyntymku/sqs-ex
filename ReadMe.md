# How to run simple messaging system

## Purpose

The solution is sending and receiving messages from a queue.

## Prerequisites

- You must have an AWS account, and have your default credentials and AWS Region
  configured as described in (https://docs.aws.amazon.com/sdkref/latest/guide/creds-config-files.html).
  The account must have AWS SQS permissions to be able to send and receive messages.
- Python 3.7 or later
- Boto 3 1.11.10 or later

## Running the code

`queues.py` contains functions for working with a queue.
`client_sender.py` is a client for sending messages to a queue.
`client_receiver.py` is a client for receiving messages from a queue.
`input.txt` is a text file with some input text.
`output.txt` is a test file for the output.

### Send messages:

For sending the messages to the queue use this command:
```
python3 -m client_sender.py
``` 

Make sure theese parameters are set properly:
`input_file` - path to the input file
`queue_name` - the name of the exising SQS queue

### Receive messages:

For receiving the messages from the queue use this command:

```
python3 -m client_receiver.py
``` 

Make sure theese parameters are set properly:
`output_file` - path to the output file
`queue_name` - the name of the exising SQS queue

## References

- [Python Code Samples for Amazon SQS](https://docs.aws.amazon.com/code-samples/latest/catalog/code-catalog-python-example_code-sqs.html).

- [Boto 3 Amazon SQS documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html).
