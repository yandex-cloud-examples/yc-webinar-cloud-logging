# Шаг 3. Создание экземпляра Container Registry

Для демонстрации работы `Cloud Logging` с `Serverless Container` и `COI` нам необходимо создать репозиторий для размещения нашего Docker-образа. Создадим простой репозиторий `for-logging-server`:

    yc container registry create --name for-logging-server
    yc container registry configure-docker

В выводе команды нам потребуется `ID` вновь созданного репозитория:

    echo "export REGISTRY_ID=<ID>" >> ~/.bashrc && . ~/.bashrc
    echo $REGISTRY_ID

В дальнейшем в этот репозиторий мы загрузим наш Docker-образ.

## Видео

https://youtu.be/kcbeEvg4XJs