docker compose run --rm notifier python main.py --test

docker compose run --rm notifier python -m tests.publish_test_message

Пока что здесь просто набросаны сообщения, по которым пробегаются

Есть небольшой задел на юнит-тесты, если захочется. Но пока так

Изменение крайне возможно