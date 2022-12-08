import matchers


class QueryBuilder:
    def __init__(self, matchers=[matchers.All()]) -> None:
        self._matchers = matchers

    def build(self):
        matcher = matchers.And(*self._matchers)
        self._matchers.clear()
        return matcher

    def oneOf(self, m1, m2):
        matcher = matchers.Or(*(m1, m2))
        return QueryBuilder([matcher])

    def playsIn(self, team):
        self._matchers.append(matchers.PlaysIn(team))
        return QueryBuilder(self._matchers)

    def hasAtLeast(self, value, attr):
        self._matchers.append(matchers.HasAtLeast(value, attr))
        return QueryBuilder(self._matchers)

    def hasFewerThan(self, value, attr):
        self._matchers.append(matchers.HasFewerThan(value, attr))
        return QueryBuilder(self._matchers)
