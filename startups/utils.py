import csv

class Import:
  def startups():
    with open('startups.csv', newline='') as csvfile:
      spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
      for row in spamreader:
        name = row[0]
        round = row[1]
        round_date = row[2]
        description = row[3]
        url = row[4]

        Startups.objects.create(
          name: name,
          url: url,
          description: description
        )

        Round.objects.create(
          value: value(round),
          currency: currency(round),
          date: round_date # --> toDate
        )

  def articles():
    with open('articles.csv', newline='') as csvfile:
      spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
      for row in spamreader:
        print(', '.join(row))