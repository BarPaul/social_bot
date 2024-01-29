# Как установить бота?
1. Скопируйте репозиторий командой [Git](https://git-scm.com/downloads) <br>
```
git clone https://github.com/NorthStart-Studio/ITLearning_bot.git
```
3. Перейдите в папку репозитория <br>
```
cd ITLearning_bot
```
5. Создайте файл .env по такому примеру и заполните данными 
```env
TOKEN=""
YOUTUBE_LINK="https://www.youtube.com/"
TIKTOK_LINK="https://tiktok.com"
TG_LINK="https://t.me"
DISCORD_LINK="https://discord.com"
```
<details>
    <summary>Если непонятно куда что писать</summary>
    TOKEN - токен телеграм бота, (Его можно взять у BotFather)<br>
    YOUTUBE, TG, TIKTOK, DISCORD + _LINK - соц. сети <br>
    FULL_PRICE - Цена подписки
</details>
4. Установите необходимые библиотеки командой
<pre lang="cmd">pip install -r requirements.txt</pre>
5. Запустите файл main.py командой (бот написан на <code>Python 3.12</code>, желательно на ней и запускать)
<pre lang="cmd">python main.py</pre>
<h1>Полный скрипт установки</h1>
<pre lang="cmd">
git clone https://github.com/NorthStart-Studio/ITLearning_bot.git
cd ITLearning_bot
</pre>
настройте файл .env, потом
<pre lang="cmd">
pip install -r requirements.txt
python main.py
</pre>
