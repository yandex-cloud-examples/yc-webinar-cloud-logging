# Шаг 2. Создание экземпляра Serverless Function

Мы будем использовать версию рантайма `python39` и библиотеки необходиомо указывать явно. Для работы с `requirements.txt` есть удобная python библиотека `pipreqs`. Для генерации `requirements.txt` с помощью `pipreqs` достаточно указать рабочий каталог. В большинстве интерпритаторов linux для указания текущего каталога есть переменная `$PWD`. Если файл `requirements.txt` уже есть и его нужно актуализировать то используется флаг `--force`, например:

    pip install pipreqs
    pipreqs $PWD --print
    pipreqs $PWD --force

Находясь в директории с исходными файлами, упакуем все нужные нам файлы в zip-архив:

    zip src.zip index.py requirements.txt 

Создадим нашу функцию `function-for-cloud-logging`, при этом сразу зададим сервисный аккаунт:

    yc serverless function create \
    --name function-for-cloud-logging \
    --description "function function-for-cloud-logging for cloud clogging example"

    yc serverless function version create \
    --function-name function-for-cloud-logging \
    --memory=128m \
    --execution-timeout=5s \
    --runtime=python39 \
    --entrypoint=index.handler \
    --service-account-id $SERVICE_ACCOUNT_ID \
    --source-path src.zip

    yc serverless function allow-unauthenticated-invoke function-for-cloud-logging

Если вызвать нашу функцию, то в `Cloud Logging` мы получим соответствующие записи после исполнения методов `logger.info`, `logger.error`, `logger.debug`. При этом записи будут структурированные и вы можете самостоятельно с помощью `extra` расширить содержимое `json` записи.

Каждый из вызовов функции формирует ряд записей, по умолчанию, в лог-группе с именем `default`, и мы можем посмотреть их:

    yc logging read --group-name=default --format=json

Далее следует перейти к следующему пункту.

## Видео

https://youtu.be/zdlnYEfaBhM