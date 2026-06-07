import graphene

class Product(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    sku = graphene.String()
    price = graphene.Float()
    quantity = graphene.Int()