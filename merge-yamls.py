from ruamel.yaml import YAML

yaml = YAML()
yaml.sort_keys = False
yaml.preserve_quotes = True
yaml.explicit_start = True

merged_tasks = []
microservices = ["orchestrator", "kubewatch", "git-sensor", "lens", "notifier", "image-scanner", "kubelink", "casbin", "dashboard"]

# Get release values
with open("release-values.yaml") as file:
  release_values = yaml.load(file)

# Get target file
with open("kustomize/base/release-workflow.yaml") as workflow:
  workflow_file = yaml.load(workflow)

task_path = workflow_file['spec']['templates'][0]['dag']['tasks']

def checkReleaseValues(str: str):
  if release_values[str].lower() == "yes" or release_values[str].lower() == "true" or release_values[str] == True:
    return True

def mergeAllTasks():
  global merged_tasks
  for microservice in microservices:
    if checkReleaseValues(microservice):
      print("Found microservice", microservice)
      filePath = "release-yamls/%s.yaml"%(microservice)
      with open(filePath) as microservice_file:
        microservice_task = yaml.load(microservice_file)
        merged_tasks = merged_tasks + microservice_task

mergeAllTasks()

workflow_file['spec']['templates'][0]['dag']['tasks'] = merged_tasks
with open("kustomize/base/release-workflow.yaml", mode="w") as workflow:
  yaml.dump(workflow_file, workflow)
