# Kontent
Crud de gerenciamente de conteúdos desenvolvido em Python com Django e Django Rest Framework.


### Endpoints da aplicação:
| Método | Endpoint | Descrição |
|---|---|---|
| `POST` | `api/contents/` |Criação de conteúdo | 
| `GET` | `api/contents/` |Listar todos os conteúdos|
| `GET` | `api/contents/<content_id>/` | Filtrar conteúdos pelo id | 
| `PATCH` | `api/contents/<content_id>/` | Atualizar conteúdo pelo id | 
| `DELETE` | `api/contents/<content_id>/` | Deletar conteúdo pelo id |
| `GET` | `api/contents/filter/` | Filtrar conteúdos por query param | 
