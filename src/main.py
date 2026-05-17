from dotenv import load_dotenv 
import os

def print_author():
  load_dotenv(dotenv_path='/home/ivan/Документы/practicum_git_sprint/.env')
  author = os.getenv('AUTHOR')
  print(f"Автор проекта: {author}")

print_author()