from django.db import models

class Article(models.Model):
    titre = models.CharField(max_length=100)
    slug = models.SlugField()
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(verbose_name="Date de parution",
                                auto_now_add=True, auto_now=False)
    is_visible = models.BooleanField(verbose_name="Article publié ?",
                                     default=False)
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)

    def __str__(self):
        return self.titre

    # En cas de besoin, vous êtes autorisé à rajouter des méthodes ou
    # propriétés dans ce modèle.


class Categorie(models.Model):
    titre = models.CharField(max_length=100)

    def __str__(self):
        return self.titre


class Comment(models.Model):
    """ Modèle pour les commentaires. A vous de l'écrire ! """
    pseudo = models.CharField(max_length=100)
    mail = models.EmailField()
    description = models.TextField()
    date = models.DateTimeField(verbose_name="Date", auto_now_add=True, auto_now=False)
    is_visible = models.BooleanField(verbose_name="Commentaire publié ?", default=True)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    
