from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import os
import objgraph  # <-- Ajout de l'importation

# Initialisation du rapport
REPORT_FILE = "reports/facebook_test_report.json"

if not os.path.exists("reports"):
    os.makedirs("reports")

# Initialiser le rapport de test
def initialize_report():
    if not os.path.exists(REPORT_FILE):
        with open(REPORT_FILE, "w") as file:
            json.dump({"tests": []}, file)

# Ajouter un résultat au rapport
def append_to_report(scenario, status, details=None):
    with open(REPORT_FILE, "r") as file:
        report = json.load(file)

    report["tests"].append({
        "scenario": scenario,
        "status": status,
        "details": details or {}
    })

    with open(REPORT_FILE, "w") as file:
        json.dump(report, file, indent=4)

# Fonction pour écrire les données de profilage dans un fichier texte
def write_to_txt(data, filename="memory_profile.txt"):
    """Écrit les données de profilage dans un fichier texte."""
    with open(filename, mode="a") as file:
        file.write(data + "\n")

# Initialisation du fichier texte
if not os.path.exists("memory_profile.txt"):
    with open("memory_profile.txt", mode="w") as file:
        file.write("Step,Object Type,Count\n")  # En-tête du fichier texte

initialize_report()

# Given - L'utilisateur est sur la page de connexion de Facebook
@given('L\'utilisateur est sur la page de connexion de Facebook')
def step_open_facebook_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.facebook.com/login")
    context.driver.maximize_window()

    # Profilage de la mémoire après l'initialisation du navigateur
    growth = objgraph.growth(limit=10)
    for obj_type, count in growth:
        write_to_txt(f"Initialisation du navigateur,{obj_type},{count}")

# When - L'utilisateur saisit un identifiant
@when('L\'utilisateur saisit "{username}" dans le champ identifiant')
def step_enter_username(context, username):
    context.username = username
    context.driver.find_element(By.ID, "email").send_keys(username)

    # Profilage de la mémoire après la saisie de l'identifiant
    growth = objgraph.growth(limit=10)
    for obj_type, count in growth:
        write_to_txt(f"Saisie de l'identifiant,{obj_type},{count}")

# When - L'utilisateur saisit un mot de passe
@when('L\'utilisateur saisit "{password}" dans le champ mot de passe')
def step_enter_password(context, password):
    context.password = password
    context.driver.find_element(By.ID, "pass").send_keys(password)

    # Profilage de la mémoire après la saisie du mot de passe
    growth = objgraph.growth(limit=10)
    for obj_type, count in growth:
        write_to_txt(f"Saisie du mot de passe,{obj_type},{count}")

# When - L'utilisateur clique sur le bouton "Connexion"
@when('L\'utilisateur clique sur le bouton "Connexion"')
def step_click_login_button(context):
    context.driver.find_element(By.NAME, "login").click()
    time.sleep(5)  # Attendre un peu pour que la page se charge

    # Profilage de la mémoire après la connexion
    growth = objgraph.growth(limit=10)
    for obj_type, count in growth:
        write_to_txt(f"Connexion,{obj_type},{count}")

# Then - L'utilisateur est redirigé vers la page d'accueil
@then('L\'utilisateur est redirigé vers la page d\'accueil')
def step_check_homepage_redirection(context):
    try:
        assert "https://www.facebook.com/login" in context.driver.current_url
        append_to_report(
            scenario=f"Connexion réussie pour {context.username}",
            status="success"
        )
    except AssertionError:
        append_to_report(
            scenario=f"Connexion réussie pour {context.username}",
            status="failure",
            details={"reason": "Redirection manquante"}
        )
        raise

    # Profilage de la mémoire après la vérification de la redirection
    growth = objgraph.growth(limit=10)
    for obj_type, count in growth:
        write_to_txt(f"Vérification de la redirection,{obj_type},{count}")

# Then - Un message d'erreur "Identifiants invalides" est affiché
@then('Un message d\'erreur "Identifiants invalides" est affiché')
def step_check_error_message(context):
    try:
        error_message = context.driver.find_element(By.XPATH, '//*[contains(text(), "Identifiants invalides")]')
        assert error_message.is_displayed()
        append_to_report(
            scenario=f"Connexion échouée pour {context.username}",
            status="success"
        )
    except AssertionError:
        append_to_report(
            scenario=f"Connexion échouée pour {context.username}",
            status="failure",
            details={"reason": "Message d'erreur manquant"}
        )
        raise

    # Profilage de la mémoire après la vérification du message d'erreur
    growth = objgraph.growth(limit=10)
    for obj_type, count in growth:
        write_to_txt(f"Vérification du message d'erreur,{obj_type},{count}")

# Then - Fermer le navigateur
@then('Fermer le navigateur')
def step_close_browser(context):
    context.driver.quit()