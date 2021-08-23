project_id= 'ericvb-hybrid-cloud'
location = 'us' # Format is 'us' or 'eu'
processor_id = 'fdfc7b292ceba571' # Create processor in Cloud Console
file_path = 'w2_sample.pdf' # The local file in your current working directory

from google.cloud import documentai_v1beta3 as documentai
from google.cloud import storage
from prettytable import PrettyTable


def process_document(
    project_id=project_id, location=location, processor_id=processor_id,  file_path=file_path
):

    # Instantiates a client
    client = documentai.DocumentProcessorServiceClient()

    # The full resource name of the processor, e.g.:
    # projects/project-id/locations/location/processor/processor-id
    # You must create new processors in the Cloud Console first
    name = f"projects/{project_id}/locations/{location}/processors/{processor_id}"

    with open(file_path, "rb") as image:
        image_content = image.read()

    # Read the file into memory
    document = {"content": image_content, "mime_type": "application/pdf"}

    # Configure the process request
    request = {"name": name, "document": document}

    # Use the Document AI client to process the sample form
    result = client.process_document(request=request)

    document = result.document
    document_text = document.text
    print("Document processing complete.")
    print("Text: {}".format(document_text))
