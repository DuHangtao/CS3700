#!/usr/bin/env python3
import socket
import ssl
import sys
import argparse


# Collecting the completed message from server
def receive(client):
    received_message = ""
    # Keep receiving message until see a "\n"
    while "\n" not in received_message:
        received_message = received_message + str(client.recv(8192).decode())
    return received_message


# Counting the number of times of given symbol appears in the random string
def count(find, client):
    _split = find.split(" ")
    given_symbol = str(_split[2])
    given_string = str(_split[3])
    _count = given_string.count(given_symbol)
    send_count_message = "cs3700fall2019 COUNT " + str(_count) + "\n"
    client.send(send_count_message.encode())
    received_data = receive(client)
    format_check(received_data)
    return received_data


# Connecting the program with the server
def connection(client, port_number, host_name):
    try:
        client.connect((host_name, port_number))
    except OSError as e:
        raise ConnectionError from e


# Sending HELLO message to the server and returning a FIND from server
def hello(client, student_id):
    _hello = "cs3700fall2019 HELLO " + student_id + "\n"
    client.send(_hello.encode())
    received_data = receive(client)
    format_check(received_data)
    return received_data


# check if the received message is a FIND/BYE
# FIND returns True/ BYE returns False
def count_more(received_message):
    if received_message.find("FIND") != -1:
        return True
    else:
        return False


# Checking if the format fot the FIND MESSAGE is correct
# The server may send the bad message which may collapse the program
# The correct format for FIND is "cs3700fall2019 FIND [A single ASCII symbol] [A random string] \n"
def format_check(find):
    split_message = find.split(" ")
    length_of_message = len(split_message)

    if length_of_message < 3:
        print("The message is incomplete")
        exit()

    first_element = split_message[0]
    second_element = split_message[1]
    third_element = split_message[2]

    if length_of_message == 4 or length_of_message == 3:

        is_find_first_correct = (first_element == "cs3700fall2019")
        is_find_second_correct = (second_element == "FIND")
        is_find_third_correct = len(third_element) is 1

        is_bye_first_correct = (first_element == "cs3700fall2019")
        is_bye_second_correct = (second_element == "BYE")

        is_find = is_find_first_correct and is_find_second_correct and is_find_third_correct
        is_bye = is_bye_first_correct and is_bye_second_correct

        if is_find or is_bye:
            return True
        else:
            print("The format for the received message is incorrect")
            exit()


# Reading arguments from command line and contains the logic of the program
def main():
    # Reading useful message from command line and save them and use them later
    arguments_number = len(sys.argv)
    correct_range = range(3, 7)
    argument_list = sys.argv

    # Deleting the first unnecessary element
    del argument_list[0]

    # default port number
    if arguments_number not in correct_range:
        print("Invalid input message, program exit")
        exit()

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", dest="port_number", type=int)
    parser.add_argument("-s", action="store_true", default=False)
    parser.add_argument("host_name")
    parser.add_argument("nu_id")
    arguments = parser.parse_args(argument_list)

    if arguments.port_number:
        port_number = arguments.port_number
    else:
        if arguments.s:
            port_number = 27994
        else:
            port_number = 27993

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        if arguments.s:
            client = ssl.wrap_socket(client, ssl_version=ssl.PROTOCOL_SSLv23)
        # Connecting the client with server
        connection(client, port_number, arguments.host_name)
        # Receiving the first FIND from server
        first_task = hello(client, arguments.nu_id)
        # Sending the Count message to the server for the first FIND
        # At the end, getting the next message which is either a FIND or BYE
        next_task = count(first_task, client)
        # A while loop to communicate with server until client receive BYE
        while True:
            is_find = count_more(next_task)
            if is_find:
                next_task = count(next_task, client)
            else:
                print(next_task)
                break


if __name__ == "__main__":
    main()
