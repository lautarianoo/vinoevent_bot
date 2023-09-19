import peewee

conn = peewee.MySQLDatabase('teleevent', user='teleuser', password="%Lautariano5%", host="31.129.104.244", port=3306)

class BaseModel(peewee.Model):
    class Meta:
        database = conn

class Event(BaseModel):

    website_id = peewee.IntegerField(column_name="WebsiteId", null=True)
    city_id = peewee.IntegerField(column_name='CityId',null=True)
    type_id = peewee.IntegerField(column_name="TypeId",null=True)
    organization_id = peewee.IntegerField(column_name="Organization",null=True)
    title = peewee.TextField(column_name='Title', null=False)
    is_active = peewee.BooleanField(column_name="IsActive", default=False)
    date_event = peewee.DateField(column_name="DateEvent",null=True)
    address = peewee.CharField(column_name="Address",null=True)
    description = peewee.TextField(column_name="Description",null=True)
    time_start = peewee.TimeField(column_name="TimeStart",null=True)
    time_end = peewee.TimeField(column_name="TimeEnd",null=True)

    class Meta:
        table_name = 'Event'

class Organization(BaseModel):
    name_organization = peewee.CharField(column_name='Title')
    address = peewee.CharField(column_name="AddressOrg")
    city_id = peewee.IntegerField(column_name="CityId")

    class Meta:
        table_name = 'City'

class City(BaseModel):
    title = peewee.CharField(column_name='Title')

    class Meta:
        table_name = 'City'

class TypeEvent(BaseModel):
    title = peewee.CharField(column_name='Title')

    class Meta:
        table_name = 'TypeEvent'

if __name__ == '__main__':
    Event.delete().execute()
    #City.create_table()
    #Event.create_table()
    #TypeEvent.create_table()
    #Organization.create_table()
    #City.create(title='Город 1')
    #City.create(title='Город 2')
    #TypeEvent.create(title='Дегустации')
    #TypeEvent.create(title='Мероприятия')
    #TypeEvent.create(title='Курсы')
    #TypeEvent.create(title='Винное казино')
    #TypeEvent.create(title='Гастроужины')
    #Event.create(title='Винное казино всем на успех', city_id=1, type_id=1)
    #Event.create(title='Событие 2', city_id=1, type_id=1)
    #Event.create(title='Событие 3', city_id=2, type_id=2)
