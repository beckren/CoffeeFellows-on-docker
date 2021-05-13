import graphene
from graphene_django import DjangoObjectType

from .models import Mitarbeiter
from .models import Produkt

class MitarbeiterType(DjangoObjectType):
    class Meta:
        model = Mitarbeiter

class ProduktType(DjangoObjectType):
    class Meta:
        model = Produkt


class Query(graphene.ObjectType):
    mitarbeiter = graphene.List(MitarbeiterType)

    def resolve_mitarbeiter(self, info, **kwargs):
        return Mitarbeiter.objects.all()


class ProduktInput(graphene.InputObjectType):
    produkt_bezeichnung = graphene.String()
    produkt_anzahl = graphene.Decimal()

class CreateProducts(graphene.Mutation):
    class Arguments:
        produkte = graphene.List(ProduktInput)
    ok = graphene.Boolean()

    def mutate(self, info, **kwargs):
        produkteList = [Produkt.objects.create(produkt_bezeichnung=produkt.produkt_bezeichnung, produkt_anzahl=produkt.produkt_anzahl ) for produkt in kwargs.get('produkte')]
        return CreateProducts(produkteList)

# class ProduktInput(graphene.InputObjectType):
#     id = graphene.Int()
#     bezeichnung = graphene.Int()
#     einheit = graphene.String()

# class CreateProdukte(graphene.Mutation):
#     class Input:
#        produkte = graphene.List(ProduktInput)

#     produkte = graphene.List(lambda: Produkt)

#     @staticmethod
#     def mutate(root, args, context, info):
#         produkte = [Produkt.objects.create(produkt_id_pkey=produkt.produkt_id_pkey, produkt_bezeichnung=produkt.produkt_bezeichnung, produkt_einheit_id_fkey = produkt.produkt_einheit_id_fkey) for produkt in args.get('produkte')]
#         return CreateProdukte(produkte=produkte)


# class Mutation(graphene.ObjectType):
#     create_produkte = CreateProdukte.Field()


# class CreateMitarbeiter(graphene.Mutation):
#     mitarbeiter_id_pkey = graphene.Int()
#     mitarbeiter_vorname = graphene.String()
#     mitarbeiter_nachname = graphene.String()

#     #2
#     class Arguments:
#         mitarbeiter_vorname = graphene.String()
#         mitarbeiter_nachname = graphene.String()

#     #3
#     def mutate(self, info, mitarbeiter_vorname, mitarbeiter_nachname):
#         mitarbeiter = Mitarbeiter(mitarbeiter_vorname=mitarbeiter_vorname, mitarbeiter_nachname=mitarbeiter_nachname)
#         mitarbeiter.save()

#         return CreateMitarbeiter(
#             mitarbeiter_id_pkey=mitarbeiter.mitarbeiter_id_pkey,
#             mitarbeiter_vorname=mitarbeiter.mitarbeiter_vorname,
#             mitarbeiter_nachname=mitarbeiter.mitarbeiter_nachname,
#         )
# class MitarbeiterInput(graphene.InputObjectType):
#     mitarbeiter_vorname = graphene.String()
#     mitarbeiter_nachname = graphene.String()

# class CreateMitarbeiter(graphene.Mutation):
#     class Input:
#        mitarbeiters = graphene.List(MitarbeiterInput)

#     mitarbeiters = graphene.List(lambda: Mitarbeiter)

#     @staticmethod
#     def mutate(root, args, context, info):
#         people = [Mitarbeiter.objects.create(mitarbeiter_vorname=mitarbeiter.mitarbeiter_vorname, mitarbeiter_nachname=mitarbeiter.mitarbeiter_nachname) for mitarbeiter in args.get('mitarbeiters')]
#         return CreateMitarbeiter(mitarbeiters=mitarbeiters)

class Mutation(graphene.ObjectType):
    create_products = CreateProducts.Field()