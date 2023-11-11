# Mininet_Computer_Networks
  In the assignment we have 2 parts the description is as following:-
**Part 1: Routing in Mininet**

First we need to install mininet

To install Mininet, you can use the following command:

sudo pip3 install mininet
This will install Mininet and its dependencies.

If you are using Ubuntu 16.04 or higher, you can also install Mininet using the following command:

sudo apt-get install mininet

To install Open vSwitch on Ubuntu, you can use the following command:

sudo apt-get install openvswitch-switch


This will install the Open vSwitch switch daemon and the necessary dependencies.

## Documentation

For more information on Open vSwitch, please see the following documentation:

* [Open vSwitch website](https://openvswitch.org/)
* [Open vSwitch documentation](https://openvswitch.org/documentation/)
* [Open vSwitch FAQ](https://openvswitch.org/faq)

Go to the directory where your Python file is saved.
Make the file executable by running the following command:
chmod +x pythonfilename.py
Run the file with superuser privileges by running the following command:
sudo ./pythonfilename.py
This will open the Mininet CLI, where you can run your Python file.

**Part 2: Evaluating Congestion Control Schemes**

Write a custom TCP client-server program in Mininet.
Use the program to evaluate different congestion control schemes, such as Vegas, Reno, Cubic, and BBR.
Measure throughput under different conditions, such as varying loss parameters and multiple hosts.
Analyze the results to determine the best congestion control scheme for each condition.
