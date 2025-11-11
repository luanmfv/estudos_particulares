br para quebra de linha vem de break

para deixar no texto  o simbolo < é &lt; e o simbolo > é &gt;

se quiser um espaço maior use o css, não faça <br><br><br><br><br><br>

para usar emojis vá no site emojipedia

exemplo: &#x1F480;  &#x 
o código inteiro é U+1F480 você filtra apenas a partir do u+

----------------------------------------------------------------------------------------------------------------------------

DIREITOS AUTORAIS

não é correto pegar imagens da internet e usar como fossem suas

sempre use sites de imagens gratuitas como pexels, unsplash, pixabay

no google imagens existe a ferramenta para filtro de direitos autorais
 
para vídeos também existem sites

baixar Gimp para alterar tamanho e formato de imagens

para web geralmente o tipo de imagem é jpeg e png, as vezes um gif

jpeg foi criado em 1983 consegue compactar uma imagem

png foi criado em 1996 foi criada pela w3c (WOrld Wide Web Consortium) empresa que define padrões oficiais da Web.
para substituir o formato gif, png não permite animação mas permite transparência.

png mais qualidade e permite transparencia, jpeg tamanho menor de arquivo

----------------------------------------------------------------------------------------------------------------------------

tratamento de imagens

tamanho comum é 1500 / 1000 e 50 / 50 de resolução  formato px

geralmente em site é um tamanho 650px também

não pode deixar seu site lento nunca

a resolução que ja vem do arquivo é do valor estabelecido para baixo, não aumente que a qualidade não irá melhorar.


para upar imagem aperta img e da enteder o sistema dará o código todo, para upar a imagem clica nas aspas duplas do source e da cntrl espaço

<img src="logo.html.full.png" alt="Logo HTML5">  (imagem source="imagem" texto alternativo para deficientes visuais="nome da imagem")

----------------------------------------------------------------------------------------------------------------------------



favicon que é o icone do site e é muito mais compatível usar o arquvo como ico

site iconarchive free icons

site para criar icone favicon.cc

https://favicon.io/ é para texto png ou emoji virar icone

para adicionar a função de icone digite link e selecione a opção favicon em href coloque o arquivo com cntrl espaço

recomenda-se usar o icone com o nome de arquivo favicon.ico


----------------------------------------------------------------------------------------------------------------------------

semântica: muito mais valor o significado do que a forma, significado das palavras 

se a tag ficar vermelha é porque está incorreto, comandos antigos que não funcionam mais

mudar cor de letra, cor de fundo tamanho de letra é tudo com css

e para animações é com js

mecanismos de busca podem não te valorizar como google, por utilizar códigos antigos

a tag B por exemplo, deixa em negrito, e não tem significado, mas tem forma que é o b

a tag b significa bold que é negrito em ingles

e também é possivel deixar igual ao negrito com o comando strong que é forte porém em semântica

comando para colocar comando em alguma frase, selecione ela, apeerta control + shift + p, va em wrap with abbreviation, selecione o comando e dê enter

para italico temos o comando i ou em  não semântica e semântica

----------------------------------------------------------------------------------------------------------------------------

a tag mark exerce a função de marca texto e é semântica

se quiser criar um mark para todos de padrão, crie assim

    <style>
        mark {
            background-color:cyan;
        }

    </style>

    daí todos os mark serão da cor desejável,  caso queira alterar é apenas ir no especifico e adicionar 

    <mark style="background-color: brown;"
    



    <p>Estamos criando um <big>texto grande</big> <small>um texto pequeno</small></p>


    big não existe mais porque entra em css, small existe porque em contrato por exemplo existem letras pequenas

    a tag ins é de insert e deixa sublinhado

    temos sup (em cima) e sub (em baixo), 
    ----------------------------------------------------------------------------------------------------------------------------

    comando code para envelopar melhor um texto, ou quando citar algum código ele deixa em um formato melhor


    comando shift + tab toda a area que selecionar voltara para a esquerda nos espaços vazios, apenas tab vai para a direita (no vs code)


    o comando pre serve para respeitar os espaços que você inseriu


    ao invés de utilizar " " nos textos, você pode inserir o comando q  que ele faz o mesmo. e é recomendável usar quando é uma citação.



    <blockquote cite="https://www.google.com.br/books/edition/Building_iPhone_Apps_with_HTML_CSS_and_J/3NQhBTNKJB8C?hl=pt-BR&gbpv=1&dq=html&pg=PA16&printsec=frontcover">
        The future of mobile development is clearly web technologies like CSS, HTML and JavaScript. Jonathan Stark shows you how
    to leverage your existing web development skills to build native iPhone applications using these technologies.
    </blockquote>



o comando cite=""  não aparece nada na tela, mas os mecanismos de busca sabem que você mencionou aquela página e relacionará a ela.


p>Estou estudando <abbr title="HyperText Markup Language">HTML</abbr> e <abbr title="Cascading Style Sheets">CSS</abbr>.</p>

comando abbr ao passar o mouse na palavra html no site, mostrara escrito a palavra  inteira da abrevicação citada.

bdo para inverter o que for digitado

----------------------------------------------------------------------------------------------------------------------------


ol significa ordered list

segurar o alt em varias linhas você pode alterar elas ao mesmo tempo

    















