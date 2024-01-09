openapi-generator-cli generate^
    -g python^
    -i https://esi.evetech.net/latest/swagger.json^
    -p generateSourceCodeOnly=false^
    --package-name esi-client^
    --git-host github.com^
    --git-user-id ballsten^ 
    --git-repo-id eve-esi-client