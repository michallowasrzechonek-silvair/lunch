from fastapi import FastAPI, Query

app = FastAPI(title="Lunch Topic Generator")


@app.get("/")
def lunch_topic(count: int = Query(1)):
    return count
