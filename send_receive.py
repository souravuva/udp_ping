import socket
import threading
import time

UDP_DST_IP = "10.186.1.157"
UDP_DST_PORT = 5005
MAX_PKT_LEN = 1024

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
def rx_thread():
    print("start receive thread")
    while True:
        data, address = sock.recvfrom(MAX_PKT_LEN)
        recv_time = time.time_ns()/1000000
        data_str = data.decode('ascii')
        sent_time = float(data_str.split(",")[1].split(":")[1])
        rtt = recv_time - sent_time
        clientMsg = "Message from Client:{}".format(data_str)
        print(clientMsg + ",client_recv_time:" + str(recv_time)+ ",rtt:" + str(rtt))

if __name__ == '__main__':
    print("UDP target IP: %s" % UDP_DST_IP)
    print("UDP target port: %s" % UDP_DST_PORT)
    thread = threading.Thread(target=rx_thread)
    thread.start()
    for i in range(10):
        tx_time = str(time.time_ns()/1000000)
        msg = "seq_num:%s,client_tx_time:%s" % (str(i), tx_time)
        sock.sendto(msg.encode(), (UDP_DST_IP, UDP_DST_PORT))
        print("Sent " + msg)
        time.sleep(1)
    thread.join()
    print("Program shutting down")

