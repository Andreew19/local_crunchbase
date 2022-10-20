import csv
import datetime
from startups.models import Startups, Founds, Articles, Categories

class Import:
  def startups():
    with open('startups.csv', newline='') as csvfile:
      spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
      for row in spamreader:
        print(row)
        name = row[0]
        round = row[1]
        round_date = row[2]
        description = row[3]
        url = row[4]

        startup = Startups(
          name=name,
          url=url,
          description=description
        )

        startup.save()
        print(startup.id)

        amount_level = round[-1]
        amount = float(round[1:-1])
        amount = amount * 1000 if amount_level == "K" else amount
        amount = amount * 1000000 if amount_level == "M" else amount

        months = {
          "апреля": "apr",
          "мая": "may",
          "июня": "jun",
          "июля": "jul",
          "августа": "aug",
          "сентября": "sep",
          "октября": "oct",
          "ноября": "nov",
          "декабря": "dec",
          "января": "jan",
          "февраля": "feb",
          "марта": "mar"
        }

        round_date = round_date.split(" ")[1:-1]
        round_date[1] = months[round_date[1]]
        round_date = datetime.datetime.strptime(" ".join(round_date), '%d %b %Y')

        round = Founds(
          amount=amount,
          currency=round[0],
          startup=startup,
          publicated_at=round_date
        )

        round.save()

  def articles():
    with open('articles.csv', newline='') as csvfile:
      spamreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
      for row in spamreader:
        print(row)
        print(12)
        title = row['title']
        categories = row['categories'][1:-1].replace("\"", "").split(",")
        content = row['content']
        iso_date = row['isoDate']
        link = row['link']

        article = Articles(
          title=title,
          link=link,
          description=content
        )

        article.save()

        for category in categories:
          cat, created = Categories.objects.get_or_create(name=category)

          print(cat)

          article.article_categories.add(cat)

  def inside():
    startups = Startups.objects.all()
    for article in Articles.objects.all():
      for startup in startups:
        if startup.name in article.title:
          print(article.title)
          print(startup.name)