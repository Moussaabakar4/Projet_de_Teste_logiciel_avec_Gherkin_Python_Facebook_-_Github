from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('L\'utilisateur est sur la page de connexion de GitHub')
def step_open_github_login_page(context):
    context.driver = webdriver.Chrome()  # Lance le navigateur
    context.driver.get("https://github.com/login")  # Ouvre la page de connexion
    context.driver.maximize_window()

@when('L\'utilisateur saisit son identifiant GitHub "{username}"')
def step_enter_github_username(context, username):
    username_field = context.driver.find_element(By.ID, "login_field")
    username_field.clear()  # Assurez-vous que le champ est vide avant de taper
    username_field.send_keys(username)  # Tapez le nom d'utilisateur

@when('L\'utilisateur saisit son mot de passe GitHub "{password}"')
def step_enter_github_password(context, password):
    password_field = context.driver.find_element(By.ID, "password")
    password_field.clear()  # Assurez-vous que le champ est vide avant de taper
    password_field.send_keys(password)  # Tapez le mot de passe

@when('L\'utilisateur clique sur le bouton "Connexion" sur GitHub')
def step_click_github_login_button(context):
    context.driver.find_element(By.NAME, "commit").click()  # Clique sur le bouton de connexion
    time.sleep(5)  # Attendez pour que la redirection se termine

@then('L\'utilisateur est redirigé vers la page d\'accueil de GitHub')
def step_check_github_homepage_redirection(context):
    assert "https://github.com/" in context.driver.current_url  # Vérifie que la redirection est réussie
    context.driver.quit()  # Ferme le navigateur

@then('Un message d\'erreur "Incorrect username or password." est affiché sur GitHub')
def step_check_github_error_message(context):
    error_message = context.driver.find_element(By.CSS_SELECTOR, "div.flash.flash-full.flash-error").text
    assert "Incorrect username or password." in error_message  # Vérifie que le message d'erreur est correct
    context.driver.quit()  # Ferme le navigateur
