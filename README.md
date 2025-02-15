# my-discord-bot-boilerplate
This boilerplate is designed for scalability, maintainability, and seamless integration between Discord Bot and FastAPI, using SQLAlchemy and Alembic for database control.
- This include slash commands in cogs

## Update procedure
1. Modify your SQLAlchemy models (models.py).
2. Run alembic revision --autogenerate -m "describe changes" to detect model changes.
3. Run alembic upgrade head to apply the migrations.