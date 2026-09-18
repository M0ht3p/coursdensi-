import java.util.Scanner;

public class VerificateurMotDePasse {

    public static boolean motDePasseSecurise(String motDePasse) {
        boolean longueurSuffisante = motDePasse.length() >= 8;
        boolean contientMajuscule = motDePasse.matches(".*[A-ZÀ-ÖØ-Þ].*");
        boolean contientChiffre = motDePasse.matches(".*[0-9].*");

        return longueurSuffisante
                && contientMajuscule
                && contientChiffre;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Vérificateur de mot de passe ===");
        System.out.println("Votre mot de passe doit respecter les règles suivantes :");
        System.out.println("- Contenir au moins 8 caractères ;");
        System.out.println("- Contenir au moins une lettre majuscule ;");
        System.out.println("- Contenir au moins un chiffre.");
        System.out.println();

        System.out.print("Saisissez votre mot de passe : ");
        String motDePasse = scanner.nextLine();

        if (!motDePasseSecurise(motDePasse)) {
            System.out.println();
            System.out.println("Votre mot de passe n'est pas suffisamment sécurisé.");

            if (motDePasse.length() < 8) {
                System.out.println("- Il doit contenir au moins 8 caractères.");
            }

            if (!motDePasse.matches(".*[A-ZÀ-ÖØ-Þ].*")) {
                System.out.println("- Il doit contenir au moins une lettre majuscule.");
            }

            if (!motDePasse.matches(".*[0-9].*")) {
                System.out.println("- Il doit contenir au moins un chiffre.");
            }

            scanner.close();
            return;
        }

        System.out.println();
        System.out.println("Votre mot de passe respecte les règles de sécurité.");

        System.out.print("Confirmez votre mot de passe : ");
        String confirmation = scanner.nextLine();

        if (motDePasse.equals(confirmation)) {
            System.out.println("Mot de passe confirmé avec succès !");
        } else {
            System.out.println("Erreur : les deux mots de passe ne correspondent pas.");
        }

        scanner.close();
    }
}
