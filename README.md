# Packet Communication System

This Python project implements a simple packet communication system where a sender sends packets containing a message to a receiver. The communication is simulated using classes and objects.

## Features

- **Packet Class**: Represents a packet containing source and destination addresses, sequence number, acknowledgment status, and data.
- **Communicator Class**: Represents a generic communicator with methods for setting and getting the current sequence number.
- **Sender Class**: Extends Communicator class, represents a sender that prepares and sends packets to a receiver.
- **Receiver Class**: Extends Communicator class, represents a receiver that receives packets from a sender and acknowledges them.
- **README File**: Provides information about the project and its usage.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/packet-communication.git
    ```

2. Navigate to the project directory:

    ```bash
    cd packet-communication
    ```

3. Run the Python script:

    ```bash
    python packet_communication.py
    ```

## Requirements

- Python 3.x

## Contributing

Contributions are welcome! If you have any suggestions, bug fixes, or improvements, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
