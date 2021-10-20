from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Ville(models.Model):
    id=models.AutoField(db_column="idV",primary_key=True)
    lib = models.CharField(db_column="nomV",max_length=200)
    createdAt = models.DateTimeField(db_column="v_createdAt",auto_now_add=True)
    updatedAt = models.DateTimeField(db_column="v_updatedAt",auto_now=True)
    
    def __str__(self):
        return self.lib[:50]


class Logement(models.Model):
    id=models.AutoField(db_column="idLo",primary_key=True)
    lib = models.CharField(db_column="libLo",max_length=200)
    detail = models.TextField(db_column="detailLo")
    ville = models.ForeignKey(Ville,db_column="idV",on_delete=models.DO_NOTHING) 
    user = models.ForeignKey(User,db_column="userId",on_delete=models.DO_NOTHING)
    createdAt = models.DateTimeField(db_column="lo_createdAt",auto_now_add=True)
    updatedAt = models.DateTimeField(db_column="lo_updatedAt",auto_now=True)

    class Meta:
        #db_table="Logement"
        ordering=["-updatedAt"]

    def __str__(self):
        return self.lib[:50]

    def logements(self):
        return self.objects.all()

    def getById(self,id:int):
        return self.objects.get(id=id)




class Niveau(models.Model):
    id = models.AutoField(db_column="idNiv",primary_key=True)
    lib = models.CharField(db_column="libNiv",max_length=200)
    detail = models.TextField(db_column="detailNiv",null=True,blank=True)
    createdAt = models.DateTimeField(db_column="niv_createdAt",auto_now_add=True)
    updatedAt = models.DateTimeField(db_column="niv_updatedAt",auto_now=True)

    
    class Meta:
        #db_table="Niveau"
        ordering=["lib"]
    
    
    def __str__(self):
        return self.lib[:50]

    def niveaux(self):
        return self.objects.all()

    def getById(self,id:int):
        return self.objects.get(id=id)

    def getMetierCount(self):
        return self.metier_set.count()


class Debouche(models.Model):
    id = models.AutoField(db_column="idDeb",primary_key=True)
    lib = models.CharField(db_column="libDeb",max_length=200)
    detail = models.TextField(db_column="detailDeb")
    createdAt = models.DateTimeField(db_column="deb_createdAt",auto_now_add=True)
    updatedAt = models.DateTimeField(db_column="deb_updatedAt",auto_now=True)

    def __str__(self) -> str:
        return self.lib[:50]

    class Meta:
        #db_table="Logement"
        ordering=["lib"]

class Metier(models.Model):
    id=models.AutoField(db_column="idM",primary_key=True)
    niveau=models.ForeignKey(Niveau,db_column="idNiv",on_delete=models.DO_NOTHING,related_name="Metier")
    debouche=models.ForeignKey(Debouche,db_column="idDeb",on_delete=models.DO_NOTHING,related_name="Metier")

    def __str__(self) -> str:
        return self.niveau.lib[:30] +"->"+self.debouche.lib[:30]

class Ecole(models.Model):
    id = models.AutoField(db_column="idEc",primary_key=True)
    lib = models.CharField(db_column="nomEc",max_length=200)
    adr = models.CharField(db_column="adrEc",max_length=200)
    phone = models.CharField(db_column="phoneEc",max_length=100)
    email = models.EmailField(db_column="emailEc",max_length=100)
    ville = models.ForeignKey(Ville,db_column="idV",on_delete=models.DO_NOTHING,related_name="Ecoles")
    formations = models.ManyToManyField(Niveau,related_name="Formations",blank=True) #db_table="Former"
    createdAt = models.DateTimeField(db_column="ec_createdAt",auto_now_add=True)
    updatedAt = models.DateTimeField(db_column="ec_updatedAt",auto_now=True)
    deactivatedAt = models.DateTimeField(db_column="ec_deactivatedAt",null=True,blank=True)

    class Meta:
        #db_table="Logement"
        ordering=["lib"]

    def __str__(self)->str:
        return self.lib[:50]+" ("+self.ville.lib[:20] +")"

