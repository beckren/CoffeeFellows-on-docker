import graphene

import Listen.schema


class Query(Listen.schema.Query, graphene.ObjectType):
    pass

class Mutation(Listen.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)