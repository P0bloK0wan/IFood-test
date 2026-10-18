# iFood: pesquisa de movimento e eventos do pedido — 18/10/2026

Esta revisão adiciona resposta visual a quatro ações dos fluxos locais: colocar um produto na sacola, receber a confirmação do restaurante, preparar o pedido e sair para entrega. Nenhum evento se conecta à operação real do iFood.

| Evento | Implementação | Origem e limite |
| --- | --- | --- |
| Produto adicionado | Confete e fitas, 30 fps, recorte dos frames 9–74 (2,167 s); pulso discreto da sacola | Camadas `confete` e `fitas` do splash CazéTV recuperado do APK. Transformações, formas e keyframes preservados; apenas as camadas necessárias e seus assets foram selecionados. A aplicação na sacola e o recorte de tempo são adaptações. |
| Restaurante aceitou | Sacola vermelha, logo branco, selo de confirmação e pequenos brilhos; entrada em aproximadamente 1,18 s | Composição e movimento criados para a versão web. Usa o wordmark já documentado. Não é apresentado como Lottie nativo recuperado. |
| Preparando seu pedido | Panela vermelha com wordmark branco, tampa oscilando e três trilhas de vapor; entrada de 650 ms e movimento por até 4,52 s | Ilustração em CSS/SVG e movimento criados para a versão web, usando o wordmark já documentado. Não é um recurso nativo recuperado do aplicativo. |
| Saiu para entrega | Ilustração do entregador de moto/mochila vermelha; entrada, leve movimento vertical, cenário e pista em deslocamento durante 4,8 s | PNG preservado de um espelho público de ilustrações iFood. Fonte oficial exata não estabelecida. Movimento, pista e cenário são adaptações web. |

## Comportamento

- Confete ocorre depois que o item entra na sacola. Abrir produto, recusar a troca de restaurante ou atingir o limite de 20 unidades não dispara a celebração.
- A camada de confete não captura toques/cliques, não recebe foco e se remove ao terminar, navegar, ocultar a aba ou ativar movimento reduzido.
- Aceite, preparo e saída para entrega aparecem no acompanhamento. Cada cena toca uma vez por pedido/estado nesta sessão; recarregar ou voltar ao histórico mantém a ilustração estática. As animações param antes de 5 s.
- Com movimento reduzido, o usuário recebe a confirmação textual normal e as ilustrações estáticas. A preferência é respeitada inclusive se mudar durante o efeito.
- Concluir/cancelar/navegar remove as animações da cena anterior. A reprodução pausa quando a aba está oculta.

## Pesquisa pública

O inventário detalhado está em [research.md](../references/ifood/motion-v4/research/research.md). Abrange os dez arquivos completos já recuperados do APK, materiais oficiais do iFood Design no Dribbble, estudos dos autores sobre esperas de confirmação, ilustrações, expressões Ailo, iFood Ads e campanhas. Foram catalogadas 16 URLs públicas de GIFs de esperas e dois vídeos do autor; os downloads desses arquivos foram bloqueados por 403/406 e não estão incluídos como arquivos obtidos.

Foram efetivamente baixados e medidos cinco vídeos MP4, um GIF animado e uma imagem estática do perfil iFood Design, incluindo acompanhamento, abas, capas, rating de restaurantes, conceito do gestor e fluxo iFood Box. As referências de parceiros/marketing são identificadas como tais. A referência “Loop Onboarding” é estática; “Loop” é o nome do produto. A duração da apresentação completa não é tratada como duração de uma transição nativa.

Não existe, nas fontes localizadas, um catálogo público que comprove todas as animações de todas as versões/experimentos do app. A pesquisa não encontrou confirmação de confete nativo ao adicionar à sacola, nem o JSON executável dos novos personagens de espera. Os originais já integrados permanecem separados, intactos, no manifesto de `assets/motion/`.

## Recursos e validação

`dist/assets/effects/manifest.json` registra hashes, recorte, fonte e classificação. O entregador vem de [Imagens Free](https://imagensfree.com.br/entregador-ifood-png/), arquivo PNG de 302×276, com bytes preservados. Os relatórios e tentativas de acesso ficam em `references/ifood/motion-v4/courier/`.

`tests/ifood-effects.test.mjs` compara as camadas/assets do confete com o JSON de origem e verifica integridade dos dois recursos. `tests/ifood_effects_browser.py` percorre os eventos reais da interface, verifica movimento entre frames, descarte, recusa de troca, preferência de acessibilidade e persistência de reprodução. Executar com servidor ativo: `BASE_URL=http://localhost:3000/ TEST_OUTPUT=verification-local/effects npm run test:effects` no pacote iFood.
