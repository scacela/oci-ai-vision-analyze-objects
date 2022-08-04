# authentication method: "api_key" or "resource_principal"
auth_method="resource_principal"
# config file path
config_file_path="~/.oci/config"
# config file profile
config_profile="DEFAULT"
# compartment id of create_image_job
compartment_id = "<COMPARTMENT OCID>"
# model id: to use default model, assign: None
model_id = "<AI VISION MODEL OCID>"
# feature type: "IMAGE_CLASSIFICATION" or "OBJECT_DETECTION" or "DOCUMENT_CLASSIFICATION" or "KEY_VALUE_DETECTION" or "LANGUAGE_CLASSIFICATION" or "TABLE_DETECTION" or "TEXT_DETECTION"
feature_type = "IMAGE_CLASSIFICATION"

# namespace of Object Storage location containing the images to be analyzed
object_location_namespace_name="<OBJECT STORAGE NAMESPACE FOR INFERENCE OBJECTS>"
# Object Storage bucket containing the images to be analyzed
object_location_bucket_name="<BUCKET NAME FOR INFERENCE OBJECTS>"
# Prefix in bucket containing images to be analyzed
object_location_prefix=""

# namespace of Object Storage location where the image analysis will be generated
output_location_namespace_name="<OBJECT STORAGE NAMESPACE FOR OUTPUT ANALYSIS>"
# Object Storage bucket where the image analysis will be generated
output_location_bucket_name="<BUCKET NAME FOR OUTPUT ANALYSIS>"
# Prefix in bucket where image analysis will be generated
output_location_prefix="Analysis"

# Generate a zip file for all analyzed results in user-specified output location in object storage
# set is_zip_output_enabled true to enable zip output feature
is_zip_output_enabled=True