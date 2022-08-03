import time
import oci
import json
from config import *

def main():
    if auth_method == "resource_principal":
        rps = oci.auth.signers.get_resource_principals_signer()
        object_storage_client = oci.object_storage.ObjectStorageClient(config={}, signer=rps)
    elif auth_method == "api_key":
        config = oci.config.from_file(config_file_path, config_profile)
        object_storage_client = oci.object_storage.ObjectStorageClient(config=config, retry_strategy=retry_strategy)
    else:
        print("Assign a value to auth_method in config.py: \"resource_princpal\" or \"api_key\".")

    # API call
    res=object_storage_client.list_objects(
        namespace_name=object_location_namespace_name,
        bucket_name=object_location_bucket_name,
        prefix=object_location_prefix,
        start=None,
        end=None,
        limit=None,
        delimiter=None,
        fields=None,
        opc_client_request_id=None,
        start_after=None)

    object_array=[]
    for i in res.data.objects:
        # exclude objects that are folders
        if i.name[-1]!="/":
            object_array.append(i.name)

    return object_array