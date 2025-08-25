## ls no terminal somente powershell ele é sempre melhor que o cmd porque aceita mais atalhos e comandos.

criando um ambiente virtual    ou seja, tudo o que você baixar instalar e criar ficará isolado nesse ambiente

python -m venv ll_env    ((ll é learning_log))

para mudar a pasta é o comando cd e o caminho


No PowerShell, o . é chamado de “dot sourcing”.
Ele serve pra executar um script no contexto atual
. ll_env/Scripts/activate


se o power shell bloquear, abra como adm e execute

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

toda vez que entrar em um projeto precisa lembrar de ativar o projeto virtual

pip install Django

django-admin --version   (para ver a versão atual do seu django instalado)


para criar um projeto é 

django-admin startproject learning_log .     (o . é para organizar as pastas de uma forma boa)  (learning_log é o nome do projeto)

para criar um banco de dados basico é 

python manage.py migrate 

para dar run no server
python manage.py runserver







