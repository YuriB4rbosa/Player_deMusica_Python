🎵 Player de Música Python
Um player de música simples e elegante desenvolvido em Python com interface gráfica usando Tkinter e Pygame para reprodução de áudio.

✨ Características
🎶 Reprodução de arquivos MP3

📁 Interface moderna com tema escuro

🎚️ Controle de volume

📋 Gerenciamento de playlist

⏯️ Controles de reprodução (play, pause, stop, next)

🖱️ Seleção interativa da playlist

🛠️ Requisitos
Bibliotecas Necessárias
bash
pip install pygame
O Tkinter geralmente já vem instalado com o Python.

🚀 Como Usar
Executar o programa:

bash
python music_player.py
Carregar músicas:

Clique no botão "📁 Carregar"

Selecione um ou mais arquivos MP3

As músicas serão adicionadas à playlist

Controles:

▶ Play: Reproduz a música selecionada

⏸ Pause: Pausa a reprodução atual

⏹ Stop: Para a reprodução

⏭ Next: Avança para a próxima música

Volume: Use o slider para ajustar o volume

Seleção na playlist:

Clique em qualquer música da lista para reproduzi-la imediatamente

📋 Funcionalidades
✅ Implementadas
Carregamento múltiplo de arquivos MP3

Controles básicos de reprodução

Controle de volume

Navegação pela playlist

Interface visual intuitiva

Detecção e tratamento de erros

🔧 Possíveis Melhorias Futuras
Botão "Anterior"

Barra de progresso da música

Tempo decorrido/restante

Modo de repetição (repeat)

Modo aleatório (shuffle)

Equalizador

Suporte a mais formatos de áudio

🎨 Interface
A interface foi desenvolvida com um tema escuro moderno:

Cores principais: Azul escuro (#2C3E50) e variações

Botões coloridos para diferentes ações

Lista de reprodução com highlights

Informações em tempo real da música atual

⚠️ Solução de Problemas
Erros Comuns:
"Nenhuma música na playlist!"

Solução: Carregue músicas usando o botão "📁 Carregar"

Erro ao reproduzir arquivo

Verifique se o arquivo MP3 não está corrompido

Certifique-se de que o arquivo existe no local especificado

Sem áudio

Verifique se o volume do sistema está ligado

Confirme se os speakers/fones de ouvido estão conectados

📁 Estrutura do Código
text
MusicPlayer/
├── __init__()          # Inicialização do player
├── setup_ui()          # Configuração da interface
├── load_music()        # Carregamento de arquivos
├── play_music()        # Reprodução de música
├── pause_music()       # Pausar reprodução
├── stop_music()        # Parar reprodução
├── next_music()        # Próxima música
├── set_volume()        # Controle de volume
└── update_playlist()   # Atualização da lista
🤝 Contribuindo
Sinta-se à vontade para:

Reportar bugs

Sugerir novas funcionalidades

Enviar pull requests
