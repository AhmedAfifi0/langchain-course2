import os

from dotenv import load_dotenv

load_dotenv()


def main():
    print("Hello from langchain-course2!")
    print(os.environ.get("OPEN_AI_KEY"))


if __name__ == "__main__":
    main()
