Feature: Page de connexion GitHub

        Scenario: Connexion réussie avec des identifiants valides
            Given L'utilisateur est sur la page de connexion de GitHub
             When L'utilisateur saisit "moussaabakar4@gmail.com" dans le champ identifiant
              And L'utilisateur saisit "Abbazene78" dans le champ mot de passe
              And L'utilisateur clique sur le bouton "Connexion"
             Then L'utilisateur est redirigé vers la page d'accueil de GitHub

        Scenario: Connexion échouée avec un mot de passe incorrect
            Given L'utilisateur est sur la page de connexion de GitHub
             When L'utilisateur saisit "valid_user@gmail.com" dans le champ identifiant
              And L'utilisateur saisit "IncorrectPassword" dans le champ mot de passe
              And L'utilisateur clique sur le bouton "Connexion"
             Then Un message d'erreur "Incorrect username or password." est affiché sur GitHub
