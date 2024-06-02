# HakatonDVFU КиберМужики
Создание визуальной поддержки по текстовому описанию
<h2>Что нужно сделать:</h2>
<ol>
  <li>Зарегистрироваться на сайте Fusion Brain, и получить API-ключ на сайте: https://auth.fusionbrain.ai/realms/FB/protocol/openid-connect/auth?client_id=fusion-web-mobile&redirect_uri=https%3A%2F%2Fm.fusionbrain.ai%2Fkeys%2F&state=a290e432-74e3-4108-8d5f-b8c263d830e5&response_mode=fragment&response_type=code&scope=openid&nonce=950e10e7-d993-4548-80d1-7f2bdd2ef2b8</li>
  <li>В файле model.py необходимо необходимо найти строку в классе Text2ImageAPI: "self.AUTH_HEADERS" и  добавить туда свой ключ.</li>
  <li>Установить python версии 3.10, pip 23.0.1</li>
  <li>Затем необходимо установить необходимые библиотеки:
      <ul>
        <li>python-pptx</li>
        <li>spacy</li>
        <li>python -m spacy download ru_core_news_sm</li>
        <li>python-pptx 0.6.23</li>
        <li>qrcode</li>
        <li>imagecolor</li>
        <li>customtkinter 5.2.2</li>
        <li>colorthief 0.2.1</li>
      </ul>
   </li>
<li>открыть терминал, перейти в каталог проекта и запустить файл Main.py</li>
</ol>
