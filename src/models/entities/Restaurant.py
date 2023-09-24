
class Restaurant():
    def __init__(self,id,rating=None,name=None,site=None,email=None,phone=None,street=None,city=None,state=None,lat=None,ing=None) -> None:
        self.id=id
        self.rating= rating
        self.name= name
        self.site = site
        self.email=email
        self.phone=phone
        self.street=street
        self.city=city
        self.state=state
        self.lat=lat
        self.ing=ing

    def to_JSON(self):
        return {
            'id':self.id,
            'rating':self.rating,
            'name':self.name,
            'site':self.site ,
            'email':self.email,
            'phone':self.phone,
            'street':self.street,
            'city':self.city,
            'state':self.state,
            'lat':self.lat,
            'ing':self.ing,
        } 