# Шаг 4. Создание Docker-образа

Скачай исходный код приложения из репозитория:

    git clone https://github.com/yandex-cloud-examples/yc-serverless-go-container.git

Создай Docker-образ на его основе:

    docker build . -t cr.yandex/$REGISTRY_ID/logging-server:latest
    docker push cr.yandex/$REGISTRY_ID/logging-server:latest

или можно выполнить одну слитную команду:

    docker build -t cr.yandex/$REGISTRY_ID/logging-server:latest . && docker push cr.yandex/$REGISTRY_ID/logging-server:latest

# Локальное тестирование Docker-образа

Прежде чем запустить наш контейнер в облаке, запустим его локально и протестируем. Запускаем контейнер:

    docker run -p 8080:8080 -e PORT=8080 -e LOG_LEVEL=debug cr.yandex/$REGISTRY_ID/logging-server:latest

Убедитесь, что контейнер запустился и доступ к нему не блокируется правилами локального файрвола.

Чтобы протестировать работоспособность, зададим локальную переменную `ENDPOINT`, которой будем манипулировать:

    echo "export ENDPOINT=http://localhost:8080" >> ~/.bashrc && . ~/.bashrc
    echo $ENDPOINT

    curl -v ${ENDPOINT}/ && echo
    curl -v ${ENDPOINT}/user-error && echo
    curl -v ${ENDPOINT}/internal-error && echo
    curl -v ${ENDPOINT}/not-found && echo

Каждый из вызовов `curl` формирует отдельный запрос, который будет создавать соответствующие записи в `Cloud Logging`. Если все запросы отработали в штатном режиме, переходим к следующему пункту.

## Видео

https://youtu.be/kSxJcyRsH4U