from django.db import models

#class Publisher(models.Model):
#    name = models.CharField(max_length=30)
#    address = models.CharField(max_length=50)
#    city = models.CharField(max_length=60)
#    state_province = models.CharField(max_length=30)
#    country = models.CharField(max_length=50)
#    website = models.URLField()

#    def __unicode__(self):
#        return self.name

class Author(models.Model):
    AuthorID = models.CharField(max_length=4)
    Name = models.CharField(max_length=30)
    Age = models.CharField(max_length=10)
    Country = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s %s' % (self.AuthorID, self.Name)

class Book(models.Model):
	ISBN = models.CharField(max_length=10)
	Title = models.CharField(max_length=100)
	AuthorID = models.ForeignKey(Author)
	Publisher = models.CharField(max_length=100)
	PublishDate = models.DateField()
	Price = models.CharField(max_length=20)

	def __unicode__(self):
		return self.Title
