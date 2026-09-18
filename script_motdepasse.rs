use std::io::{self, Write};

fn lire_texte(message: &str) -> String {
    print!("{}", message);
    io::stdout().flush().expect("Impossible d'afficher le message");

    let mut saisie = String::new();
    io::stdin()
        .read_line(&mut saisie)
        .expect("Impossible de lire la saisie");

    saisie.trim().to_string()
}

fn mot_de_passe_securise(mot_de_passe: &str) -> bool {
    let longueur_suffisante = mot_de_passe.chars().count() >= 8;
    let contient_majuscule = mot_de_passe.chars().any(|caractere| caractere.is_uppercase());
    let contient_chiffre = mot_de_passe.chars().any(|caractere| caractere.is_ascii_digit());

    longueur_suffisante && contient_majuscule && contient_chiffre
}

fn main() {
    println!("=== Vérificateur de mot de passe ===");
    println!("Votre mot de passe doit respecter les règles suivantes :");
    println!("- Contenir au moins 8 caractères ;");
    println!("- Contenir au moins une lettre majuscule ;");
    println!("- Contenir au moins un chiffre.");
    println!();

    let mot_de_passe = lire_texte("Saisissez votre mot de passe : ");

    if !mot_de_passe_securise(&mot_de_passe) {
        println!();
        println!("Votre mot de passe n'est pas suffisamment sécurisé.");

        if mot_de_passe.chars().count() < 8 {
            println!("- Il doit contenir au moins 8 caractères.");
        }

        if !mot_de_passe.chars().any(|caractere| caractere.is_uppercase()) {
            println!("- Il doit contenir au moins une lettre majuscule.");
        }

        if !mot_de_passe.chars().any(|caractere| caractere.is_ascii_digit()) {
            println!("- Il doit contenir au moins un chiffre.");
        }

        return;
    }

    println!();
    println!("Votre mot de passe respecte les règles de sécurité.");

    let confirmation = lire_texte("Confirmez votre mot de passe : ");

    if mot_de_passe == confirmation {
        println!("Mot de passe confirmé avec succès !");
    } else {
        println!("Erreur : les deux mots de passe ne correspondent pas.");
    }
}
