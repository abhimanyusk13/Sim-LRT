import random
import time
from collections import deque
from typing import List, Dict
import matplotlib.pyplot as plt
import numpy as np

class Server:
    def __init__(self, server_id: str, base_response_time: float = 0.1):
        self.server_id = server_id
        self.base_response_time = base_response_time
        self.response_times = deque(maxlen=10)  # Store last 10 response times

    def process_request(self) -> float:
        # Simulate processing time with some randomness
        response_time = self.base_response_time + random.uniform(-0.05, 0.05)
        time.sleep(response_time / 10)  # Reduced sleep for faster simulation
        self.response_times.append(response_time)
        return response_time

    def get_avg_response_time(self) -> float:
        # Return average response time or high default if no data
        return sum(self.response_times) / len(self.response_times) if self.response_times else float('inf')

class LeastResponseTimeLoadBalancer:
    def __init__(self, servers: List[Server]):
        self.servers = servers
        self.server_metrics: Dict[str, float] = {server.server_id: float('inf') for server in servers}
        self.request_history = {server.server_id: [] for server in servers}  # Track response times per server
        self.request_counts = {server.server_id: 0 for server in servers}  # Track request counts

    def select_server(self) -> Server:
        # Select server with the lowest average response time
        min_response_time = float('inf')
        selected_server = None

        for server in self.servers:
            avg_response_time = server.get_avg_response_time()
            self.server_metrics[server.server_id] = avg_response_time
            if avg_response_time < min_response_time:
                min_response_time = avg_response_time
                selected_server = server

        # If no server has valid metrics, pick randomly
        if selected_server is None:
            selected_server = random.choice(self.servers)

        return selected_server

    def handle_request(self, request_id: int):
        # Handle a single request
        server = self.select_server()
        response_time = server.process_request()
        self.request_history[server.server_id].append((request_id, response_time))
        self.request_counts[server.server_id] += 1
        return server.server_id, response_time

def simulate_load_balancer(num_requests: int = 50):
    # Initialize servers with different base response times
    servers = [
        Server("Server1", base_response_time=0.1),
        Server("Server2", base_response_time=0.15),
        Server("Server3", base_response_time=0.2)
    ]

    # Create load balancer
    load_balancer = LeastResponseTimeLoadBalancer(servers)

    # Simulate requests
    print(f"Simulating {num_requests} requests with Least Response Time Load Balancing...")
    for i in range(num_requests):
        server_id, response_time = load_balancer.handle_request(i)
        print(f"Request {i+1} routed to {server_id}, Response Time: {response_time:.3f}s")

    # Print final metrics
    print("\nFinal Server Metrics (Avg Response Time):")
    for server_id, avg_time in load_balancer.server_metrics.items():
        print(f"{server_id}: {avg_time:.3f}s" if avg_time != float('inf') else f"{server_id}: No data")
    print("\nRequest Distribution:")
    for server_id, count in load_balancer.request_counts.items():
        print(f"{server_id}: {count} requests")

    # Plot results
    plt.figure(figsize=(12, 6))

    # Plot response times
    for server_id in load_balancer.request_history:
        if load_balancer.request_history[server_id]:
            requests, times = zip(*load_balancer.request_history[server_id])
            plt.scatter(requests, times, label=f"{server_id} Response Times", alpha=0.6)

    plt.title("Least Response Time Load Balancer Simulation")
    plt.xlabel("Request ID")
    plt.ylabel("Response Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.savefig("load_balancer_simulation.png")
    print("\nSimulation plot saved as 'load_balancer_simulation.png'")

if __name__ == "__main__":
    simulate_load_balancer(num_requests=50)
