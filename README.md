# xivap-fsd-server
Multi-player flight server based on FSD protocol for X-Plane XIVAP multi-player plugin

This is a simple multi-player server designed to work with the X-Ivap multi-player plugin for X-Plane 10/11. This software is a partial implimentation of the IVAO FSD protocol, and was designed mostly as a sandbox and a learning tool.

How to use:
run python fsd.py

To stop:
Linux: Ctrl-C
Windows: You may have to kill the program through the taskmanager

What works:
+ Multiple clients can connect
+ Information about the air plane models are correctly exchanged
+ Positional information is correctly exchanged (currently over TCP)

What does not work:
- P2P handshaking is currently not working
- Administration is not implimented yet





