import json
import os

# Chemin du fichier de rapport
REPORT_FILE = "github_results.json"

def before_all(context):
    # Initialisation du fichier JSON
    if os.path.exists(REPORT_FILE):
        os.remove(REPORT_FILE)
    with open(REPORT_FILE, "w") as f:
        json.dump({"tests": []}, f)

def after_scenario(context, scenario):
    # Récupération des informations sur le scénario
    result = {
        "scenario": scenario.name,
        "status": "passed" if scenario.status == "passed" else "failed",
        "steps": []
    }
    for step in scenario.steps:
        result["steps"].append({
            "name": step.name,
            "status": "passed" if step.status == "passed" else "failed"
        })

    # Écriture dans le fichier JSON
    with open(REPORT_FILE, "r") as f:
        data = json.load(f)
    data["tests"].append(result)
    with open(REPORT_FILE, "w") as f:
        json.dump(data, f, indent=4)

def after_all(context):
    # Fermeture du navigateur si encore ouvert
    if hasattr(context, "driver"):
        context.driver.quit()
