Приложение сделано на Flask. Частично ручками, частично навайбкожено

## Для запуска

```bash
python3 -m pip install -r requirements.txt
python3 scripts/init_db.py
python3 src/webapp.py
```

По-умолчанию подрубает по: `http://127.0.0.1:5000/login`

## Линтер

```bash
python3 -m flake8 src scripts
```

