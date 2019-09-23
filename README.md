# api-test-sample

Pytest + allure  api tests sample for http://data.fixer.io/

Service source: https://github.com/fixerAPI/fixer

Install requirements:
```
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt 
```

Run tests with Selenium Hub:
```
pytest tests --alluredir ./alluredir
```