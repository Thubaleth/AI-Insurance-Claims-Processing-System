from pydantic import BaseModel, Field

class Claim(BaseModel):
    claim_id:str
    claim_type:str
    description:str
    estimated_amount:float |None =Field(default=None,gt=0) #optional



claim = Claim(
    claim_id="CLM-004",
    claim_type="CAR-ACCIDENT",
    description="Vehicle damaged in an accident"
)

print(claim)



