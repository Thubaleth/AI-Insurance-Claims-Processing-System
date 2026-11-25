from fastapi import FastAPI

#create API application

app = FastAPI(
    title= "AI Insurance Claims Processing System",
    description="An API for intellengent insurance claims processing",
    version="0.1.0"
)

#HTTP GET Endpoint
@app.get("/") 
def root():
    return {
        "message" : "Welcome to the AI insurance Claims Processing system"
    }


@app.get("/health")
def health_check():
    return{
        "status":"healthy",
        "application":"AI insurance Claims Processing"
    }

