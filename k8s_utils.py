from kubernetes import client, config

def get_k8s_client():
    """
    Kubernetes clientを初期化して返す
    """
    config.load_kube_config()
    return client.CoreV1Api()

def get_secret(name, namespace, api_client):
    """
    指定された名前空間からシークレットを取得
    """
    try:
        return api_client.read_namespaced_secret(name, namespace)
    except client.exceptions.ApiException as e:
        if e.status == 404:
            print(f"Error: Secret '{name}' not found in namespace '{namespace}'")
        else:
            print(f"Error accessing Kubernetes API: {e}")
        return None