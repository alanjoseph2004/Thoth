import socket
import threading
import time

BROADCAST_PORT = 5000  # Port for broadcasting
DISCOVERY_MESSAGE = "DISCOVER:ThothNode"  # Message to announce presence
discovered_peers = set()  # Store discovered peers

def broadcast_presence(port=BROADCAST_PORT):
    """Broadcast the node's presence to the local network."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # Enable broadcast
    message = DISCOVERY_MESSAGE.encode()
    
    while True:
        sock.sendto(message, ('<broadcast>', port))
        print(f"[Broadcast] Presence announced: {message.decode()}")
        time.sleep(2)  # Broadcast every 2 seconds

def listen_for_peers(port=BROADCAST_PORT):
    """Listen for presence broadcasts from other nodes."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', port))  # Bind to all interfaces on the specified port
    
    while True:
        data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
        message = data.decode()
        
        if message.startswith("DISCOVER:"):
            peer_info = f"{addr[0]}:{addr[1]}"
            if peer_info not in discovered_peers:
                discovered_peers.add(peer_info)
                print(f"[Discovery] New peer found: {peer_info}")
            else:
            	continue
                #print(f"[Discovery] Peer already known: {peer_info}")

def start_discovery():
    """Start broadcasting and listening in separate threads."""
    threading.Thread(target=broadcast_presence, daemon=True).start()
    threading.Thread(target=listen_for_peers, daemon=True).start()

if __name__ == "__main__":
    print("Starting peer discovery...")
    start_discovery()

    # Keep the main thread alive
    while True:
        time.sleep(1)

