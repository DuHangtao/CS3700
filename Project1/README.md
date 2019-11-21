#Project1

##High-level approach
When I first see the problem, I tried to find out what basically the program 
can do. Then, I found out the program is able to do several things. Firstly,
the program should be able to read arguments from command line, which contains
the important information like TCP port number, name of the server, and student
ID that are useful for program to connected with the server later. Next, the program
will need to connect with the server via a tool called socket which can connect
two nodes on a network to communicate with each other. Once the connection is succeed
the program is able to talk to the server, so we want program send out a HELLO message in
a certain format, and waiting for the reply from the server. The first message from the server
will be a FIND which asks program to count the occurrence number of a symbol in a 
given string. After that, the program should send back a COUNT message, and server will
send another FIND if the program counted right. Server will send several FIND tasks to
program. After program finished all the tasks, server will send back a BYE message with 
a secret code which is different from each student.
##Challenges 
1. When is the complete information collected<br/>
It took me a while to figure out when is the complete information collected form
the server. I use a while loop to accumulate the message from the server until it sees
a "\n" which means the end of the message. It is because client can only receive
a certain size of message at one time.

2. How to read and check the arguments from command line<br/>
There are several useful methods in argparse library which help me to match the correct useful
information from the command line arguments.

##Overview of testing code
I will check if client will receive the first FIND message from server after the client 
sending out a HELLO.After that, I would see if program count right number every time 
until receiving the BYE message with a secret code.
