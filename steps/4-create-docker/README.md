# Шаг 4. Создание Docker-образа

Скачаем исходные код приложения из репозитория: 

    git clone https://github.com/yandex-cloud-examples/yc-serverless-go-container.git

Создадим docker-образ на его основе:

    docker build . -t cr.yandex/$REGISTRY_ID/logging-server:latest
    docker push cr.yandex/$REGISTRY_ID/logging-server:latest

или можно выполнить одну слитную команду:

    docker build -t cr.yandex/$REGISTRY_ID/logging-server:latest . && docker push cr.yandex/$REGISTRY_ID/logging-server:latest

# Локальное тестирование Docker-образа

Прежде чем запустить наш контейнер в облаке произведем его локальный запуск и тестирвоание. Для начала запустим наш контейнер:

    docker run -p 8080:8080 -e PORT=8080 -e LOG_LEVEL=debug cr.yandex/$REGISTRY_ID/logging-server:latest

Убедитесь, что контейнер запустился, и что доступ к нему не блокируется правилами локального фаервола. 

Произведем тестирование работоспособности, для этого зададим локальную переменную `ENDPOINT`, которой в будущем будем манипулировать:

    echo "export ENDPOINT=http://localhost:8080" >> ~/.bashrc && . ~/.bashrc
    echo $ENDPOINT

    curl -v ${ENDPOINT}/ && echo
    curl -v ${ENDPOINT}/user-error && echo
    curl -v ${ENDPOINT}/internal-error && echo
    curl -v ${ENDPOINT}/not-found && echo

Каждый из вызовов `curl` формирует отдельный запрос, который в будущем будет создавать соответствующие записи в `Cloud Logging`. Если все запросы отработали в штатном режиме следует перейти к следующему пункту.

## Видео

https://youtu.be/kSxJcyRsH4U