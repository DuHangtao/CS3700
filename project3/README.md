### Project 3 README
#### Hangtao Du & Zongru Wang & Jinhui Hong

## High Level Approach
The goal of this project was to implement a transport protocol that provides reliable datagram service. The program consists of a sender and receiver module.

The sender will track its congestion window, sequence number, RTT. The sender is responsible for estimating RTT using time samples from requests. The sender is also primarily responsible for the initial handshake to establish the connection between sender and receiver. We've established these methods within the class.

The sender will first call handshake to get the estimate RTT, if we can make connection, it will record the RTT for future use. Then it will call send_packet to send packets to receiver. When the size larger than the max packet size, it will call congestion control to congest the packet and assign them will sequence number. Once complete, it will send to receiver side, and read from receiver's response (ACKs) to determine if a packet been sent successfully or not. If yes, then it will remove it from the packet_queue list, if till the end, there still packet left inside, send will retransmit for the dropped packets
If the packet been received (ACK) send will send next packet again.

We use estimate RTT (RTT will change during the sending and receiving process to get the best performance), and slow start, but we use 10 instead of 1 to get a better performance.

The receiver is initialized to listen for inbound connection and will decode the message to verify that the data arrived uncorrupted. Once this is done it will respond appropriately for ACK handshake, an EOF.

## Challenges Faced
The challenge we faced it the make sure the advanced tests can past every time instead of most time, and rewrite the code in whole to make sure we can pass the performance tests every time. The hardest part is the testing, especially when you can past all tests most of time, but sometimes you can't. It takes a lot of time for us to fix our code.

## Testing
For testing, we first use the script to provided to run simple message and see the log, then we make sure the code are good in big picture, then we run all test to check which test we can't pass, if so, we set up the internet parameters to run individual test and modify our code. Also, inline printing and log is also used for debugging.