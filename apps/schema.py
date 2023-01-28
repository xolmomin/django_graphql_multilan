from graphene_django import DjangoObjectType
import graphene

from apps.models import Product, Category


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class CategoryInput(graphene.InputObjectType):
    name = graphene.String()


class ProductInput(graphene.InputObjectType):
    id = graphene.Int()
    name = graphene.String()
    description = graphene.String()
    price = graphene.Float()
    category_id = graphene.Int()


class Query(graphene.ObjectType):
    products = graphene.List(ProductType)
    product = graphene.Field(ProductType, id=graphene.Int())

    categories = graphene.List(CategoryType)
    category = graphene.Field(CategoryType, id=graphene.Int())

    @graphene.resolve_only_args
    def resolve_products(self):
        return Product.objects.all()

    @graphene.resolve_only_args
    def resolve_product(self, id):
        return Product.objects.get(pk=id)

    @graphene.resolve_only_args
    def resolve_categories(self):
        return Category.objects.all()

    @graphene.resolve_only_args
    def resolve_category(self, id):
        return Category.objects.get(pk=id)


class CreateCategory(graphene.Mutation):
    class Arguments:
        category_data = CategoryInput(required=True)

    category = graphene.Field(CategoryType)

    @staticmethod
    def mutate(root, info, category_data=None):
        category_instance = Category(name=category_data.name)
        category_instance.save()
        return CreateCategory(category=category_instance)  # noqa


class CreateProduct(graphene.Mutation):
    class Arguments:
        product_data = ProductInput(required=True)

    product = graphene.Field(ProductType)

    @staticmethod
    def mutate(root, info, product_data=None):
        product_instance = Product(**product_data).save()
        # product = Product(
        #     name=product_data.name,
        #     description=product_data.description,
        #     price=product_data.price,
        #     category_id=product_data.category_id
        # )
        # product.save()
        return CreateProduct(product=product_instance)  # noqa


class UpdateProduct(graphene.Mutation):
    class Arguments:
        product_data = ProductInput(required=True)

    product = graphene.Field(ProductType)

    @staticmethod
    def mutate(root, info, product_data=None):
        product_instance = Product.objects.get(pk=product_data.id)
        if product_instance:
            # product_data.pop('id')
            # product_instance.update(**product_data)
            # product_instance.save(update_fields={**product_data})

            product_instance.name = product_data.name
            product_instance.description = product_data.description
            product_instance.price = product_data.price
            product_instance.category_id = product_data.category_id
            product_instance.save()

            return UpdateProduct(product=product_instance)  # noqa
        return UpdateProduct(product=None)  # noqa


class DeleteProduct(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    product = graphene.Field(ProductType)

    @staticmethod
    def mutate(root, info, id):
        Product.objects.get(pk=id).delete()


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
