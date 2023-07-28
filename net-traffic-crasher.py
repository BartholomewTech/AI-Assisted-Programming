import requests
import threading
import socket

def send_http_requests(target_ip):
    url = f"http://{target_ip}:your_server_port"  # Replace 'your_server_port' with your server's port
    while True:
        try:
            response = requests.get(url)
            print("HTTP Status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("HTTP Error:", e)

def send_dns_requests(target_ip):
    domain_name = input("Enter the domain name to resolve: ")
    while True:
        try:
            result = socket.gethostbyname(domain_name)
            print(f"Resolved IP for {domain_name}: {result}")
        except socket.gaierror as e:
            print("DNS Error:", e)

def generate_traffic(target_ip, traffic_type):
    if traffic_type == "--http":
        num_threads = 50  # Adjust the number of threads for desired traffic intensity
        threads = [threading.Thread(target=send_http_requests, args=(target_ip,)) for _ in range(num_threads)]
    elif traffic_type == "--dns":
        num_threads = 50  # Adjust the number of threads for desired traffic intensity
        threads = [threading.Thread(target=send_dns_requests, args=(target_ip,)) for _ in range(num_threads)]
    elif traffic_type == "--all":
        num_http_threads = 30  # Adjust the number of threads for desired HTTP traffic intensity
        num_dns_threads = 20  # Adjust the number of threads for desired DNS traffic intensity
        threads = [threading.Thread(target=send_http_requests, args=(target_ip,)) for _ in range(num_http_threads)]
        threads += [threading.Thread(target=send_dns_requests, args=(target_ip,)) for _ in range(num_dns_threads)]
    else:
        print("Invalid traffic type. Use '--http', '--dns', or '--all'.")
        return

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    traffic_type = input("Enter the type of traffic to generate (--http, --dns, or --all): ")
    generate_traffic(target_ip, traffic_type)
