# Шаг 5. Создание Serverless Container из Docker-образа

Создадим контейнер в сервисе `Serverless Container` с именем `logging-server`:

    echo "export SERVERLESS_CONTAINER_NAME=logging-server" >> ~/.bashrc && . ~/.bashrc
    echo $SERVERLESS_CONTAINER_NAME

    yc serverless container create --name $SERVERLESS_CONTAINER_NAME
    yc container image list

Составим `URL_Docker-образа`. Возьмем наименование реджестри `cr.yandex`. Добавим значение `NAME` из выведенного ранее списка контейнеров, оно будет иметь вид `crp8ei5vkhh11pc7pd8h/logging-server`. Добавим значение `TAGS`, скорее всего, оно будет равно `latest`. Получившаяся строка вида `cr.yandex/crp8ei5vkhh11pc7pd8h/logging-server:latest` будет вашим URL (ранее мы уже использовали такой URL).

    echo "export URL_IMAGE=YOUR_URL_IMAGE" >> ~/.bashrc && . ~/.bashrc
    echo $URL_IMAGE

Развернём наш контейнер:

    yc serverless container revision deploy \
    --container-name $SERVERLESS_CONTAINER_NAME \
    --image $URL_IMAGE \
    --cores 1 \
    --memory 128MB \
    --concurrency 1 \
    --execution-timeout 30s \
    --service-account-id $SERVICE_ACCOUNT_ID \
    --environment LOG_LEVEL=debug

Проверим список `Serverless Container` и запишем ID созданного контейнера (он нам понадобится при создании `Yandex API Gateway`).

    yc serverless container list

## Видео

https://youtu.be/hN8I99J5wW4