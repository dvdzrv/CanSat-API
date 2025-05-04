import uvicorn

if __name__ == "__main__":
    from main import app
    from uvicorn import run
    import multiprocessing

    multiprocessing.freeze_support()
    uvicorn.run(app, host="0.0.0.0", port=3000, reload=False, workers=1)