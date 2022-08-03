import time
import oci
from config import *
import list_objects

def main():
    retry_strategy = oci.retry.DEFAULT_RETRY_STRATEGY
    if auth_method == "resource_principal":
        rps = oci.auth.signers.get_resource_principals_signer()
        ai_vision_client = oci.ai_vision.AIServiceVisionClient(config={}, signer=rps)
    elif auth_method == "api_key":
        config = oci.config.from_file(config_file_path, config_profile)
        ai_vision_client = oci.ai_vision.AIServiceVisionClient(config=config, retry_strategy=retry_strategy)
    else:
        print("Assign a value to auth_method in config.py: \"resource_princpal\" or \"api_key\".")

    # gather objects from Object Storage location
    object_storage_objects=list_objects.main()
    object_locations=[]
    for i in object_storage_objects:
        current_object=oci.ai_vision.models.ObjectLocation(
            namespace_name=object_location_namespace_name,
            bucket_name=object_location_bucket_name,
            object_name=i)
        object_locations.append(current_object)

    # Send the request to service, some parameters are not required, see API
    # doc for more info
    res = ai_vision_client.create_image_job(
        create_image_job_details=oci.ai_vision.models.CreateImageJobDetails(
            input_location=oci.ai_vision.models.ObjectListInlineInputLocation(
                object_locations=object_locations),
            features=[oci.ai_vision.models.ImageClassificationFeature(
                    feature_type="IMAGE_CLASSIFICATION")],
            output_location=oci.ai_vision.models.OutputLocation(
                namespace_name=output_location_namespace_name,
                bucket_name=output_location_bucket_name,
                prefix=output_location_prefix),
            compartment_id=compartment_id,
            is_zip_output_enabled=is_zip_output_enabled))

    # Get the data from response
    print("**************************Analyze Image Batch Job**************************")
    print(res.data)

    job_id=res.data.id
    seconds=0
    res=ai_vision_client.get_image_job(image_job_id=job_id)

    # track the job progress
    while res.data.lifecycle_state=="IN_PROGRESS" or res.data.lifecycle_state=="ACCEPTED":
        print("Job " + job_id + " is IN_PROGRESS for "+str(int(seconds/3600))+"h "+str(int((seconds/60)%60))+"m "+str(int(seconds%60))+"s")
        time.sleep(5)
        seconds+=5
        res=ai_vision_client.get_image_job(image_job_id=job_id)

    print("**************************Get Image Job Result**************************")
    print(res.data)

main()