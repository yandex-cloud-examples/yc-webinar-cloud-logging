# Шаг 1. Создание Service Account
## Создание сервисного аккаунта

Создайте сервисный аккаунт с именем `service-account-for-logging-server`:

    export SERVICE_ACCOUNT=$(yc iam service-account create \
    --name service-account-for-logging-server \
    --description "service account for logging server" \
    --format json | jq -r .)

Проверьте текущий список сервисных аккаунтов:

    yc iam service-account list
    echo $SERVICE_ACCOUNT

После проверки запишите ID, созданного сервисного аккаунта, в переменную `SERVICE_ACCOUNT_ID`:

    echo "export SERVICE_ACCOUNT_ID=<ID>" >> ~/.bashrc && . ~/.bashrc 
    echo $SERVICE_ACCOUNT_ID

## Назначение роли сервисному аккаунту

Добавим вновь созданному сервисному аккаунту необходимые роли `logging.writer`, `container-registry.images.puller`, `serverless.functions.invoker`, `serverless.containers.invoker`: 

    echo "export FOLDER_ID=$(yc config get folder-id)" >> ~/.bashrc && . ~/.bashrc
    echo $FOLDER_ID

    yc resource-manager folder add-access-binding $FOLDER_ID \
    --subject serviceAccount:$SERVICE_ACCOUNT_ID \
    --role logging.writer

    yc resource-manager folder add-access-binding $FOLDER_ID \
    --subject serviceAccount:$SERVICE_ACCOUNT_ID \
    --role serverless.containers.invoker

    yc resource-manager folder add-access-binding $FOLDER_ID \
    --subject serviceAccount:$SERVICE_ACCOUNT_ID \
    --role serverless.functions.invoker

    yc resource-manager folder add-access-binding $FOLDER_ID \
    --subject serviceAccount:$SERVICE_ACCOUNT_ID \
    --role container-registry.images.puller

Все перечисленные роли можно заменить ролью `editor`:

    yc resource-manager folder add-access-binding $FOLDER_ID \
    --subject serviceAccount:$SERVICE_ACCOUNT_ID \
    --role editor

## Видео

https://youtu.be/kgeTS2spO1Y