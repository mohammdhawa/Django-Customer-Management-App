# Returns all customers from customer table
customers = Customer.objects.all()

# Retruns first customer in table
firstcustomer = Customer.objects.first()

# Returns last customer in table
lastcustomer = Customer.objects.last()

# Returns single customer by name
customerByName = Customer.objects.get(name='Enes Afas')

# Returns all orders released to customer
firstcustomer.order_set.all()

# Returns order customer name: (Query parent model values)
order = Order.objects.first()
parentName = oorder.customer.name

# Returns products from products table with value fo 'out Door' in Category attribute
products = Product.objects.filter(Category="Out Door")

# Order/Sort objects by id
leastToGreatest = Product.objects.all().order_by('id')
greatestToLeast = Product.objects.all().order_by('-id')

# Returns all products with tag of 'Sports': (Query Many to Many fields)
productsFiltered = Product.objects.filter(tag__name='sports')


'''
Q: if the customer has more than 1 ball, how would you reflect it in the database?

A: Because there are many different products and this values changes constantly you would most
likly not want to store the value in the database but rather just make this a function we can run
each time we load the customers profile
'''

# Returns the total count for number of time a "Ball" was ordered by the first customer
ballOrders = firstcustomer.order_set.filter(product__name="Ball").count()

# Returns total count for each product ordered
allOrders = {}

for order in firstcustomer.order_set.all():
    if order.product.name in allOrders:
        allOrders[order.product.name] += 1
    else:
        allOrders[order.product.name] = 1

# Returns: allOrders {"Ball": 2, "BBQ Grill": 1}

# Related set example
class ParentModel(models.Model):
    name = models.Charfield(max_length=100, null=True)

class ChildModel(models.Model):
    parent = models.ForeignKey(ParentModel)
    name = models.CharField(max_length=100, null=True)

parent = ParentModel.objects.first()
# Returns all child models related to parent
parent.chilcmodel_set.all()