import coreapi
import coreschema
from rest_framework.schemas import ManualSchema


UpdateMeetingLogSchema =  ManualSchema(fields=[


    coreapi.Field(
        "user_id",
        required=True,
        location="form",
        schema=coreschema.Integer(description="0 for all meeting list or the user_id ")
    ),

    coreapi.Field(
        "start_date",
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        "end_date",
        required=True,
        location="form",
        schema=coreschema.String()
    ),
])