import joblib
from azureml.core.model import Model
from azureml.core import Workspace

# Load the trained model
model = joblib.load('event_classifier.pkl')

# Connect to Azure ML workspace
ws = Workspace.from_config()

# Register and deploy the model
model = Model.register(ws, model_name="EventClassifier", model_path="event_classifier.pkl")
print(f"Model registered: {model.name}")

# Deploy the model as a web service
from azureml.core.webservice import AciWebservice, Webservice
from azureml.core.model import InferenceConfig

inference_config = InferenceConfig(runtime="python", entry_script="score.py", conda_file="myenv.yml")
aci_config = AciWebservice.deploy_configuration(cpu_cores=1, memory_gb=1)

service = Model.deploy(ws, "event-classifier-service", [model], inference_config, aci_config)
service.wait_for_deployment(show_output=True)
print(f"Model deployed at: {service.scoring_uri}")
