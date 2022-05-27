from pydantic import BaseModel, Field


class Contact(BaseModel):
    name: str = Field(default='name')
    surname: str = Field(default='surname')
    phone: str = Field(default='phone')
    address: str = Field(default='address')


class Deal(BaseModel):
    title: str = Field(default='title')
    description: str = Field(default='description')
    products: list = Field(default=[])
    delivery_address: str = Field(default='delivery_address')
    delivery_date: str = Field(default='delivery_date')
    delivery_code: str = Field(default='delivery_code')

    def __eq__(self, other):
        if isinstance(other, Deal):
            return (self.delivery_date == other.delivery_date
                    and sorted(self.products) == sorted(other.products)
                    and self.delivery_address == other.delivery_address)
        return NotImplemented


class RequestBody(BaseModel):
    deal: Deal = Field(...)
    contact: Contact = Field(...)
