from matchers import And, Or, Not, All, PlaysIn, HasAtLeast, HasFewerThan

class QueryBuilder:
    def __init__(self, query = All()):
        self.query_object = query

    def playsIn(self, team):
        return QueryBuilder(And(PlaysIn(team), self.query_object))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(HasAtLeast(value, attr), self.query_object))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(HasFewerThan(value, attr), self.query_object))

    def build(self):
        return self.query_object
