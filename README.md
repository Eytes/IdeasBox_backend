![lining and type checking](https://github.com/eytes/IdeasBox_backend/actions/workflows/lining_and_type_checking.yml/badge.svg) ![CI](https://github.com/eytes/IdeasBox_backend/actions/workflows/CI.yml/badge.svg)

# IdeasBox Backend

Бэкенд для проекта IdeasBox

## Локальный запуск

### Самостоятельная сборка образа

1. Сборка образа

```commandline
docker build . -t ideasbox_backend
```

2. Запуск контейнера. Вместо `<host_port>` укажите порт на хосте

```commandline
docker run --rm -d -p <host_port>:8000 ideasbox_backend
```

3. Перейдите в браузере на `http://localhost:<host_port>/`

### Запустить готовый образ

Запуск контейнера. Вместо `<host_port>` укажите порт на хосте

```commandline
docker run --rm -d -p <host_port>:8000 eytes/ideasbox_backend
```