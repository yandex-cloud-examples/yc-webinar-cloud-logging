# Шаг 8. Удаление ресурсов

По завершению работы удалите все используемые вами ресурсы.

Удалите экземпляр COI и дополнительную лог-группу:

    yc compute instance delete --name=coi-vm
    yc serverless container delete --name=logging-server
    yc logging group delete --name=yc-logging

Удалите Doker-образ и репозиторий:

    yc container image list
    yc container image delete --id=<ID>
    yc container registry delete --name=for-logging-server

Удалите экземпляр функцию и API-Gateway:

    yc serverless api-gateway list
    yc serverless api-gateway delete --name=logging-server-apigw

    yc serverless function list
    yc serverless function delete --name=function-for-cloud-logging

Если вы создавали отдельную сеть с подсетями, то сначала удалите все подсети, а потом сеть:

    yc vpc subnet list
    yc vpc subnet delete --name=<NAME>
    
    yc vpc network list
    yc vpc network delete --name=<NAME>

Удалите сервисный аккаунт:

    yc iam service-account delete --id $SERVICE_ACCOUNT_ID