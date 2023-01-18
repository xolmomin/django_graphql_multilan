from graphene_django import DjangoObjectType
import graphene

from apps.models import Product


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class Query(graphene.ObjectType):
    products = graphene.List(ProductType)
    product = graphene.Field(ProductType, id=graphene.Int())

    @graphene.resolve_only_args
    def resolve_products(self):
        return Product.objects.all()

    @graphene.resolve_only_args
    def resolve_product(self, id):
        return Product.objects.get(pk=id)


schema = graphene.Schema(query=Query)
