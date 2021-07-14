import coreapi
import coreschema
from rest_framework.schemas import ManualSchema


ReceiptSchema =  ManualSchema(fields=[
 
    coreapi.Field(
        "casher_user_id",
        required=True,
        location="form",
        schema=coreschema.Integer(description="0 for all meeting list or the user_id ")
    ),

    coreapi.Field(
        "customer_name",
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        "customer_phone",
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        "customer_address",
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        "item",
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        "unit_price",
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        "quantity",
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    #     coreapi.Field(
    #     "total",
    #     required=True,
    #     location="form",
    #     schema=coreschema.Float()
    # ),
    coreapi.Field(
        "description",
        required=True,
        location="form",
        schema=coreschema.String()
    ),
])