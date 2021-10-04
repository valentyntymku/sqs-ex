import sys
import queues

input_file = "./input.txt"
queue_name = "MyTestQueue"
queue = queues.get_queue(queue_name)

def pack_message(msg_path, msg_body, msg_line):
    return {
        'body': msg_body,
        'attributes': {
            'path': {'StringValue': msg_path, 'DataType': 'String'},
            'line': {'StringValue': str(msg_line), 'DataType': 'String'}
        }
    }

def main():

    with open(input_file) as file:
        lines = file.readlines()

    line = 0
    batch_size = 10

    print(f"Sending file lines in batches of {batch_size} as messages.")

    while line < len(lines):
        messages = [pack_message(input_file, lines[index], index)
                    for index in range(line, min(line + batch_size, len(lines)))]
        line = line + batch_size
        queues.send_messages(queue, messages)
        print('.', end='')
        sys.stdout.flush()
        
    print(f"Done. Sent {len(lines) - 1} messages.")

if __name__ == '__main__':
    main()