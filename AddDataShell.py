# this why for speed add databeas in shell Without detail
from teams.models import Team
Team.object.create(name='فريق النصور', details='فريق النصور مقرة في مصر')

# this why for add databeas with detail
from teams.models import Team
team = Team()
team.name = 'فريق العرب'
team.details = 'فريق العرب مقرة في الخليج العربي'
team.save()

# for view databeas
Team.object.all() # Team For example You can import to another name