class Packet:
    def __init__(self, source_address, destination_address, sequence_number, is_ack=False, data=None):
        # Initialize packet attributes
        self.source_address = source_address
        self.destination_address = destination_address
        self.sequence_number = sequence_number
        self.is_ack = is_ack
        self.data = data

    def __repr__(self):
        # String representation of a packet
        return f"""Packet(src={self.source_address},
                dst={self.destination_address},
                seq={self.sequence_number},
                ack={self.is_ack},
                data={self.data})"""

    # Getter methods for packet attributes
    def get_source_address(self):
        return self.source_address

    def get_destination_address(self):
        return self.destination_address

    def get_sequence_number(self):
        return self.sequence_number

    def set_sequence_number(self, seq_num):
        # Setter method for sequence number
        self.sequence_number = seq_num

    def get_is_ack(self):
        return self.is_ack

    def get_data(self):
        return self.data


class Communicator:
    def __init__(self, address):
        # Initialize communicator with an address
        self.address = address
        self.current_sequence_number = None

    # Getter method for communicator's address
    def get_address(self):
        return self.address

    # Getter and setter methods for current sequence number
    def get_current_sequence_number(self):
        return self.current_sequence_number

    def set_current_sequence_number(self, seq_num):
        self.current_sequence_number = seq_num

    @staticmethod
    def send_packet(packet_to_send):
        # Static method to simulate sending a packet
        seq_num = packet_to_send.get_sequence_number()
        print(f"Sender: Packet Seq Num: {seq_num} was sent")
        return packet_to_send

    def increment_current_seq_num(self):
        # Increment current sequence number
        if self.current_sequence_number is not None:
            self.current_sequence_number += 1


class Sender(Communicator):
    def __init__(self, address, packet_size):
        # Initialize sender with an address and packet size
        self.num_letters_in_packet = packet_size
        super().__init__(address)

    def prepare_packets(self, message, destination_address):
        # Prepare packets from a message to be sent to a destination address
        packets_arr = []
        jumps = self.num_letters_in_packet
        sequence_number = 0
        for i in range(0, len(message), jumps):
            end = min(i + self.num_letters_in_packet, len(message))
            data = message[i:end]
            current_packet = Packet(self.address, destination_address, sequence_number, False, data)
            packets_arr.append(current_packet)
            sequence_number += 1
        return packets_arr

    def send_packets(self, packets, receiver):
        # Send packets to a receiver
        for packet in packets:
            packet = self.send_packet(packet)
            receiver.receive_packet(packet)
            self.increment_current_seq_num()

    def receive_ack(self, acknowledgment_packet):
        # Receive acknowledgment packet
        return acknowledgment_packet.is_ack


class Receiver(Communicator):
    def __init__(self, address):
        # Initialize receiver with an address
        super().__init__(address)
        self.__received_packets = []

    def receive_packet(self, packet):
        # Receive a packet
        seq_num = packet.get_sequence_number()
        print(f"Receiver: Received packet seq num: {seq_num}")

        self.__received_packets.append(packet)
        # Generate acknowledgment packet
        ack_packet = Packet(packet.get_destination_address(), packet.get_source_address(), packet.get_sequence_number(), True, "ACK")

        return ack_packet

    def get_message_by_received_packets(self):
        # Get the message from received packets
        data = ""
        for packet in self.__received_packets:
            data += packet.get_data()
        return data


if __name__ == '__main__':
    # Test the functionality
    source_address = "192.168.1.1"
    destination_address = "192.168.2.2"
    message = "What is up?"
    
