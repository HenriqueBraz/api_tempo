# api_tempo

[![HitCount](http://hits.dwyl.com/HenriqueBraz/HenriqueBraz/api_tempo.svg)](http://hits.dwyl.com/HenriqueBraz/HenriqueBraz/api_tempo)


Uma api para fazer scraping de páginas web, passando elemento_html/seletor_css/pagina_web. Retorna um json com o conteúdo encontrado e campo Status = 1, ou mensagem de erro e campo Status = 0. Método: GET  Exemplo: Todas as divs cujo o seletor css seja "id" na página https://www.climatempo.com.br:  

https://returnstuff-tempo.herokuapp.com/div/id/https://www.climatempo.com.br 
