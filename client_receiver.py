import sys
import queues

output_file = "./output.txt"
queue_name = "MyTestQueue"
queue = queues.get_queue(queue_name)

def main():

    batch_size = 10
    received_lines = []

    print(f"Receiving, handling, and deleting messages in batches of {batch_size}.")
    more_messages = True
    while more_messages:
        received_messages = queues.receive_messages(queue, batch_size, 2)
        print('.', end='')
        sys.stdout.flush()
        for message in received_messages:
            received_lines.append(message.body)
        if received_messages:
            queues.delete_messages(queue, received_messages)
        else:
            more_messages = False
    print('Done.')

    with open(output_file, 'w') as file:
        file.writelines(received_lines)
    print(f"Successfully reassembled all file lines!")

if __name__ == '__main__':
    main()