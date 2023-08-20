import uvicorn


def main():
    # Process(target=looper).start()
    uvicorn.run("server:app", host="0.0.0.0", port=4444, reload=True, workers=9)


if __name__ == "__main__":
    main()
