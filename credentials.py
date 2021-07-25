from dotenv import load_dotenv

load_dotenv()

super_secret = os.environ['SUPER_SECRET']

# Create .env file to use secrets and import it from credentials.py
# 
# .env
# SUPER_SECRET=bla_bla_bla