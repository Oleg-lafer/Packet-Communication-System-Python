class Packet:
    def __init__(self, source_address, destination_address, sequence_number, is_ack=False, data=None):
        self.source_address = source_address
        self.destination_address = destination_address
        self.sequence_number = sequence_number
        self.is_ack = is_ack
        self.data = data

    def __repr__(self):
        return f"""Packet(src={self.source_address},
                dst={self.destination_address},
                seq={self.sequence_number},
                ack={self.is_ack},
                data={self.data})"""

    def get_source_address(self):
        return self.source_address

    def get_destination_address(self):
        return self.destination_address

    def get_sequence_number(self):
        return self.sequence_number

    def set_sequence_number(self, seq_num):
        self.sequence_number = seq_num

    def get_is_ack(self):
        return self.is_ack

    def get_data(self):
        return self.data


class Communicator:
    def __init__(self, address):
        self.address = address
        self.current_sequence_number = None

    def get_address(self):
        return self.address

    def get_current_sequence_number(self):
        return self.current_sequence_number

    def set_current_sequence_number(self, seq_num):
        self.current_sequence_number = seq_num

    @staticmethod
    def send_packet(packet_to_send):
        seq_num = packet_to_send.get_sequence_number()
        print(f"Sender: Packet Seq Num: {seq_num} was sent")
        return packet_to_send

    def increment_current_seq_num(self):
        if self.current_sequence_number is not None:
            self.current_sequence_number += 1


class Sender(Communicator):
    def __init__(self, address, packet_size):
        self.num_letters_in_packet = packet_size
        super().__init__(address)

    def prepare_packets(self, message, destination_address):
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
        for packet in packets:
            packet = self.send_packet(packet)
            receiver.receive_packet(packet)
            self.increment_current_seq_num()

    def receive_ack(self, acknowledgment_packet):
        return acknowledgment_packet.is_ack


class Receiver(Communicator):
    def __init__(self, address):
        super().__init__(address)
        self.__received_packets = []

    def receive_packet(self, packet):
        seq_num = packet.get_sequence_number()
        print(f"Receiver: Received packet seq num: {seq_num}")

        self.__received_packets.append(packet)
        ack_packet = Packet(packet.get_destination_address(), packet.get_source_address(), packet.get_sequence_number(), True, "ACK")

        return ack_packet

    def get_message_by_received_packets(self):
        data = ""
        for packet in self.__received_packets:
            data += packet.get_data()
        return data


if __name__ == '__main__':
    source_address = "192.168.1.1"
    destination_address = "192.168.2.2"
    message = "What is up?"
    num_letters_in_packet = 3

    sender = Sender(source_address, num_letters_in_packet)
    receiver = Receiver(destination_address)

    packets = sender.prepare_packets(message, receiver.get_address())

    # setting current packet
    start_interval_index = packets[0].get_sequence_number()
    # setting current packet in the sender and receiver
    sender.set_current_sequence_number(start_interval_index)
    receiver.set_current_sequence_number(start_interval_index)

    sender.send_packets(packets, receiver)

    full_message = receiver.get_message_by_received_packets()
    print(f"Receiver message: {full_message}")
