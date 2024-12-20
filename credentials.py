import base64
from k8s_utils import get_k8s_client, get_secret

def get_elastic_credentials(namespace):
    """
    指定された名前空間からElasticsearchの認証情報を取得
    """
    client = get_k8s_client()
    secret = get_secret('elasticsearch-master-credentials', namespace, client)
    
    if not secret:
        return None, None
        
    try:
        username = base64.b64decode(secret.data['username']).decode('utf-8')
        password = base64.b64decode(secret.data['password']).decode('utf-8')
        return username, password
        
    except KeyError as e:
        print(f"Error: Missing key in secret: {e}")
        return None, None
    except Exception as e:
        print(f"Error decoding credentials: {e}")
        return None, None