# Packet Communication System

## Overview

The Packet Communication System is a simple simulation of a network packet communication framework. It consists of a sender and a receiver that communicate through packets, each containing data and a sequence number. This project demonstrates how packets can be prepared, sent, received, and acknowledged in a controlled environment.

### Key Features

- **Packet Creation**: Each packet contains source and destination addresses, a sequence number, acknowledgment status, and the data being transmitted.
- **Communicator Classes**: The system consists of `Sender` and `Receiver` classes that manage the sending and receiving of packets.
- **Acknowledgments**: The receiver can send back acknowledgment packets to confirm receipt of the data.

## Installation

To use this project, you need Python installed on your machine. This project does not have any external dependencies, so you can simply clone or download the repository and run it.

### Clone the Repository

```bash
git clone https://github.com/yourusername/packet-communication-system.git
cd packet-communication-system
```

## Usage

You can run the simulation by executing the `main` section of the code in the `__main__` block. This section sets up the addresses and message, then simulates the sending and receiving of packets.

### Example

1. **Set Up Addresses and Message**:
   - Define source and destination addresses.
   - Specify the message to be sent.

2. **Instantiate the Sender and Receiver**:
   - Create instances of the `Sender` and `Receiver` classes with appropriate addresses and packet sizes.

3. **Prepare and Send Packets**:
   - Use the `prepare_packets` method of the `Sender` class to break the message into packets.
   - Call the `send_packets` method to send the packets to the receiver.

4. **Receive and Acknowledge Packets**:
   - The receiver will receive packets and automatically generate acknowledgment packets.

### Sample Code

```python
if __name__ == '__main__':
    source_address = "192.168.1.1"
    destination_address = "192.168.2.2"
    message = "What is up?"

    sender = Sender(source_address, packet_size=4)  # Packet size of 4 characters
    receiver = Receiver(destination_address)

    packets = sender.prepare_packets(message, destination_address)
    sender.send_packets(packets, receiver)

    # Collect the message from received packets
    received_message = receiver.get_message_by_received_packets()
    print(f"Received Message: {received_message}")
```

### Explanation of Classes

- **Packet**: Represents a packet with attributes such as source address, destination address, sequence number, acknowledgment status, and data. 
  - Methods include getters for packet attributes and a string representation.

- **Communicator**: A base class for both sender and receiver, which manages the communicator's address and current sequence number.
  - Contains methods for sending packets and managing sequence numbers.

- **Sender**: Inherits from `Communicator`. Responsible for preparing packets from a message and sending them to the receiver.
  - Contains methods for packet preparation and acknowledgment handling.

- **Receiver**: Also inherits from `Communicator`. Receives packets, stores them, and generates acknowledgment packets.
  - Contains a method to reconstruct the original message from received packets.

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request. Any improvements or bug fixes are welcome!



