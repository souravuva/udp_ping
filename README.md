# udp_ping
A client server implementation of UDP ping packets

send_receive.py: Is a two threaded python program that generates sequenced UDP packets from localhost (client) to a server. These packets are timestamped when sent out.
udp_reply.py: Runs on the server that receives UDP packets sent out by the above client and reflects it back to the client. The client upon receiving it timestamps the packets on which it was received. In send_receive.py it also computes this time difference to get and estimated RTT. This system uses handcrafted UDP packets and does not rely on ICMP protocol to compute ping.

Usage:

On the client:
root@ip-10-186-1-139:/home/ubuntu# python3 send_receive.py 
UDP target IP: 10.186.1.157
UDP target port: 5005
start receive thread
Sent seq_num:0,client_tx_time:1716223414632.8708
Message from Client:seq_num:0,client_tx_time:1716223414632.8708,client_recv_time:1716223414633.5818,rtt:0.7109375
Sent seq_num:1,client_tx_time:1716223415634.1514
Message from Client:seq_num:1,client_tx_time:1716223415634.1514,client_recv_time:1716223415634.8557,rtt:0.704345703125
Sent seq_num:2,client_tx_time:1716223416635.369
Message from Client:seq_num:2,client_tx_time:1716223416635.369,client_recv_time:1716223416636.1257,rtt:0.7568359375

On the server:
root@ip-10-186-1-157:/home/ubuntu# python3 udp_reply.py 
('10.186.1.139', 53906)
Message from Client:seq_num:0,client_tx_time:1716223414632.8708
('10.186.1.139', 53906)
Message from Client:seq_num:1,client_tx_time:1716223415634.1514
('10.186.1.139', 53906)
Message from Client:seq_num:2,client_tx_time:1716223416635.369

Actual RTT from ping:
root@ip-10-186-1-139:/home/ubuntu# ping 10.186.1.157
PING 10.186.1.157 (10.186.1.157) 56(84) bytes of data.
64 bytes from 10.186.1.157: icmp_seq=1 ttl=64 time=0.469 ms
64 bytes from 10.186.1.157: icmp_seq=2 ttl=64 time=0.488 ms
64 bytes from 10.186.1.157: icmp_seq=3 ttl=64 time=0.562 ms
64 bytes from 10.186.1.157: icmp_seq=4 ttl=64 time=0.444 ms
64 bytes from 10.186.1.157: icmp_seq=5 ttl=64 time=0.485 ms

The extra overhead of UDP packet parsing on the user land and conversion between data types adds some overhead of around 0.25 ms which is negligible for any experiments where RTT can be in 10 ms or more.
