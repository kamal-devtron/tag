from ruamel.yaml import YAML

yaml = YAML()
yaml.sort_keys = False
yaml.preserve_quotes = True
yaml.explicit_start = True


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

merged_tasks = []

if checkReleaseValues("orchestrator"):
    with open("release-yamls/orchestrator.yaml") as orchestrator:
        orchestrator_task = yaml.load(orchestrator)
        merged_tasks = merged_tasks + orchestrator_task

if checkReleaseValues("kubewatch"):
    with open("release-yamls/kubewatch.yaml") as kubewatch:
        kubewatch_task = yaml.load(kubewatch)
        merged_tasks = merged_tasks + kubewatch_task
        print(merged_tasks)


workflow_file['spec']['templates'][0]['dag']['tasks'] = merged_tasks
with open("kustomize/base/release-workflow.yaml", mode="w") as workflow:
    yaml.dump(workflow_file, workflow)