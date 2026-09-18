def mot_de_passe_securise?(mot_de_passe)
  longueur_suffisante = mot_de_passe.length >= 8
  contient_majuscule = mot_de_passe.match?(/[A-ZÀ-ÖØ-Þ]/)
  contient_chiffre = mot_de_passe.match?(/[0-9]/)

  longueur_suffisante && contient_majuscule && contient_chiffre
end

puts "=== Vérificateur de mot de passe ==="
puts "Votre mot de passe doit respecter les règles suivantes :"
puts "- Contenir au moins 8 caractères"
puts "- Contenir au moins une lettre majuscule"
puts "- Contenir au moins un chiffre"
puts

print "Saisissez votre mot de passe : "
mot_de_passe = STDIN.gets&.chomp || ""

unless mot_de_passe_securise?(mot_de_passe)
  puts
  puts "Votre mot de passe n'est pas suffisamment sécurisé."

  puts "- Il doit contenir au moins 8 caractères." if mot_de_passe.length < 8
  puts "- Il doit contenir au moins une lettre majuscule." unless mot_de_passe.match?(/[A-ZÀ-ÖØ-Þ]/)
  puts "- Il doit contenir au moins un chiffre." unless mot_de_passe.match?(/[0-9]/)

  exit
end

puts
puts "Votre mot de passe respecte les règles de sécurité."

print "Confirmez votre mot de passe : "
confirmation = STDIN.gets&.chomp || ""

if mot_de_passe == confirmation
  puts "Mot de passe confirmé avec succès !"
else
  puts "Erreur : les deux mots de passe ne correspondent pas."
end
