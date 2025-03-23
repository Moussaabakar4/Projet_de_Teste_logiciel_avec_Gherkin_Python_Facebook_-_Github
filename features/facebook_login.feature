Feature: Page de connexion Facebook

        Scenario: Connexion réussie avec des identifiants valides
            Given L'utilisateur est sur la page de connexion de Facebook
             When L'utilisateur saisit "moussaabakarabbazene" dans le champ identifiant
              And L'utilisateur saisit "abbazene78" dans le champ mot de passe
              And L'utilisateur clique sur le bouton "Connexion"
             Then L'utilisateur est redirigé vers la page d'accueil

        Scenario: Connexion échouée avec un mot de passe incorrect
            Given L'utilisateur est sur la page de connexion de Facebook
             When L'utilisateur saisit "valid_user@gmail.com" dans le champ identifiant
              And L'utilisateur saisit "abbazene78" dans le champ mot de passe
              And L'utilisateur clique sur le bouton "Connexion"
             Then Un message d'erreur "Identifiants invalides" est affiché

  Scenario: Connexion échouée avec un nom d'utilisateur incorrect
    Given L'utilisateur est sur la page de connexion de Facebook
    When L'utilisateur saisit "moussa@gmail.com" dans le champ identifiant
    And L'utilisateur saisit "abbazene78" dans le champ mot de passe
    And L'utilisateur clique sur le bouton "Connexion"
    Then Un message d'erreur "Identifiants invalides" est affiché

  Scenario: Connexion échouée avec un nom d'utilisateur vide
    Given L'utilisateur est sur la page de connexion de Facebook
    When L'utilisateur saisit " " dans le champ identifiant
    And L'utilisateur saisit "abbazene78" dans le champ mot de passe
    And L'utilisateur clique sur le bouton "Connexion"
    Then Un message d'erreur "Identifiants invalides" est affiché

  Scenario: Connexion échouée avec un mot de passe vide
    Given L'utilisateur est sur la page de connexion de Facebook
    When L'utilisateur saisit "moussaabakarabbazene" dans le champ identifiant
    And L'utilisateur saisit " " dans le champ mot de passe
    And L'utilisateur clique sur le bouton "Connexion"
    Then Un message d'erreur "Identifiants invalides" est affiché

