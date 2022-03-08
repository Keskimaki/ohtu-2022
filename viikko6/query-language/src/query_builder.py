from matchers import And, Or, Not, All, PlaysIn, HasAtLeast, HasFewerThan

class QueryBuilder:
    def __init__(self, query = All()):
        self._query_object = query

    def oneOf(self, *queries):
        return QueryBuilder(And(Or(*queries), self._query_object))

    def playsIn(self, team):
        return QueryBuilder(And(PlaysIn(team), self._query_object))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(HasAtLeast(value, attr), self._query_object))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(HasFewerThan(value, attr), self._query_object))

    def build(self):
        return self._query_object
