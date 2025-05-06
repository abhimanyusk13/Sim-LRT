# Least Response Time Load Balancer Simulation

## Overview

This project implements a **Least Response Time** load balancing algorithm in Python. The algorithm routes requests to the server with the lowest average response time, optimizing for performance. The simulation includes:

- A `Server` class that simulates request processing with configurable response times.
- A `LeastResponseTimeLoadBalancer` class that distributes requests based on the least response time algorithm.
- A visual simulation using Matplotlib to plot response times and request distribution across servers.

The project is designed to demonstrate how the least response time algorithm prioritizes faster servers and adapts to performance differences. It generates a scatter plot to visualize the simulation results.

## Requirements

- Python 3.6 or later
- Required Python libraries:
  - `matplotlib` (for plotting)
  - `numpy` (for numerical operations)

## Installation

1. **Clone or Download the Project**:
   - If using a repository, clone it: `git clone <repository-url>`.
   - Alternatively, download the `least_response_time_simulation.py` file.

2. **Install Dependencies**:
   - Install the required libraries using pip:
     ```bash
     pip install matplotlib numpy
     ```

3. **Verify Setup**:
   - Ensure Python is installed: `python --version`.
   - Confirm libraries are installed: `pip show matplotlib numpy`.

## Usage

1. **Run the Simulation**:
   - Save the `least_response_time_simulation.py` file.
   - Execute the script:
     ```bash
     python least_response_time_simulation.py
     ```

2. **Simulation Details**:
   - The script simulates 50 requests across three servers with base response times of 0.1s, 0.15s, and 0.2s.
   - For each request, it prints:
     - The server selected and the response time.
   - After the simulation, it outputs:
     - Average response times for each server.
     - The number of requests handled by each server.
   - A scatter plot is saved as `load_balancer_simulation.png` in the working directory, showing response times per server over time.

3. **Expected Output**:
   - Console output example:
     ```
     Simulating 50 requests with Least Response Time Load Balancing...
     Request 1 routed to Server1, Response Time: 0.102s
     Request 2 routed to Server1, Response Time: 0.098s
     ...
     Final Server Metrics (Avg Response Time):
     Server1: 0.100s
     Server2: 0.151s
     Server3: 0.199s
     Request Distribution:
     Server1: 40 requests
     Server2: 8 requests
     Server3: 2 requests
     Simulation plot saved as 'load_balancer_simulation.png'
     ```
   - A PNG file (`load_balancer_simulation.png`) with a scatter plot of response times.

## Interpreting Results

- **Console Output**: Shows that faster servers (e.g., Server1 with 0.1s base response time) receive more requests due to the algorithm’s preference for lower response times.
- **Request Distribution**: The final metrics indicate how many requests each server handled, typically with Server1 handling the majority.
- **Scatter Plot**: Visualizes response times for each request, with points clustered by server. Server1 will have the most points and lowest response times, demonstrating the algorithm’s effectiveness.

## Customization

You can modify the simulation to explore different scenarios:

1. **Change Number of Requests**:
   - Edit the `num_requests` parameter in `simulate_load_balancer(num_requests=50)` to simulate more or fewer requests.

2. **Adjust Server Parameters**:
   - Modify the `base_response_time` in the `Server` initialization (e.g., `Server("Server1", base_response_time=0.05)`).
   - Add more servers to the `servers` list in `simulate_load_balancer()`.

3. **Simulate Dynamic Load**:
   - Extend the `Server` class to change `base_response_time` dynamically (e.g., increase it after a threshold to simulate overload).

4. **Enhance Visualization**:
   - Modify the plotting code in `simulate_load_balancer()` to add features like a bar chart for request counts or a line plot for average response times.

5. **Add Features**:
   - Implement health checks to skip unresponsive servers.
   - Add logging to save simulation results to a file.
   - Integrate with a web framework (e.g., Flask) for real HTTP request simulation.

## Project Structure

- `least_response_time_simulation.py`: The main Python script containing the simulation logic and visualization.
- `load_balancer_simulation.png`: The output plot generated after running the simulation (created in the working directory).

## Notes

- The simulation uses a `deque` with a maximum length of 10 to store recent response times, ensuring the algorithm adapts to recent performance.
- The `time.sleep` duration is scaled down (divided by 10) to make the simulation run faster while preserving relative response time differences.
- For production use, consider integrating with real servers, monitoring tools (e.g., Prometheus), or cloud load balancers (e.g., AWS ELB).

## Troubleshooting

- **Missing Libraries**: If you encounter import errors, ensure `matplotlib` and `numpy` are installed (`pip install matplotlib numpy`).
- **No Plot Generated**: Verify that `matplotlib` is correctly installed and that the working directory is writable.
- **Slow Simulation**: Reduce `num_requests` or further scale down `time.sleep` in the `Server.process_request` method.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

## Contact

For questions or suggestions, please open an issue on the repository or contact the maintainer.
