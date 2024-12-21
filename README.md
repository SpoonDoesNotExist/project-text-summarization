# Проект по саммаризации текстов

## Установка зависимостей
```bash
pip install -r requirements.txt 
```

## Запуск
```bash
python app.py --host localhost --port 8080
```

## Пример запроса
```bash
curl -X 'POST' \
  'http://0.0.0.0:8000/summarize' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "FastAPI is a high-performance web framework for building HTTP-based service APIs in Python 3.8+. It uses Pydantic and type hints to validate, serialize and deserialize data. FastAPI also automatically generates OpenAPI documentation for APIs built with it. It was first released in 2018. Wikipedia",
  "max_length": 130,
  "min_length": 30,
  "do_sample": true
}'
```