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
        'hello': 'Hið\nI can download music, playlist, album from Youtube, Spotify & Deezer.\nI can also change song\'s metatag.\n\nP.S. Subscribe to @just_another_day_with_music to remove watermark. ð',
        'inline': 'Hi ð\nI can work inline, for this in any chat write "@YouTube_Spotify_Deezer_Bot *" (instead of * enter your search) and I will download this song for you. \n\nFor example: "@YouTube_Spotify_Deezer_Bot The Beatles"',
        'shazam': 'Hello!ð\nI recognize melodies. Send me a 5-10 second audio message or video message. ð',

        'donate': f'Dear user, if you want to support the development of the bot, you can donate money via: \n\nBitcoin (BTC): `{addresses.btc}` \n\nEthereum (ERC20/BEP20): {addresses.eth} \n\nSolana: {addresses.sol} \n\nTRX/USDT (TRC20): {addresses.trx}\n\nPay By Card (Visa/MasterCard): {addresses.mono} \n\nBuy Me A Coffee: {addresses.bmc} \n\nThanks for your support â¤ï¸, we will continue to support the bot and improve it.',

        'feedback': 'If you have any requests regarding the bot\'s work, write to me @JADWM',
        'shazam_answers': ['An incomparable track! But I can\'t find it ð', 'It\'s rare to listen to this kind of music. Unfortunately, I cannot find it in my directory. ð¥²', 'Extraordinary and rare music, but I cannot find it. ð©'],
        'processing': 'Processing...',
        'search_results': ['Results on request', 'Page'],
        'audio_soon': 'Audio will be here soon.\nWait for the download.\n\nPosition',
        'sww': 'Something went wrong. ð©',
        'downloaded': 'Downloaded â',
        'pos_queue': 'Position in the queue',
        'pos_current': 'Current position',
        'access': 'I\'m so sorry ð\nBut this feature is <b>only</b> for @just_another_day_with_music subscribers.\nSo subscribe and you can use it too ð\n\nP.S. Then resend link',
        'ncbf': '<b>Nothing could be found</b> ð',
        'metaKey': ["Change title", "Change artist", "Change cover", "Cut audio", 'Get cover', "Auto Naming", "Shazam it!", "Done"],
        'action': 'Select an action',
        'metatag_answers': ['Submit a new song title', 'Submit a new artist', 'Submit a new cover for the song', 'Enter a new interval for the song\nFor example: 00:17-02:10'],
        'success': 'Successfully â',
        'fra': 'Failed to rename automatically',
        'artTitle': ['Artist', 'Title', 'Song'],
        'ugc': 'Unable to get cover',
        'cantDownload': 'Sorry, I can\'t download this song ð',
        'albumLimit': 'Currently, the number of songs in the album to download is limited to 50. In the future, we will definitely increase this limit',
        'playlistLimit': 'Currently, the number of songs in the playlist to download is limited to 50. In the future, we will definitely increase this limit',
        'startDownload': 'Started downloading...',
        'download': 'Download',
        'spam_limit': '<b>WARNING!</b>\nThe bot has reached its message limit, please wait 60 seconds!'
    },

    'fr': {
        'name': 'FranÃ§ais',
        'hello': 'Salutð\nJe peux tÃ©lÃ©charger de la musique, une liste de lecture, un album depuis Youtube, Spotify et Deezer.\nJe peux Ã©galement changer le metatag de la chanson.\n\nP.S. Abonnez-vous Ã  @just_another_day_with_music pour supprimer le filigrane. ð',
        'inline': 'Salut ð\nJe peux travailler en ligne, pour cela dans n\'importe quel chat Ã©crivez "@YouTube_Spotify_Deezer_Bot *" (au lieu de * entrez votre recherche) et je tÃ©lÃ©chargerai cette chanson pour vous. \n\nPar exempleÂ : "@YouTube_Spotify_Deezer_Bot The Beatles"',
        'shazam': 'BonjourÂ !ð\nJe reconnais les mÃ©lodies. Envoyez-moi un message audio ou un message vidÃ©o de 5 Ã  10 secondes. ð',

        'donate': f'Cher utilisateur, si vous souhaitez soutenir le dÃ©veloppement du bot, vous pouvez faire un don via: \n\nBitcoin (BTC): `{addresses.btc}` \n\nEthereum (ERC20/BEP20): {addresses.eth} \n\nSolana: {addresses.sol} \n\nTRX/USDT (TRC20): {addresses.trx}\n\nPay By Card (Visa/MasterCard): {addresses.mono} \n\nBuy Me A Coffee: {addresses.bmc} \n\nMerci pour votre soutien â¤ï¸, nous continuerons Ã  soutenir le bot et Ã  l\'amÃ©liorer.',

        'feedback': 'Si vous avez des demandes concernant le travail du bot, Ã©crivez-moi @JADWM',
        'shazam_answers': ['Un titre incomparable! Mais je ne la trouve pas ð', 'C\'est rare d\'Ã©couter ce genre de musique. Malheureusement, je ne le trouve pas dans mon rÃ©pertoire. ð¥²', 'Musique extraordinaire et rare, mais je ne la trouve pas. ð©'],
        'processing': 'Traitement en cours...',
        'search_results': ['RÃ©sultats sur demande', 'Page'],
        'audio_soon': 'L\'audio sera bientÃ´t lÃ .\nAttendez le tÃ©lÃ©chargement.\n\nPosition',
        'sww': 'Quelque chose s\'est mal passÃ©. ð©',
        'downloaded': 'TÃ©lÃ©chargÃ© â',
        'pos_queue': 'Position dans la file d\'attente',
        'pos_current': 'Position actuelle',
        'access': 'Je suis vraiment dÃ©solÃ© ð\nMais cette fonctionnalitÃ© est <b>uniquement</b> pour les abonnÃ©s @just_another_day_with_music.\nAlors abonnez-vous et vous pourrez Ã©galement l\'utiliser ð\n\nP.S. Puis renvoyez le lien',
        'ncbf': '<b>Rien n\'a Ã©tÃ© trouvÃ©</b> ð',
        'metaKey': ["Changer de titre", "Changer d'artiste", "Changer de couverture", "Couper l'audio", 'Obtenir une couverture', "Auto Naming", "Shazam it!", "Done"],
        'action': 'SÃ©lectionner une action',
        'metatag_answers': ['Soumettre un nouveau titre de chanson', 'Soumettre un nouvel artiste', 'Soumettre une nouvelle couverture pour la chanson', 'Entrez un nouvel intervalle pour la chanson\nPar exemple: 00:17-02:10' ],
        'success': 'Avec succÃ¨s â',
        'fra': 'Ãchec du renommage automatique',
        'artTitle': ['Artiste', 'Titre', 'Chanson'],
        'ugc': 'Impossible de se mettre Ã  couvert',
        'cantDownload': 'DÃ©solÃ©, je ne peux pas tÃ©lÃ©charger cette chanson ð',
        'albumLimit': 'Actuellement, le nombre de chansons de l\'album Ã  tÃ©lÃ©charger est limitÃ© Ã  50. Ã l\'avenir, nous allons certainement augmenter cette limite',
        'playlistLimit': 'Actuellement, le nombre de chansons dans la playlist Ã  tÃ©lÃ©charger est limitÃ© Ã  50. Ã l\'avenir, nous allons certainement augmenter cette limite',
        'startDownload': 'TÃ©lÃ©chargement lancÃ©...',
        'download': 'TÃ©lÃ©charger',
        'spam_limit': '<b>ATTENTIONÂ !</b>\nLe bot a atteint sa limite de messages, veuillez patienter 60Â secondesÂ !'
    },

    'es': {
        'name': 'EspaÃ±ol',
        'hello': 'Holað\nPuedo descargar mÃºsica, listas de reproducciÃ³n, Ã¡lbumes de Youtube, Spotify y Deezer.\nTambiÃ©n puedo cambiar la metaetiqueta de la canciÃ³n.\n\nP.D. SuscrÃ­bete a @just_another_day_with_music para eliminar la marca de agua. ð',
        'inline': 'Hola ð\nPuedo trabajar en lÃ­nea, para esto en cualquier chat escribe "@YouTube_Spotify_Deezer_Bot *" (en lugar de * ingresa tu bÃºsqueda) y descargarÃ© esta canciÃ³n para ti. \n\nPor ejemplo: "@YouTube_Spotify_Deezer_Bot Los Beatles"',
        'shazam': 'Â¡Hola!ð\nReconozco melodÃ­as. EnvÃ­ame un mensaje de audio o un mensaje de video de 5 a 10 segundos. ð',

        'donate': f'Estimado usuario, si desea apoyar el desarrollo del bot, puede donar dinero a travÃ©s de: \n\nBitcoin (BTC): `{addresses.btc}` \n\nEthereum (ERC20/BEP20): {addresses.eth} \n\nSolana: {addresses.sol} \n\nTRX/USDT (TRC20): {addresses.trx}\n\nPay By Card (Visa/MasterCard): {addresses.mono} \n\nBuy Me A Coffee: {addresses.bmc} \n\nGracias por su apoyo â¤ï¸, continuaremos apoyando el bot y mejorÃ¡ndolo.',

        'feedback': 'Si tiene alguna solicitud con respecto al trabajo del bot, escrÃ­bame @JADWM',
        'shazam_answers': ['Â¡Una pista incomparable! Pero no puedo encontrarlo ð', 'Es raro escuchar este tipo de mÃºsica. Desafortunadamente, no puedo encontrarlo en mi directorio. ð¥²', 'MÃºsica extraordinaria y rara, pero no la encuentro. ð©'],
        'processing': 'Procesando...',
        'search_results': ['Resultados a pedido', 'PÃ¡gina'],
        'audio_soon': 'El audio estarÃ¡ aquÃ­ pronto.\nEspere la descarga.\n\nPosiciÃ³n',
        'sww': ' Algo saliÃ³ mal.ð©',
        'downloaded': 'Descargado â',
        'pos_queue': 'PosiciÃ³n en la cola',
        'pos_current': 'PosiciÃ³n actual',
        'access': 'Lo siento mucho ð\n Pero esta funciÃ³n es <b>solo</b> para los suscriptores de @just_another_day_with_music.\nAsÃ­ que suscrÃ­bete y tÃº tambiÃ©n puedes usarlo ð\n\nP.D. Luego reenviar enlace',
        'ncbf': '<b>No se pudo encontrar nada</b> ð',
        'metaKey': ["Cambiar tÃ­tulo", "Cambiar artista", "Cambiar portada", "Cortar audio", 'Obtener portada', "Auto Naming", "Shazam it!", "Listo"],
        'action': 'Seleccione una acciÃ³n',
        'metatag_answers': ['EnvÃ­e un nuevo tÃ­tulo de canciÃ³n', 'EnvÃ­e un nuevo artista', 'EnvÃ­e una nueva versiÃ³n de la canciÃ³n', 'Ingrese un nuevo intervalo para la canciÃ³n\nPor ejemplo: 00:17-02:10' ],
        'success': 'Con Ã©xito â',
        'fra': 'No se pudo cambiar el nombre automÃ¡ticamente',
        'artTitle': ['Artista', 'TÃ­tulo', 'CanciÃ³n'],
        'ugc': 'No se pudo cubrir',
        'cantDownload': 'Lo siento, no puedo descargar esta canciÃ³n ð',
        'albumLimit': 'Actualmente, la cantidad de canciones en el Ã¡lbum para descargar estÃ¡ limitada a 50. En el futuro, definitivamente aumentaremos este lÃ­mite',
        'playlistLimit': 'Actualmente, la cantidad de canciones en la lista de reproducciÃ³n para descargar estÃ¡ limitada a 50. En el futuro, definitivamente aumentaremos este lÃ­mite',
        'startDownload': 'ComenzÃ³ a descargar...',
        'download': 'Descargar',
        'spam_limit': '<b>Â¡ADVERTENCIA!</b>\nEl bot ha alcanzado su lÃ­mite de mensajes, Â¡espere 60 segundos!'
    },

    'pt': {
        'name': 'PortuguÃªs',
        'hello': 'Oið\nPosso baixar mÃºsicas, playlists, Ã¡lbuns do Youtube, Spotify e Deezer.\nTambÃ©m posso alterar a metatag da mÃºsica.\n\nP.S. Inscreva-se em @just_another_day_with_music para remover a marca d\'Ã¡gua. ð',
        'inline': 'Oi ð\nEu posso trabalhar inline, para isso em qualquer chat escreva "@YouTube_Spotify_Deezer_Bot *" (em vez de * digite sua pesquisa) e eu vou baixar essa mÃºsica para vocÃª. \n\nPor exemplo: "@YouTube_Spotify_Deezer_Bot The Beatles"',
        'shazam': 'OlÃ¡!ð\nReconheÃ§o melodias. Envie-me uma mensagem de Ã¡udio ou mensagem de vÃ­deo de 5 a 10 segundos. ð',

        'donate': f'Caro usuÃ¡rio, se vocÃª deseja apoiar o desenvolvimento do bot, vocÃª pode doar dinheiro via: \n\nBitcoin (BTC): `{addresses.btc}` \n\nEthereum (ERC20/BEP20): {addresses.eth} \n\nSolana: {addresses.sol} \n\nTRX/USDT (TRC20): {addresses.trx}\n\nPay By Card (Visa/MasterCard): {addresses.mono} \n\nBuy Me A Coffee: {addresses.bmc} \n\nObrigado pelo seu apoio â¤ï¸, continuaremos a apoiar o bot e a melhorÃ¡-lo.',

        'feedback': 'Se vocÃª tiver alguma solicitaÃ§Ã£o sobre o trabalho do bot, escreva para mim @JADWM',
        'shazam_answers': ['Uma trilha incomparÃ¡vel! Mas nÃ£o consigo achar ð', 'Ã raro ouvir este tipo de mÃºsica. Infelizmente, nÃ£o consigo encontrÃ¡-lo no meu diretÃ³rio. ð¥²', 'MÃºsica extraordinÃ¡ria e rara, mas nÃ£o consigo encontrÃ¡-la. ð©'],
        'processing': 'Em processamento...',
        'search_results': ['Resultados a pedido', 'PÃ¡gina'],
        'audio_soon': 'O Ã¡udio estarÃ¡ aqui em breve.\nAguarde o download.\n\nPosiÃ§Ã£o',
        'sww': 'Algo deu errado. ð©',
        'downloaded': 'Baixado â',
        'pos_queue': 'PosiÃ§Ã£o na fila',
        'pos_current': 'PosiÃ§Ã£o atual',
        'access': 'Sinto muito ð\nMas esse recurso Ã© <b>somente</b> para assinantes do @just_another_day_with_music.\nEntÃ£o se inscreva e vocÃª tambÃ©m pode usar ð\n\nP.S. Em seguida, reenvie o link',
        'ncbf': '<b>Nada pÃ´de ser encontrado</b> ð',
        'metaKey': ["Alterar tÃ­tulo", "Alterar artista", "Alterar capa", "Cut audio", 'Cortar Ã¡udio', "NomeaÃ§Ã£o automÃ¡tica", "Shazam isso!", "Feito"],
        'action': 'Selecione uma aÃ§Ã£o',
        'metatag_answers': ['Envie um novo tÃ­tulo de mÃºsica', 'Envie um novo artista', 'Envie um novo cover para a mÃºsica', 'Digite um novo intervalo para a mÃºsica\nPor exemplo: 00:17-02:10'],
        'success': 'Com sucesso â',
        'fra': 'Falha ao renomear automaticamente',
        'artTitle': ['Artista', 'TÃ­tulo', 'CanÃ§Ã£o'],
        'ugc': 'NÃ£o foi possÃ­vel obter cobertura',
        'cantDownload': 'Desculpe, nÃ£o consigo baixar essa mÃºsica ð',
        'albumLimit': 'Atualmente, o nÃºmero de mÃºsicas do Ã¡lbum para download Ã© limitado a 50. No futuro, definitivamente aumentaremos esse limite',
        'playlistLimit': 'Atualmente, o nÃºmero de mÃºsicas na playlist para download Ã© limitado a 50. No futuro, definitivamente aumentaremos esse limite',
        'startDownload': 'Download iniciado...',
        'download': 'Download',
        'spam_limit': '<b>AVISO!</b>\nO bot atingiu seu limite de mensagens, aguarde 60 segundos!'
    },

    'ru': {
        'name': 'Ð ÑÑÑÐºÐ¸Ð¹',
        'hello': 'ÐÐ´ÑÐ°Ð²ÑÑÐ²ÑÐ¹ÑÐµð\nÐ¯ Ð¼Ð¾Ð³Ñ ÑÐºÐ°ÑÐ°ÑÑ Ð¼ÑÐ·ÑÐºÑ, Ð¿Ð»ÐµÐ¹Ð»Ð¸ÑÑ, Ð°Ð»ÑÐ±Ð¾Ð¼ Ñ Youtube, Spotify Ð¸ Deezer.\nÐ¯ ÑÐ°ÐºÐ¶Ðµ Ð¼Ð¾Ð³Ñ Ð¸Ð·Ð¼ÐµÐ½Ð¸ÑÑ Ð¼ÐµÑÐ°ÑÐµÐ³ Ð¿ÐµÑÐ½Ð¸.\n\nP.S. ÐÐ¾Ð´Ð¿Ð¸ÑÐ¸ÑÐµÑÑ Ð½Ð° @just_another_day_with_music, ÑÑÐ¾Ð±Ñ ÑÐ´Ð°Ð»Ð¸ÑÑ Ð²Ð¾Ð´ÑÐ½Ð¾Ð¹ Ð·Ð½Ð°Ðº. ð',
        'inline': 'ÐÑÐ¸Ð²ÐµÑ ð\nÐ¯ Ð¼Ð¾Ð³Ñ ÑÐ°Ð±Ð¾ÑÐ°ÑÑ Ð² Ð¸Ð½Ð»Ð°Ð¹Ð½ ÑÐµÐ¶Ð¸Ð¼Ðµ, Ð´Ð»Ñ ÑÑÐ¾Ð³Ð¾ Ð² Ð»ÑÐ±Ð¾Ð¼ ÑÐ°ÑÐµ Ð½Ð°Ð¿Ð¸ÑÐ¸ "@YouTube_Spotify_Deezer_Bot *" (ÐÐµÐ· ÐºÐ°Ð²ÑÑÐµÐº Ð¸ Ð²Ð¼ÐµÑÑÐ¾ * ÑÐ²Ð¾Ð¹ Ð·Ð°Ð¿ÑÐ¾Ñ) Ð¸ Ñ Ð¿Ð¾ÐºÐ°Ð¶Ñ ÑÐµÐ±Ðµ ÑÐ¿Ð¸ÑÐ¾Ðº Ð´Ð¾ÑÑÑÐ¿Ð½ÑÑ Ð°ÑÐ´Ð¸Ð¾Ð·Ð°Ð¿Ð¸ÑÐµÐ¹ Ð´Ð»Ñ ÑÐºÐ°ÑÐ¸Ð²Ð°Ð½Ð¸Ñ, Ð³Ð´Ðµ ÑÑ ÑÐ¼Ð¾Ð¶ÐµÑÑ Ð²ÑÐ±ÑÐ°ÑÑ Ð½ÑÐ¶Ð½ÑÐ¹ Ð¸ ÑÐºÐ°ÑÐµÐ½Ð½ÑÐ¹ . \n\nÐÑÐ¸Ð¼ÐµÑ Ð¸ÑÐ¿Ð¾Ð»ÑÐ·Ð¾Ð²Ð°Ð½Ð¸Ñ: "@YouTube_Spotify_Deezer_Bot The Beatles"',
        'shazam': 'ÐÐ°Ðº Ð´ÐµÐ»Ð°? ð\nÐ¯ ÑÐ¼ÐµÑ ÑÐ°ÑÐ¿Ð¾Ð·Ð½Ð°Ð²Ð°ÑÑ Ð¼ÐµÐ»Ð¾Ð´Ð¸Ð¸. ÐÐ»Ñ ÑÑÐ¾Ð³Ð¾ Ð¾ÑÐ¿ÑÐ°Ð²Ñ Ð¼Ð½Ðµ Ð°ÑÐ´Ð¸Ð¾/Ð²Ð¸Ð´ÐµÐ¾Ð·Ð°Ð¿Ð¸ÑÑ Ð¸ Ñ Ð¿ÑÐ¸ÑÐ»Ñ ÑÐµÐ±Ðµ Ð½Ð°Ð·Ð²Ð°Ð½Ð¸Ðµ Ð¿ÐµÑÐ½Ð¸, ÐºÐ¾ÑÐ¾ÑÐ°Ñ ÑÐ°Ð¼ Ð±ÑÐ´ÐµÑ Ð¸Ð³ÑÐ°ÑÑ.',

        'donate': f'ÐÐ¾ÑÐ¾Ð³Ð¾Ð¹ Ð¿Ð¾Ð»ÑÐ·Ð¾Ð²Ð°ÑÐµÐ»Ñ, ÐµÑÐ»Ð¸ Ð¶ÐµÐ»Ð°ÐµÑÑ Ð¿Ð¾Ð´Ð´ÐµÑÐ¶Ð°ÑÑ Ð´Ð°Ð»ÑÐ½ÐµÐ¹ÑÑÑ ÑÐ°Ð·ÑÐ°Ð±Ð¾ÑÐºÑ Ð¸ ÑÑÐ½ÐºÑÐ¸Ð¾Ð½Ð¸ÑÐ¾Ð²Ð°Ð½Ð¸Ðµ Ð±Ð¾ÑÐ°, Ð¼Ð¾Ð¶ÐµÑÑ Ð¸ÑÐ¿Ð¾Ð»ÑÐ·Ð¾Ð²Ð°ÑÑ ÑÐ»ÐµÐ´ÑÑÑÐ¸Ðµ Ð¼ÐµÑÐ¾Ð´Ñ Ð´Ð»Ñ Ð¿Ð¾Ð¶ÐµÑÑÐ²Ð¾Ð²Ð°Ð½Ð¸Ñ: \n\nBitcoin (BTC): {addresses.btc} \n\nEthereum (ERC20/BEP20): {addresses.eth} \n\nSolana: {addresses.sol} \n\nTRX/USDT (TRC20): {addresses.trx}\n\nMonobank (Visa/MasterCard): {addresses.mono} \n\nBuy Me A Coffee: {addresses.bmc} \n\nÐ¡Ð¿Ð°ÑÐ¸Ð±Ð¾ Ð·Ð° Ð¿Ð¾Ð´Ð´ÐµÑÐ¶ÐºÑ â¤ï¸, Ð¼Ñ Ð±ÑÐ´ÐµÐ¼ Ð² Ð´Ð°Ð»ÑÐ½ÐµÐ¹ÑÐµÐ¼ ÑÐ¾Ð²ÐµÑÑÐµÐ½ÑÑÐ²Ð¾Ð²Ð°ÑÑ Ð±Ð¾ÑÐ°.',
        'feedback': 'ÐÑÐ»Ð¸ Ñ Ð²Ð°Ñ ÐµÑÑÑ ÐºÐ°ÐºÐ¸Ðµ-ÑÐ¾ Ð¿Ð¾Ð¶ÐµÐ»Ð°Ð½Ð¸Ñ, Ð¿Ð¾ ÑÐ°Ð±Ð¾ÑÐµ Ð±Ð¾ÑÐ° Ð¿Ð¸ÑÐ¸ÑÐµ Ð¼Ð½Ðµ @JADWM',
        'shazam_answers': ['ÐÐµÑÐ¿Ð¾Ð´Ð¾Ð±Ð½ÑÐ¹ ÑÑÐµÐº! ÐÐ¾ Ñ Ð½Ðµ Ð¼Ð¾Ð³Ñ ÐµÐ³Ð¾ Ð½Ð°Ð¹ÑÐ¸ ð', 'Ð¢Ð°ÐºÑÑ Ð¼ÑÐ·ÑÐºÑ ÑÑÐ»ÑÑÐ¸ÑÑ Ð½Ðµ ÑÐ°ÑÑÐ¾. Ð ÑÐ¾Ð¶Ð°Ð»ÐµÐ½Ð¸Ñ, Ñ Ð½Ðµ Ð¼Ð¾Ð³Ñ ÐµÐµ Ð½Ð°Ð¹ÑÐ¸ Ð² ÑÐ²Ð¾ÐµÐ¹ Ð±Ð°Ð·Ðµ. ð¥²", "ÐÐµÐ¿ÑÐµÐ²Ð·Ð¾Ð¹Ð´ÐµÐ½Ð½Ð°Ñ Ð¸ ÑÐµÐ´ÐºÐ°Ñ Ð¼ÑÐ·ÑÐºÐ°, Ð½Ð¾ Ñ Ð½Ðµ Ð¼Ð¾Ð³Ñ ÐµÐµ Ð½Ð°Ð¹ÑÐ¸. ð©'],
        'processing': 'ÐÐ±ÑÐ°Ð±Ð¾ÑÐºÐ°...',
        'search_results': ['Ð ÐµÐ·ÑÐ»ÑÑÐ°ÑÑ Ð¿Ð¾ Ð·Ð°Ð¿ÑÐ¾ÑÑ', 'Ð¡ÑÑÐ°Ð½Ð¸ÑÐ°'],
        'audio_soon': 'ÐÑÐ·ÑÐºÐ° ÑÐºÐ¾ÑÐ¾ ÑÐºÐ°ÑÐ°ÐµÑÑÑ.\nÐÐ¾Ð¶Ð°Ð»ÑÐ¹ÑÑÐ°, Ð¿Ð¾Ð´Ð¾Ð¶Ð´Ð¸ÑÐµ.\n\nÐÐ¾Ð·Ð¸ÑÐ¸Ñ',
        'sww': 'Ð§ÑÐ¾-ÑÐ¾ Ð¿Ð¾ÑÐ»Ð¾ Ð½Ðµ ÑÐ°Ðº. ÐÐ¾Ñ Ð±ÐµÐ´Ð° ð©',
        'downloaded': 'ÐÐ°Ð³ÑÑÐ¶ÐµÐ½Ð¾ â',
        'pos_queue': 'ÐÐ¾Ð·Ð¸ÑÐ¸Ñ Ð² Ð¾ÑÐµÑÐµÐ´Ð¸',
        'pos_current': 'Ð¢ÐµÐºÑÑÐ°Ñ Ð¿Ð¾Ð·Ð¸ÑÐ¸Ñ',
        'access': 'ÐÐ½Ðµ Ð¾ÑÐµÐ½Ñ Ð¶Ð°Ð»Ñ ð\nÐÐ¾ ÑÑÐ° ÑÑÐ½ÐºÑÐ¸Ñ <b>ÑÐ¾Ð»ÑÐºÐ¾</b> Ð´Ð»Ñ Ð¿Ð¾Ð´Ð¿Ð¸ÑÑÐ¸ÐºÐ¾Ð² @just_another_day_with_music.\nÐ¢Ð°Ðº ÑÑÐ¾ Ð¿Ð¾Ð´Ð¿Ð¸ÑÐ¸ÑÐµÑÑ, Ð¸ Ð²Ñ ÑÐ¾Ð¶Ðµ ÑÐ¼Ð¾Ð¶ÐµÑÐµ ÐµÑ Ð¿Ð¾Ð»ÑÐ·Ð¾Ð²Ð°ÑÑÑÑ ð\n\nP.S. ÐÐ°ÑÐµÐ¼ Ð¿Ð¾Ð²ÑÐ¾ÑÐ½Ð¾ Ð¿ÑÐ¸ÑÐ»Ð¸ÑÐµ ÑÑÑÐ»ÐºÑ',
        'ncbf': '<b>ÐÐ¸ÑÐµÐ³Ð¾ Ð½Ðµ Ð½Ð°Ð¹Ð´ÐµÐ½Ð¾</b> ð',
        'metaKey': ["Ð¡Ð¼ÐµÐ½Ð¸ÑÑ Ð½Ð°Ð·Ð²Ð°Ð½Ð¸Ðµ", "Ð¡Ð¼ÐµÐ½Ð¸ÑÑ Ð¸ÑÐ¿Ð¾Ð»Ð½Ð¸ÑÐµÐ»Ñ", "Ð¡Ð¼ÐµÐ½Ð¸ÑÑ Ð¾Ð±Ð»Ð¾Ð¶ÐºÑ", "ÐÐ±ÑÐµÐ·Ð°ÑÑ Ð°ÑÐ´Ð¸Ð¾", 'ÐÐ¾Ð»ÑÑÐ¸ÑÑ Ð¾Ð±Ð»Ð¾Ð¶ÐºÑ', "ÐÐ²ÑÐ¾Ð½ÐµÐ¹Ð¼Ð¸Ð½Ð³", "ÐÐ°ÑÐ°Ð·Ð°Ð¼Ð¸ÑÐµ ÑÑÐ¾!", "ÐÐ¾ÑÐ¾Ð²Ð¾ â"],
        'action': 'ÐÐ¾Ð¶Ð°Ð»ÑÐ¹ÑÑÐ° Ð²ÑÐ±ÐµÑÐ¸ÑÐµ Ð´ÐµÐ¹ÑÑÐ²Ð¸Ðµ',
        'metatag_answers': ['ÐÐ°Ð¿Ð¸ÑÐ¸ÑÐµ Ð½Ð¾Ð²Ð¾Ðµ Ð½Ð°Ð·Ð²Ð°Ð½Ð¸Ðµ', 'ÐÐ°Ð¿Ð¸ÑÐ¸ÑÐµ Ð½Ð¾Ð²Ð¾Ð³Ð¾ Ð¸ÑÐ¿Ð¾Ð»Ð½Ð¸ÑÐµÐ»Ñ', 'ÐÑÐ¿ÑÐ°Ð²ÑÑÐµ Ð½Ð¾Ð²ÑÑ Ð¾Ð±Ð»Ð¾Ð¶ÐºÑ', 'ÐÐ²ÐµÐ´Ð¸ÑÐµ Ð½Ð¾Ð²ÑÐ¹ Ð¸Ð½ÑÐµÑÐ²Ð°Ð» Ð¿ÐµÑÐ½Ð¸\nÐÐ»Ñ Ð¿ÑÐ¸Ð¼ÐµÑÐ°: 00:17-02:10'],
        'success': 'Ð£ÑÐ¿ÐµÑÐ½Ð¾ â',
        'fra': 'ÐÐµ ÑÐ´Ð°Ð»Ð¾ÑÑ Ð°Ð²ÑÐ¾Ð¼Ð°ÑÐ¸ÑÐµÑÐºÐ¸ Ð¿ÐµÑÐµÐ¸Ð¼ÐµÐ½Ð¾Ð²Ð°ÑÑ',
        'artTitle': ['ÐÑÐ¿Ð¾Ð»Ð½Ð¸ÑÐµÐ»Ñ', 'ÐÐ°Ð·Ð²Ð°Ð½Ð¸Ðµ', 'ÐÐµÑÐ½Ñ'],
        'ugc': 'ÐÐµÐ²Ð¾Ð·Ð¼Ð¾Ð¶Ð½Ð¾ Ð¿Ð¾Ð»ÑÑÐ¸ÑÑ Ð¾Ð±Ð»Ð¾Ð¶ÐºÑ',
        'cantDownload': 'ÐÐ·Ð²Ð¸Ð½Ð¸ÑÐµ, Ñ Ð½Ðµ Ð¼Ð¾Ð³Ñ ÑÐºÐ°ÑÐ°ÑÑ ÑÑÑ Ð¿ÐµÑÐ½Ñ ð',
        'albumLimit': 'Ð Ð½Ð°ÑÑÐ¾ÑÑÐµÐµ Ð²ÑÐµÐ¼Ñ ÐºÐ¾Ð»Ð¸ÑÐµÑÑÐ²Ð¾ Ð¿ÐµÑÐµÐ½ Ð² Ð°Ð»ÑÐ±Ð¾Ð¼Ðµ Ð´Ð»Ñ ÑÐºÐ°ÑÐ¸Ð²Ð°Ð½Ð¸Ñ Ð¾Ð³ÑÐ°Ð½Ð¸ÑÐµÐ½Ð¾ 50. Ð Ð±ÑÐ´ÑÑÐµÐ¼ Ð¼Ñ Ð¾Ð±ÑÐ·Ð°ÑÐµÐ»ÑÐ½Ð¾ ÑÐ²ÐµÐ»Ð¸ÑÐ¸Ð¼ ÑÑÐ¾Ñ Ð»Ð¸Ð¼Ð¸Ñ.',
        'playlistLimit': 'Ð Ð½Ð°ÑÑÐ¾ÑÑÐµÐµ Ð²ÑÐµÐ¼Ñ ÐºÐ¾Ð»Ð¸ÑÐµÑÑÐ²Ð¾ Ð¿ÐµÑÐµÐ½ Ð² Ð¿Ð»ÐµÐ¹Ð»Ð¸ÑÑÐµ Ð´Ð»Ñ Ð·Ð°Ð³ÑÑÐ·ÐºÐ¸ Ð¾Ð³ÑÐ°Ð½Ð¸ÑÐµÐ½Ð¾ 50. Ð Ð±ÑÐ´ÑÑÐµÐ¼ Ð¼Ñ Ð¾Ð±ÑÐ·Ð°ÑÐµÐ»ÑÐ½Ð¾ ÑÐ²ÐµÐ»Ð¸ÑÐ¸Ð¼ ÑÑÐ¾Ñ Ð»Ð¸Ð¼Ð¸Ñ.',
        'startDownload': 'ÐÐ°ÑÐ°Ð» ÑÐºÐ°ÑÐ¸Ð²Ð°ÑÑ ð',
        'download': 'ÐÐ°Ð³ÑÑÐ·Ð¸ÑÑ',
        'spam_limit': '<b>ÐÐÐÐÐÐÐÐ!</b>\nÐÐ¾Ñ Ð´Ð¾ÑÑÐ¸Ð³ Ð»Ð¸Ð¼Ð¸ÑÐ° ÑÐ¾Ð¾Ð±ÑÐµÐ½Ð¸Ð¹, Ð¿Ð¾Ð´Ð¾Ð¶Ð´Ð¸ÑÐµ 60 ÑÐµÐºÑÐ½Ð´!'
    },

    'uk': {
        'name': "Ð£ÐºÑÐ°ÑÐ½ÑÑÐºÐ°",
        'hello': 'ÐÑÐ¸Ð²ÑÑð\nÐ¯ Ð´Ð¾Ð¿Ð¾Ð¼Ð¾Ð¶Ñ ÑÐ¾Ð±Ñ ÑÐºÐ°ÑÐ°ÑÐ¸ Ð¼ÑÐ·Ð¸ÐºÑ, Ð¿Ð»ÐµÐ¹Ð»Ð¸ÑÑÐ¸, Ð° ÑÐ°ÐºÐ¾Ð¶ Ð°Ð»ÑÐ±Ð¾Ð¼Ð¸ Ð· ÑÐ°ÐºÐ¸Ñ ÑÐµÑÐ²ÑÑÑÐ², ÑÐº Youtube, Spotify ÑÐ° Deezer.\nÐ¯ ÑÐ°ÐºÐ¾Ð¶ Ð²Ð¼ÑÑ Ð¼ÑÐ½ÑÑÐ¸ Ð¼ÐµÑÐ°Ð´Ð°Ð½Ñ Ð¿ÑÑÐµÐ½Ñ. \n\nÐÑÐ´Ð¿Ð¸ÑÐ¸ÑÑ Ð½Ð° @just_another_day_with_music, ÑÐ¾Ð± Ð·Ð°Ð±ÑÐ°ÑÐ¸ Ð²Ð¾Ð´ÑÐ½Ð¸Ð¹ Ð·Ð½Ð°Ðº Ð· Ð¿Ð¾Ð²ÑÐ´Ð¾Ð¼Ð»ÐµÐ½Ñ. ð',
        'inline': 'Ð¥Ð°Ð¹ ð\nÐ¯ Ð¼Ð¾Ð¶Ñ Ð¿ÑÐ°ÑÑÐ²Ð°ÑÐ¸ Ð² ÑÐ½Ð»Ð°Ð¹Ð½ ÑÐµÐ¶Ð¸Ð¼Ñ, Ð´Ð»Ñ ÑÑÐ¾Ð³Ð¾ Ð² Ð±ÑÐ´Ñ-ÑÐºÐ¾Ð¼Ñ ÑÐ°ÑÑ Ð½Ð°Ð¿Ð¸ÑÐ¸ "@YouTube_Spotify_Deezer_Bot *" (ÐÐµÐ· Ð»Ð°Ð¿Ð¾Ðº Ñ Ð·Ð°Ð¼ÑÑÑÑ * ÑÐ²ÑÐ¹ Ð·Ð°Ð¿Ð¸Ñ) Ñ Ñ Ð¿Ð¾ÐºÐ°Ð¶Ñ ÑÐ¾Ð±Ñ ÑÐ¿Ð¸ÑÐ¾Ðº Ð´Ð¾ÑÑÑÐ¿Ð½Ð¸Ñ Ð°ÑÐ´ÑÐ¾Ð·Ð°Ð¿Ð¸ÑÑÐ² Ð´Ð»Ñ ÑÐºÐ°ÑÑÐ²Ð°Ð½Ð½Ñ, Ð´Ðµ ÑÐ¸ Ð·Ð¼Ð¾Ð¶ÐµÑ Ð²Ð¸Ð±ÑÐ°ÑÐ¸ Ð¿Ð¾ÑÑÑÐ±Ð½Ð¸Ð¹ Ñ ÑÐºÐ°ÑÐ°ÑÐ¸. \n\nÐÑÐ¸ÐºÐ»Ð°Ð´ Ð²Ð¸ÐºÐ¾ÑÐ¸ÑÑÐ°Ð½Ð½Ñ: "@YouTube_Spotify_Deezer_Bot The Beatles"',
        'shazam': 'Ð¯Ðº ÑÑ Ð¼Ð°ÑÑ? ð\nÐ¯ Ð²Ð¼ÑÑ ÑÐ¾Ð·Ð¿ÑÐ·Ð½Ð°Ð²Ð°ÑÐ¸ Ð¼ÐµÐ»Ð¾Ð´ÑÑ. ÐÐ»Ñ ÑÑÐ¾Ð³Ð¾ Ð²ÑÐ´Ð¿ÑÐ°Ð² Ð¼ÐµÐ½Ñ Ð°ÑÐ´ÑÐ¾-/Ð²ÑÐ´ÐµÐ¾Ð·Ð°Ð¿Ð¸Ñ Ñ Ñ Ð½Ð°Ð´ÑÑÐ»Ñ ÑÐ¾Ð±Ñ Ð½Ð°Ð·Ð²Ñ Ð¿ÑÑÐ½Ñ, ÑÐºÐ° ÑÐ°Ð¼ Ð±ÑÐ´Ðµ Ð³ÑÐ°ÑÐ¸. ð',

        'donate': f'ÐÐ¾ÑÐ¾Ð³Ð¸Ð¹ ÐºÐ¾ÑÐ¸ÑÑÑÐ²Ð°Ñ, ÑÐºÑÐ¾ Ð±Ð°Ð¶Ð°ÑÑ Ð¿ÑÐ´ÑÑÐ¸Ð¼Ð°ÑÐ¸ Ð¿Ð¾Ð´Ð°Ð»ÑÑÑ ÑÐ¾Ð·ÑÐ¾Ð±ÐºÑ Ñ ÑÑÐ½ÐºÑÑÐ¾Ð½ÑÐ²Ð°Ð½Ð½Ñ Ð±Ð¾ÑÐ°, ÑÐ¾ Ð¼Ð¾Ð¶ÐµÑ Ð²Ð¸ÐºÐ¾ÑÐ¸ÑÑÐ¾Ð²ÑÐ²Ð°ÑÐ¸ Ð½Ð°ÑÑÑÐ¿Ð½Ñ Ð¼ÐµÑÐ¾Ð´Ð¸ Ð´Ð»Ñ Ð¿Ð¾Ð¶ÐµÑÑÐ²ÑÐ²Ð°Ð½Ð½Ñ: \n\nMonobank: {addresses.mono} \n\nBitcoin (BTC): {addresses.btc} \n\nEthereum (ERC20/BEP20): {addresses.eth} \n\nSolana: {addresses.sol} \n\nTRX/USDT (TRC20): {addresses.trx}\n\nBuy Me A Coffee: {addresses.bmc} \n\nÐÑÐºÑÑ Ð·Ð° Ð¿ÑÐ´ÑÑÐ¸Ð¼ÐºÑ â¤ï¸, Ð¼Ð¸ Ð½Ð°Ð´Ð°Ð»Ñ Ð±ÑÐ´ÐµÐ¼Ð¾ Ð²Ð´Ð¾ÑÐºÐ¾Ð½Ð°Ð»ÑÐ²Ð°ÑÐ¸ Ð±Ð¾ÑÐ°.',
        'feedback': 'Ð¯ÐºÑÐ¾ Ð¼Ð°ÑÑÐµ ÑÐºÑÑÑ Ð¿Ð¾Ð±Ð°Ð¶Ð°Ð½Ð½Ñ, ÑÐ¾Ð´Ð¾ ÑÐ¾Ð±Ð¾ÑÐ¸ Ð±Ð¾ÑÐ° Ð¿Ð¸ÑÑÑÑ Ð¼ÐµÐ½Ñ @JADWM ',
        'shazam_answers': ['ÐÐµÐ·ÑÑÐ²Ð½ÑÐ½Ð½Ð¸Ð¹ ÑÑÐµÐº! ÐÐ»Ðµ Ñ Ð½Ðµ Ð¼Ð¾Ð¶Ñ Ð¹Ð¾Ð³Ð¾ Ð·Ð½Ð°Ð¹ÑÐ¸ ð', 'Ð¢Ð°ÐºÑ Ð¼ÑÐ·Ð¸ÐºÑ Ð¿Ð¾ÑÑÑÑ Ð½Ðµ ÑÐ°ÑÑÐ¾. ÐÐ° Ð¶Ð°Ð»Ñ, Ñ Ð½Ðµ Ð¼Ð¾Ð¶Ñ Ð·Ð½Ð°Ð¹ÑÐ¸ ÑÑ Ð² ÑÐ²Ð¾ÑÐ¹ Ð±Ð°Ð·Ñ. ð¥²", "ÐÐµÐ¿ÐµÑÐµÐ²ÐµÑÑÐµÐ½Ð° ÑÐ° ÑÑÐ´ÐºÑÑÐ½Ð° Ð¼ÑÐ·Ð¸ÐºÐ°, Ð°Ð»Ðµ Ñ Ð½Ðµ Ð¼Ð¾Ð¶Ñ ÑÑ Ð·Ð½Ð°Ð¹ÑÐ¸. ð©'],
        'processing': 'ÐÐ±ÑÐ¾Ð±ÐºÐ° Ð·Ð°Ð¿Ð¸ÑÑ...',
        'search_results': ['Ð ÐµÐ·ÑÐ»ÑÑÐ°ÑÐ¸ Ð½Ð° Ð·Ð°Ð¿Ð¸Ñ', 'Ð¡ÑÐ¾ÑÑÐ½ÐºÐ°'],
        'audio_soon': 'ÐÑÐ·Ð¸ÐºÐ° ÑÐºÐ¾ÑÐ¾ ÑÐºÐ°ÑÐ°ÑÑÑÑÑ.\nÐÑÐ´Ñ-Ð»Ð°ÑÐºÐ° Ð·Ð°ÑÐµÐºÐ°Ð¹ÑÐµ.\n\nÐÐ¾Ð·Ð¸ÑÑÑ',
        'sww': 'Ð©Ð¾ÑÑ Ð¿ÑÑÐ»Ð¾ Ð½Ðµ ÑÐ°Ðº. ÐÑ ÑÐ°Ð»ÐµÐ¿Ð° ð©',
        'downloaded': 'ÐÐ°Ð²Ð°Ð½ÑÐ°Ð¶ÐµÐ½Ð¾ â',
        'pos_queue': 'ÐÐ¾Ð·Ð¸ÑÑÑ Ð² ÑÐµÑÐ·Ñ',
        'pos_current': 'ÐÐ¾ÑÐ¾ÑÐ½Ð° Ð¿Ð¾Ð·Ð¸ÑÑÑ',
        'access': 'ÐÐµÐ½Ñ Ð´ÑÐ¶Ðµ-Ð´ÑÐ¶Ðµ ÑÐºÐ¾Ð´Ð° ð\nÐÐ»Ðµ ÑÐµÐ¹ ÑÑÐ½ÐºÑÑÐ¾Ð½Ð°Ð» <b>ÑÑÐ»ÑÐºÐ¸</b> Ð´Ð»Ñ Ð¿ÑÐ´Ð¿Ð¸ÑÐ½Ð¸ÐºÑÐ² @just_another_day_with_music.\nÐ¢Ð¾Ð¶ Ð¿ÑÐ´Ð¿Ð¸ÑÐ¸ÑÑ, ÑÐ¾Ð± Ñ ÑÐ¸ Ð¼ÑÐ³ Ð¹Ð¾Ð³Ð¾ Ð²Ð¸ÐºÐ¾ÑÐ¸ÑÑÐ¾Ð²ÑÐ²Ð°ÑÐ¸. ð\n\nP.S. Ð Ð¿ÑÑÐ»Ñ ÑÐ¾Ð³Ð¾ Ð²ÑÐ´Ð¿ÑÐ°Ð² Ð¼ÐµÐ½Ñ Ð¿Ð¾ÑÐ¸Ð»Ð°Ð½Ð½Ñ ÑÐµ ÑÐ°Ð·',
        'ncbf': '<b>ÐÐ°Ð¶Ð°Ð»Ñ Ñ Ð½ÑÑÐ¾Ð³Ð¾ Ð½Ðµ Ð·Ð¼ÑÐ³ Ð·Ð½Ð°Ð¹ÑÐ¸</b> ð',
        'metaKey': ["ÐÐ¼ÑÐ½Ð¸ÑÐ¸ Ð½Ð°Ð·Ð²Ñ", "ÐÐ¼ÑÐ½Ð¸ÑÐ¸ Ð²Ð¸ÐºÐ¾Ð½Ð°Ð²ÑÑ", "ÐÐ¼ÑÐ½Ð¸ÑÐ¸ Ð¾Ð±ÐºÐ»Ð°Ð´Ð¸Ð½ÐºÑ", "ÐÐ±ÑÑÐ·Ð°ÑÐ¸ Ð°ÑÐ´ÑÐ¾", 'ÐÑÑÐ¸Ð¼Ð°ÑÐ¸ Ð¾Ð±ÐºÐ»Ð°Ð´Ð¸Ð½ÐºÑ', "ÐÐ²ÑÐ¾-Ð½ÐµÐ¹Ð¼ÑÐ½Ð³", "ÐÐ°ÑÐ°Ð·Ð°Ð¼Ð¸ÑÐ¸ ÑÐµ!", "ÐÐ¾ÑÐ¾Ð²Ð¾ â"],
        'action': 'ÐÑÐ´Ñ Ð»Ð°ÑÐºÐ° Ð¾Ð±ÐµÑÑÑÑ Ð´ÑÑ',
        'metatag_answers': ['ÐÐ°Ð¿Ð¸ÑÑÑÑ Ð½Ð¾Ð²Ñ Ð½Ð°Ð·Ð²Ñ', 'ÐÐ°Ð¿Ð¸ÑÑÑÑ Ð½Ð¾Ð²Ð¾Ð³Ð¾ Ð²Ð¸ÐºÐ¾Ð½Ð°Ð²ÑÑ', 'ÐÑÐ´Ð¿ÑÐ°Ð²ÑÐµ Ð½Ð¾Ð²Ñ Ð¾Ð±ÐºÐ»Ð°Ð´Ð¸Ð½ÐºÑ', 'ÐÐ²ÐµÐ´ÑÑÑ Ð½Ð¾Ð²Ð¸Ð¹ ÑÐ½ÑÐµÑÐ²Ð°Ð» Ð¿ÑÑÐ½Ñ\nÐÐ»Ñ Ð¿ÑÐ¸ÐºÐ»Ð°Ð´Ñ: 00:17-02:10'],
        'success': 'Ð£ÑÐ¿ÑÑÐ½Ð¾ â',
        'fra': 'ÐÐµ Ð²Ð´Ð°Ð»Ð¾ÑÑ Ð¿ÑÐ¾Ð²ÐµÑÑÐ¸ Ð°Ð²ÑÐ¾-Ð½ÐµÐ¹Ð¼ÑÐ½Ð³',
        'artTitle': ['ÐÐ¸ÐºÐ¾Ð½Ð°Ð²ÐµÑÑ', 'ÐÐ°Ð·Ð²Ð°', 'ÐÑÑÐ½Ñ'],
        'ugc': 'ÐÐµÐ¼Ð¾Ð¶Ð»Ð¸Ð²Ð¾ Ð¾ÑÑÐ¸Ð¼Ð°ÑÐ¸ Ð¾Ð±ÐºÐ»Ð°Ð´Ð¸Ð½ÐºÑ',
        'cantDownload': 'Ð¯ Ð²Ð¸Ð±Ð°ÑÐ°ÑÑÑ, Ð°Ð»Ðµ Ð¼ÐµÐ½Ñ Ð½Ðµ Ð²Ð´Ð°Ð»Ð¾ÑÑ ÑÐºÐ°ÑÐ°ÑÐ¸ ÑÑ Ð¿ÑÑÐ½Ñ ð',
        'albumLimit': 'ÐÐ° Ð´Ð°Ð½Ð¸Ð¹ Ð¼Ð¾Ð¼ÐµÐ½Ñ ÐºÑÐ»ÑÐºÑÑÑÑ Ð¿ÑÑÐµÐ½Ñ Ð² Ð°Ð»ÑÐ±Ð¾Ð¼Ñ Ð´Ð»Ñ ÑÐºÐ°ÑÑÐ²Ð°Ð½Ð½Ñ Ð¾Ð±Ð¼ÐµÐ¶ÐµÐ½Ð° Ð² 50 Ð¾Ð´Ð¸Ð½Ð¸ÑÑ. Ð£ Ð¼Ð°Ð¹Ð±ÑÑÐ½ÑÐ¾Ð¼Ñ Ð¼Ð¸ Ð¾Ð±Ð¾Ð²Ê¼ÑÐ·ÐºÐ¾Ð²Ð¾ Ð·Ð±ÑÐ»ÑÑÐ¸Ð¼Ð¾ ÑÐµÐ¹ Ð»ÑÐ¼ÑÑ.',
        'playlistLimit': 'ÐÐ° Ð´Ð°Ð½Ð¸Ð¹ Ð¼Ð¾Ð¼ÐµÐ½Ñ ÐºÑÐ»ÑÐºÑÑÑÑ Ð¿ÑÑÐµÐ½Ñ Ð² Ð¿Ð»ÐµÐ¹Ð»Ð¸ÑÑÑ Ð´Ð»Ñ ÑÐºÐ°ÑÑÐ²Ð°Ð½Ð½Ñ Ð¾Ð±Ð¼ÐµÐ¶ÐµÐ½Ð° Ð² 50 Ð¾Ð´Ð¸Ð½Ð¸ÑÑ. Ð£ Ð¼Ð°Ð¹Ð±ÑÑÐ½ÑÐ¾Ð¼Ñ Ð¼Ð¸ Ð¾Ð±Ð¾Ð²Ê¼ÑÐ·ÐºÐ¾Ð²Ð¾ Ð·Ð±ÑÐ»ÑÑÐ¸Ð¼Ð¾ ÑÐµÐ¹ Ð»ÑÐ¼ÑÑ.',
        'startDownload': 'ÐÐ¾ÑÐ°Ð² ÑÐºÐ°ÑÑÐ²Ð°ÑÐ¸ ð',
        'download': 'ÐÐ°Ð²Ð°Ð½ÑÐ°Ð¶Ð¸ÑÐ¸',
        'spam_limit': '<b>â ï¸ Ð£ÐÐÐÐ! â ï¸</b>\nÐÐ¸Ð³Ð»ÑÐ´Ð°Ñ, ÑÐ¾ Ð²Ð¸ Ð²ÑÐ´Ð¿ÑÐ°Ð²Ð¸Ð»Ð¸ Ð·Ð°Ð±Ð°Ð³Ð°ÑÐ¾ Ð¿Ð¾Ð²ÑÐ´Ð¾Ð¼Ð»ÐµÐ½Ñ, Ð·Ð°ÑÐµÐºÐ°Ð¹ÑÐµ 60 ÑÐµÐºÑÐ½Ð´, ÑÐ¾Ð± Ð¼Ð°ÑÐ¸ Ð¼Ð¾Ð¶Ð»Ð¸Ð²ÑÑÑÑ Ð´Ð°Ð»Ñ ÐºÐ¾ÑÐ¸ÑÑÑÐ²Ð°ÑÐ¸ÑÑ Ð±Ð¾ÑÐ¾Ð¼!'
        
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