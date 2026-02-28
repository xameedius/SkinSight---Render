import tempfile
from gradio_client import Client, handle_file


SPACE_ID = "xameedius/skinsight-space"

_client = None

def _get_client():
    global _client
    if _client is None:
        _client = Client(SPACE_ID)
    return _client

def predict_upload(django_uploaded_file):
    """
    Calls the Hugging Face Space.
    Expected return: list of dicts like [{"label": "...", "score": 0.9}, ...]
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        for chunk in django_uploaded_file.chunks():
            tmp.write(chunk)
        tmp_path = tmp.name

    client = _get_client()
    return client.predict(handle_file(tmp_path))