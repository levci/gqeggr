class Addresses:
    btc = '`bc1qth4ua6eetqkme5g947jqgxne7phxxqdptf35f2`'
    eth = '`0x751a9bE56edEfdCEdc3b9f04FaFFAF20f7A927D7`'
    sol = '`yvB9Zfw9KPNentD1TG1ZTGZZEiJyZX42BgXuBov5E8X`'
    trx = '`TWdvw25fWeEesKfm2mg3NtuqXw5YFwZkAB`'
    mono = 'https://send.monobank.ua/jar/8Rr3WquUNF'
    bmc = 'https://www.buymeacoffee.com/YSDbot'

addresses = Addresses()
lang = {
    'en': {
        'name': 'English',
        'hello': 'Hi👋\nI can download music, playlist, album from Youtube, Spotify & Deezer.\nI can also change song\'s metatag.\n\nP.S. Subscribe to @just_another_day_with_music to remove watermark. 😉',
        'inline': 'Hi 👋\nI can work inline, for this in any chat write "@YouTube_Spotify_Deezer_Bot *" (instead of * enter your search) and I will download this song for you. \n\nFor example: "@YouTube_Spotify_Deezer_Bot The Beatles"',
        'shazam': 'Hello!👋\nI recognize melodies. Send me a 5-10 second audio message or video message. 😊',

        'donate': f'Dear user, if you want to support the development of the bot, you can donate money via: \n\nBitcoin (BTC): `{addresses.btc}` \n\nEthereum (ERC20/BEP20): {addresses.eth} \n\nSolana: {addresses.sol} \n\nTRX/USDT (TRC20): {addresses.trx}\n\nPay By Card (Visa/MasterCard): {addresses.mono} \n\nBuy Me A Coffee: {addresses.bmc} \n\nThanks for your support ❤️, we will continue to support the bot and improve it.',

        'feedback': 'If you have any requests regarding the bot\'s work, write to me @JADWM',
        'shazam_answers': ['An incomparable track! But I can\'t find it 😔', 'It\'s rare to listen to this kind of music. Unfortunately, I cannot find it in my directory. 🥲', 'Extraordinary and rare music, but I cannot find it. 😩'],
        'processing': 'Processing...',
        'search_results': ['Results on request', 'Page'],
        'audio_soon': 'Audio will be here soon.\nWait for the download.\n\nPosition',
        'sww': 'Something went wrong. 😩',
        'downloaded': 'Downloaded ✅',
        'pos_queue': 'Position in the queue',
        'pos_current': 'Current position',
        'access': 'I\'m so sorry 😔\nBut this feature is <b>only</b> for @just_another_day_with_music subscribers.\nSo subscribe and you can use it too 😉\n\nP.S. Then resend link',
        'ncbf': '<b>Nothing could be found</b> 😞',
        'metaKey': ["Change title", "Change artist", "Change cover", "Cut audio", 'Get cover', "Auto Naming", "Shazam it!", "Done"],
        'action': 'Select an action',
        'metatag_answers': ['Submit a new song title', 'Submit a new artist', 'Submit a new cover for the song', 'Enter a new interval for the song\nFor example: 00:17-02:10'],
        'success': 'Successfully ✅',
        'fra': 'Failed to rename automatically',
        'artTitle': ['Artist', 'Title', 'Song'],
        'ugc': 'Unable to get cover',
        'cantDownload': 'Sorry, I can\'t download this song 😞',
        'albumLimit': 'Currently, the number of songs in the album to download is limited to 50. In the future, we will definitely increase this limit',
        'playlistLimit': 'Currently, the number of songs in the playlist to download is limited to 50. In the future, we will definitely increase this limit',
        'startDownload': 'Started downloading...',
        'download': 'Download',
        'spam_limit': '<b>WARNING!</b>\nThe bot has reached its message limit, please wait 60 seconds!'
    },

    'fr': {
        'name': 'Français',
        'hello': 'Salut👋\nJe peux télécharger de la musique, une liste de lecture, un album depuis Youtube, Spotify et Deezer.\nJe peux également changer le metatag de la chanson.\n\nP.S. Abonnez-vous à @just_another_day_with_music pour supprimer le filigrane. 😉',
        'inline': 'Salut 👋\nJe peux travailler en ligne, pour cela dans n\'importe quel chat écrivez "@YouTube_Spotify_Deezer_Bot *" (au lieu de * entrez votre recherche) et je téléchargerai cette chanson pour vous. \n\nPar exemple : "@YouTube_Spotify_Deezer_Bot The Beatles"',
        'shazam': 'Bonjour !👋\nJe reconnais les mélodies. Envoyez-moi un message audio ou un message vidéo de 5 à 10 secondes. 😊',

        'donate': f'Cher utilisateur, si vous souhaitez soutenir le développement du bot, vous pouvez faire un don via: \n\nBitcoin (BTC): `{addresses.btc}` \n\nEthereum (ERC20/BEP20): {addresses.eth} \n\nSolana: {addresses.sol} \n\nTRX/USDT (TRC20): {addresses.trx}\n\nPay By Card (Visa/MasterCard): {addresses.mono} \n\nBuy Me A Coffee: {addresses.bmc} \n\nMerci pour votre soutien ❤️, nous continuerons à soutenir le bot et à l\'améliorer.',

        'feedback': 'Si vous avez des demandes concernant le travail du bot, écrivez-moi @JADWM',
        'shazam_answers': ['Un titre incomparable! Mais je ne la trouve pas 😔', 'C\'est rare d\'écouter ce genre de musique. Malheureusement, je ne le trouve pas dans mon répertoire. 🥲', 'Musique extraordinaire et rare, mais je ne la trouve pas. 😩'],
        'processing': 'Traitement en cours...',
        'search_results': ['Résultats sur demande', 'Page'],
        'audio_soon': 'L\'audio sera bientôt là.\nAttendez le téléchargement.\n\nPosition',
        'sww': 'Quelque chose s\'est mal passé. 😩',
        'downloaded': 'Téléchargé ✅',
        'pos_queue': 'Position dans la file d\'attente',
        'pos_current': 'Position actuelle',
        'access': 'Je suis vraiment désolé 😔\nMais cette fonctionnalité est <b>uniquement</b> pour les abonnés @just_another_day_with_music.\nAlors abonnez-vous et vous pourrez également l\'utiliser 😉\n\nP.S. Puis renvoyez le lien',
        'ncbf': '<b>Rien n\'a été trouvé</b> 😞',
        'metaKey': ["Changer de titre", "Changer d'artiste", "Changer de couverture", "Couper l'audio", 'Obtenir une couverture', "Auto Naming", "Shazam it!", "Done"],
        'action': 'Sélectionner une action',
        'metatag_answers': ['Soumettre un nouveau titre de chanson', 'Soumettre un nouvel artiste', 'Soumettre une nouvelle couverture pour la chanson', 'Entrez un nouvel intervalle pour la chanson\nPar exemple: 00:17-02:10' ],
        'success': 'Avec succès ✅',
        'fra': 'Échec du renommage automatique',
        'artTitle': ['Artiste', 'Titre', 'Chanson'],
        'ugc': 'Impossible de se mettre à couvert',
        'cantDownload': 'Désolé, je ne peux pas télécharger cette chanson 😞',
        'albumLimit': 'Actuellement, le nombre de chansons de l\'album à télécharger est limité à 50. À l\'avenir, nous allons certainement augmenter cette limite',
        'playlistLimit': 'Actuellement, le nombre de chansons dans la playlist à télécharger est limité à 50. À l\'avenir, nous allons certainement augmenter cette limite',
        'startDownload': 'Téléchargement lancé...',
        'download': 'Télécharger',
        'spam_limit': '<b>ATTENTION !</b>\nLe bot a atteint sa limite de messages, veuillez patienter 60 secondes !'
    },

    'es': {
        'name': 'Español',
        'hello': 'Hola👋\nPuedo descargar música, listas de reproducción, álbumes de Youtube, Spotify y Deezer.\nTambién puedo cambiar la metaetiqueta de la canción.\n\nP.D. Suscríbete a @just_another_day_with_music para eliminar la marca de agua. 😉',
        'inline': 'Hola 👋\nPuedo trabajar en línea, para esto en cualquier chat escribe "@YouTube_Spotify_Deezer_Bot *" (en lugar de * ingresa tu búsqueda) y descargaré esta canción para ti. \n\nPor ejemplo: "@YouTube_Spotify_Deezer_Bot Los Beatles"',
        'shazam': '¡Hola!👋\nReconozco melodías. Envíame un mensaje de audio o un mensaje de video de 5 a 10 segundos. 😊',

        'donate': f'Estimado usuario, si desea apoyar el desarrollo del bot, puede donar dinero a través de: \n\nBitcoin (BTC): `{addresses.btc}` \n\nEthereum (ERC20/BEP20): {addresses.eth} \n\nSolana: {addresses.sol} \n\nTRX/USDT (TRC20): {addresses.trx}\n\nPay By Card (Visa/MasterCard): {addresses.mono} \n\nBuy Me A Coffee: {addresses.bmc} \n\nGracias por su apoyo ❤️, continuaremos apoyando el bot y mejorándolo.',

        'feedback': 'Si tiene alguna solicitud con respecto al trabajo del bot, escríbame @JADWM',
        'shazam_answers': ['¡Una pista incomparable! Pero no puedo encontrarlo 😔', 'Es raro escuchar este tipo de música. Desafortunadamente, no puedo encontrarlo en mi directorio. 🥲', 'Música extraordinaria y rara, pero no la encuentro. 😩'],
        'processing': 'Procesando...',
        'search_results': ['Resultados a pedido', 'Página'],
        'audio_soon': 'El audio estará aquí pronto.\nEspere la descarga.\n\nPosición',
        'sww': ' Algo salió mal.😩',
        'downloaded': 'Descargado ✅',
        'pos_queue': 'Posición en la cola',
        'pos_current': 'Posición actual',
        'access': 'Lo siento mucho 😔\n Pero esta función es <b>solo</b> para los suscriptores de @just_another_day_with_music.\nAsí que suscríbete y tú también puedes usarlo 😉\n\nP.D. Luego reenviar enlace',
        'ncbf': '<b>No se pudo encontrar nada</b> 😞',
        'metaKey': ["Cambiar título", "Cambiar artista", "Cambiar portada", "Cortar audio", 'Obtener portada', "Auto Naming", "Shazam it!", "Listo"],
        'action': 'Seleccione una acción',
        'metatag_answers': ['Envíe un nuevo título de canción', 'Envíe un nuevo artista', 'Envíe una nueva versión de la canción', 'Ingrese un nuevo intervalo para la canción\nPor ejemplo: 00:17-02:10' ],
        'success': 'Con éxito ✅',
        'fra': 'No se pudo cambiar el nombre automáticamente',
        'artTitle': ['Artista', 'Título', 'Canción'],
        'ugc': 'No se pudo cubrir',
        'cantDownload': 'Lo siento, no puedo descargar esta canción 😞',
        'albumLimit': 'Actualmente, la cantidad de canciones en el álbum para descargar está limitada a 50. En el futuro, definitivamente aumentaremos este límite',
        'playlistLimit': 'Actualmente, la cantidad de canciones en la lista de reproducción para descargar está limitada a 50. En el futuro, definitivamente aumentaremos este límite',
        'startDownload': 'Comenzó a descargar...',
        'download': 'Descargar',
        'spam_limit': '<b>¡ADVERTENCIA!</b>\nEl bot ha alcanzado su límite de mensajes, ¡espere 60 segundos!'
    },

    'pt': {
        'name': 'Português',
        'hello': 'Oi👋\nPosso baixar músicas, playlists, álbuns do Youtube, Spotify e Deezer.\nTambém posso alterar a metatag da música.\n\nP.S. Inscreva-se em @just_another_day_with_music para remover a marca d\'água. 😉',
        'inline': 'Oi 👋\nEu posso trabalhar inline, para isso em qualquer chat escreva "@YouTube_Spotify_Deezer_Bot *" (em vez de * digite sua pesquisa) e eu vou baixar essa música para você. \n\nPor exemplo: "@YouTube_Spotify_Deezer_Bot The Beatles"',
        'shazam': 'Olá!👋\nReconheço melodias. Envie-me uma mensagem de áudio ou mensagem de vídeo de 5 a 10 segundos. 😊',

        'donate': f'Caro usuário, se você deseja apoiar o desenvolvimento do bot, você pode doar dinheiro via: \n\nBitcoin (BTC): `{addresses.btc}` \n\nEthereum (ERC20/BEP20): {addresses.eth} \n\nSolana: {addresses.sol} \n\nTRX/USDT (TRC20): {addresses.trx}\n\nPay By Card (Visa/MasterCard): {addresses.mono} \n\nBuy Me A Coffee: {addresses.bmc} \n\nObrigado pelo seu apoio ❤️, continuaremos a apoiar o bot e a melhorá-lo.',

        'feedback': 'Se você tiver alguma solicitação sobre o trabalho do bot, escreva para mim @JADWM',
        'shazam_answers': ['Uma trilha incomparável! Mas não consigo achar 😔', 'É raro ouvir este tipo de música. Infelizmente, não consigo encontrá-lo no meu diretório. 🥲', 'Música extraordinária e rara, mas não consigo encontrá-la. 😩'],
        'processing': 'Em processamento...',
        'search_results': ['Resultados a pedido', 'Página'],
        'audio_soon': 'O áudio estará aqui em breve.\nAguarde o download.\n\nPosição',
        'sww': 'Algo deu errado. 😩',
        'downloaded': 'Baixado ✅',
        'pos_queue': 'Posição na fila',
        'pos_current': 'Posição atual',
        'access': 'Sinto muito 😔\nMas esse recurso é <b>somente</b> para assinantes do @just_another_day_with_music.\nEntão se inscreva e você também pode usar 😉\n\nP.S. Em seguida, reenvie o link',
        'ncbf': '<b>Nada pôde ser encontrado</b> 😞',
        'metaKey': ["Alterar título", "Alterar artista", "Alterar capa", "Cut audio", 'Cortar áudio', "Nomeação automática", "Shazam isso!", "Feito"],
        'action': 'Selecione uma ação',
        'metatag_answers': ['Envie um novo título de música', 'Envie um novo artista', 'Envie um novo cover para a música', 'Digite um novo intervalo para a música\nPor exemplo: 00:17-02:10'],
        'success': 'Com sucesso ✅',
        'fra': 'Falha ao renomear automaticamente',
        'artTitle': ['Artista', 'Título', 'Canção'],
        'ugc': 'Não foi possível obter cobertura',
        'cantDownload': 'Desculpe, não consigo baixar essa música 😞',
        'albumLimit': 'Atualmente, o número de músicas do álbum para download é limitado a 50. No futuro, definitivamente aumentaremos esse limite',
        'playlistLimit': 'Atualmente, o número de músicas na playlist para download é limitado a 50. No futuro, definitivamente aumentaremos esse limite',
        'startDownload': 'Download iniciado...',
        'download': 'Download',
        'spam_limit': '<b>AVISO!</b>\nO bot atingiu seu limite de mensagens, aguarde 60 segundos!'
    },

    'ru': {
        'name': 'Русский',
        'hello': 'Здравствуйте👋\nЯ могу скачать музыку, плейлист, альбом с Youtube, Spotify и Deezer.\nЯ также могу изменить метатег песни.\n\nP.S. Подпишитесь на @just_another_day_with_music, чтобы удалить водяной знак. 😉',
        'inline': 'Привет 👋\nЯ могу работать в инлайн режиме, для этого в любом чате напиши "@YouTube_Spotify_Deezer_Bot *" (Без кавычек и вместо * свой запрос) и я покажу тебе список доступных аудиозаписей для скачивания, где ты сможешь выбрать нужный и скаченный . \n\nПример использования: "@YouTube_Spotify_Deezer_Bot The Beatles"',
        'shazam': 'Как дела? 👋\nЯ умею распознавать мелодии. Для этого отправь мне аудио/видеозапись и я пришлю тебе название песни, которая там будет играть.',

        'donate': f'Дорогой пользователь, если желаешь поддержать дальнейшую разработку и функционирование бота, можешь использовать следующие методы для пожертвования: \n\nBitcoin (BTC): {addresses.btc} \n\nEthereum (ERC20/BEP20): {addresses.eth} \n\nSolana: {addresses.sol} \n\nTRX/USDT (TRC20): {addresses.trx}\n\nMonobank (Visa/MasterCard): {addresses.mono} \n\nBuy Me A Coffee: {addresses.bmc} \n\nСпасибо за поддержку ❤️, мы будем в дальнейшем совершенствовать бота.',
        'feedback': 'Если у вас есть какие-то пожелания, по работе бота пишите мне @JADWM',
        'shazam_answers': ['Бесподобный трек! Но я не могу его найти 😔', 'Такую музыку услышишь не часто. К сожалению, я не могу ее найти в своей базе. 🥲", "Непревзойденная и редкая музыка, но я не могу ее найти. 😩'],
        'processing': 'Обработка...',
        'search_results': ['Результаты по запросу', 'Страница'],
        'audio_soon': 'Музыка скоро скачается.\nПожалуйста, подождите.\n\nПозиция',
        'sww': 'Что-то пошло не так. Вот беда 😩',
        'downloaded': 'Загружено ✅',
        'pos_queue': 'Позиция в очереди',
        'pos_current': 'Текущая позиция',
        'access': 'Мне очень жаль 😔\nНо эта функция <b>только</b> для подписчиков @just_another_day_with_music.\nТак что подпишитесь, и вы тоже сможете ею пользоваться 😉\n\nP.S. Затем повторно пришлите ссылку',
        'ncbf': '<b>Ничего не найдено</b> 😞',
        'metaKey': ["Сменить название", "Сменить исполнителя", "Сменить обложку", "Обрезать аудио", 'Получить обложку', "Автонейминг", "Зашазамите это!", "Готово ✅"],
        'action': 'Пожалуйста выберите действие',
        'metatag_answers': ['Напишите новое название', 'Напишите нового исполнителя', 'Отправьте новую обложку', 'Введите новый интервал песни\nДля примера: 00:17-02:10'],
        'success': 'Успешно ✅',
        'fra': 'Не удалось автоматически переименовать',
        'artTitle': ['Исполнитель', 'Название', 'Песня'],
        'ugc': 'Невозможно получить обложку',
        'cantDownload': 'Извините, я не могу скачать эту песню 😞',
        'albumLimit': 'В настоящее время количество песен в альбоме для скачивания ограничено 50. В будущем мы обязательно увеличим этот лимит.',
        'playlistLimit': 'В настоящее время количество песен в плейлисте для загрузки ограничено 50. В будущем мы обязательно увеличим этот лимит.',
        'startDownload': 'Начал скачивать 😉',
        'download': 'Загрузить',
        'spam_limit': '<b>ВНИМАНИЕ!</b>\nБот достиг лимита сообщений, подождите 60 секунд!'
    },

    'uk': {
        'name': "Українська",
        'hello': 'Привіт👋\nЯ допоможу тобі скачати музику, плейлисти, а також альбоми з таких сервісів, як Youtube, Spotify та Deezer.\nЯ також вмію міняти метадані пісень. \n\nПідпишись на @just_another_day_with_music, щоб забрати водяний знак з повідомлень. 😉',
        'inline': 'Хай 👋\nЯ можу працювати в інлайн режимі, для цього в будь-якому чаті напиши "@YouTube_Spotify_Deezer_Bot *" (Без лапок і замість * свій запит) і я покажу тобі список доступних аудіозаписів для скачування, де ти зможеш вибрати потрібний і скачати. \n\nПриклад використання: "@YouTube_Spotify_Deezer_Bot The Beatles"',
        'shazam': 'Як ся маєш? 👋\nЯ вмію розпізнавати мелодії. Для цього відправ мені аудіо-/відеозапис і я надішлю тобі назву пісні, яка там буде грати. 😊',

        'donate': f'Дорогий користувач, якщо бажаєш підтримати подальшу розробку і функціонування бота, то можеш використовувати наступні методи для пожертвування: \n\nMonobank: {addresses.mono} \n\nBitcoin (BTC): {addresses.btc} \n\nEthereum (ERC20/BEP20): {addresses.eth} \n\nSolana: {addresses.sol} \n\nTRX/USDT (TRC20): {addresses.trx}\n\nBuy Me A Coffee: {addresses.bmc} \n\nДякую за підтримку ❤️, ми надалі будемо вдосконалювати бота.',
        'feedback': 'Якщо маєте якісь побажання, щодо роботи бота пишіть мені @JADWM ',
        'shazam_answers': ['Незрівнянний трек! Але я не можу його знайти 😔', 'Таку музику почуєш не часто. На жаль, я не можу знайти її в своїй базі. 🥲", "Неперевершена та рідкісна музика, але я не можу її знайти. 😩'],
        'processing': 'Обробка запиту...',
        'search_results': ['Результати на запит', 'Сторінка'],
        'audio_soon': 'Музика скоро скачається.\nБудь-ласка зачекайте.\n\nПозиція',
        'sww': 'Щось пішло не так. От халепа 😩',
        'downloaded': 'Завантажено ✅',
        'pos_queue': 'Позиція в черзі',
        'pos_current': 'Поточна позиція',
        'access': 'Мені дуже-дуже шкода 😔\nАле цей функціонал <b>тільки</b> для підписників @just_another_day_with_music.\nТож підпишись, щоб і ти міг його використовувати. 😉\n\nP.S. А після того відправ мені посилання ще раз',
        'ncbf': '<b>Нажаль я нічого не зміг знайти</b> 😞',
        'metaKey': ["Змінити назву", "Змінити виконавця", "Змінити обкладинку", "Обрізати аудіо", 'Отримати обкладинку', "Авто-неймінг", "Зашазамити це!", "Готово ✅"],
        'action': 'Будь ласка оберіть дію',
        'metatag_answers': ['Напишіть нову назву', 'Напишіть нового виконавця', 'Відправте нову обкладинку', 'Введіть новий інтервал пісні\nДля прикладу: 00:17-02:10'],
        'success': 'Успішно ✅',
        'fra': 'Не вдалось провести авто-неймінг',
        'artTitle': ['Виконавець', 'Назва', 'Пісня'],
        'ugc': 'Неможливо отримати обкладинку',
        'cantDownload': 'Я вибачаюсь, але мені не вдалось скачати цю пісню 😞',
        'albumLimit': 'На даний момент кількість пісень в альбомі для скачування обмежена в 50 одиниць. У майбутньому ми обовʼязково збільшимо цей ліміт.',
        'playlistLimit': 'На даний момент кількість пісень в плейлисті для скачування обмежена в 50 одиниць. У майбутньому ми обовʼязково збільшимо цей ліміт.',
        'startDownload': 'Почав скачувати 😉',
        'download': 'Завантажити',
        'spam_limit': '<b>⚠️ УВАГА! ⚠️</b>\nВиглядає, що ви відправили забагато повідомлень, зачекайте 60 секунд, щоб мати можливість далі користуватися ботом!'
        
    }
}



def getUserLang(update) -> dict:
    '''
    Return language_dictionary for user's language. If the language is not found, the default English will be returned
    '''
    query = update.message or update.callback_query or update.chosen_inline_result or update.inline_query
    from_user = query.from_user or query.message.from_user
    language_code = from_user.language_code
    language_code = language_code if language_code in lang else 'en'
    return lang[language_code]