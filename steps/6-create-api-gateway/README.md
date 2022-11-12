# Шаг 6. Создание экземпляра Yandex API Gateway
## Изменение спецификации

В директории вы найдете файл `logging-server-apigw.yaml`, который нужно изменить:
1. Добавить после `container_id:` ID сервис контейнера, созданного на предыдущем шаге.
2. Добавить после `service_account_id:` ID сервисного аккаунта, созданного на шаге и записанного в переменную `$SERVICE_ACCOUNT_ID`.

После внесения изменений можно выполнить команду для создания экземпляра Yandex API Gateway:

    yc serverless api-gateway create \
    --name logging-server-apigw \
    --spec=logging-server-apigw.yaml \
    --description "logging server apigw"

## Тестирование записей в Cloud Logging

После того как экземпляр `Yandex API Gateway` развернётся, мы можем получить служебный домен, чтобы проверить работоспособность API-шлюза, контейнера и развёрнутого в нем приложения:

    yc serverless api-gateway list
    yc serverless api-gateway get --name logging-server-apigw

Технический домен будет выглядить примерно так: `https://<ID API Gateway>.apigw.yandexcloud.net`. Обновите переменную `ENDPOINT` и проведите тестирование:

    echo "export ENDPOINT=https://<ID API Gateway>.apigw.yandexcloud.net" >> ~/.bashrc && . ~/.bashrc
    echo $ENDPOINT

    curl -v ${ENDPOINT}/ && echo
    curl -v ${ENDPOINT}/user-error && echo
    curl -v ${ENDPOINT}/internal-error && echo
    curl -v ${ENDPOINT}/not-found && echo

Каждый из вызовов `curl` формирует отдельный запрос, который создаёт соответствующие записи в `Cloud Logging` в лог-группе `default`. Если все запросы отработали, можно смело смотреть результат:

    yc logging read --group-name=default --format=json

Переходите к следующему шагу.

## Видео

https://youtu.be/nXjC7AijyoY