# Реализация консольного приложения, которое устанавливает PostgreSQL на удаленный хост через ssh

### Теория
Paramiko — этот модуль реализует ssh2 протокол для защищенного (с шифрованием и аутентификацией) соединения с удаленным компьютером. При подключении предоставляется высокоуровневое API для работы с ssh — создается объект SSHClient.

###  Настройка рабочего окружения для запуска скрипта
1. Установите необходимые библиотеки
```
pip3 install paramiko
```

2. Запуск
```
python3 main.py <hostname>
```

### Литература

[Модуль paramiko](https://pyneng.readthedocs.io/ru/latest/book/18_ssh_telnet/paramiko.html)
