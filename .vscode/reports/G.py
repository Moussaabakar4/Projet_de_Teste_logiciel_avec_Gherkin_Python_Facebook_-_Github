from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import os

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

initialize_report()

# Given - L'utilisateur est sur la page de connexion de Facebook
@given('L\'utilisateur est sur la page de connexion de Facebook')
def step_open_facebook_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.facebook.com/")
    context.driver.maximize_window()

# When - L'utilisateur saisit un identifiant
@when('L\'utilisateur saisit "{username}" dans le champ identifiant')
def step_enter_username(context, username):
    context.username = username
    context.driver.find_element(By.ID, "email").send_keys(username)

# When - L'utilisateur saisit un mot de passe
@when('L\'utilisateur saisit "{password}" dans le champ mot de passe')
def step_enter_password(context, password):
    context.password = password
    context.driver.find_element(By.ID, "pass").send_keys(password)

# When - L'utilisateur clique sur le bouton "Connexion"
@when('L\'utilisateur clique sur le bouton "Connexion"')
def step_click_login_button(context):
    context.driver.find_element(By.NAME, "login").click()
    time.sleep(5)  # Attendre un peu pour que la page se charge

# Then - L'utilisateur est redirigé vers la page d'accueil
@then('L\'utilisateur est redirigé vers la page d\'accueil')
def step_check_homepage_redirection(context):
    try:
        assert "https://www.facebook.com/" in context.driver.current_url
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
