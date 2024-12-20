import argparse
from credentials import get_elastic_credentials

def main():
    parser = argparse.ArgumentParser(description='Get Elasticsearch credentials from Kubernetes')
    parser.add_argument('--namespace', '-n', required=True, help='Kubernetes namespace')
    args = parser.parse_args()
    
    username, password = get_elastic_credentials(args.namespace)
    
    if username and password:
        print(f"Username: {username}")
        print(f"Password: {password}")

if __name__ == "__main__":
    main()