#-*- coding: utf-8 -*-
from django import template
from datetime import date, timedelta
from accueil.models import Classe
conf=__import__('ecolle.config')

register = template.Library()

@register.filter
def nometab(d):
	return conf.config.NOM_ETABLISSEMENT

@register.filter
def lookup(d,key):
    return d[key]

@register.filter
def integer(n):
    return int(n)

@register.filter
def addtime(temps, ajout):
    return temps+timedelta(days=ajout)

@register.filter
def heurecolle(temps):
	temps = temps or 0 # car une somme sur un ensemble vide peut renvoyer None
	return "{}h{:02d}".format(temps//60,temps%60)

@register.filter
def heure(heure):
	return "{}h{:02d}".format(heure//4,15*(heure%4))

@register.filter
def image(fichier):
    return fichier.replace('programme','image').replace('pdf','jpg')

@register.filter
def tzip(l1, l2):
    return zip(l1,l2)

@register.assignment_tag
def get_mathjax():
    return conf.config.MATHJAX

@register.assignment_tag
def get_ects():
    return conf.config.ECTS

@register.assignment_tag
def get_modifgroupe():
    return conf.config.MODIF_SECRETARIAT_GROUPE

@register.assignment_tag
def get_classes():
    return Classe.objects.all()

