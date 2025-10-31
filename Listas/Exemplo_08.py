import os
os.system('cls')

escola ={
    "aluno_001":{
        "nome":"Ana Silva"
        "idade":20,

        "notas":{
            "matematica":8.5,
            "portugues":9.0,
            "historia":7.5
        },
        "contato":{
            "email":"ana@gmail.com",
            "telefone":"119988766"
        }

    },
    
    "aluno_002":{
        "nome":"Emerson"
        "idade":22,

        "notas":{
            "matematica":9.5,
            "portugues":8.0,
            "historia":7.0
        },
        "contato":{
            "email":"emerson@gmail.com",
            "telefone":"119988887"
        }
    }
}

print(escola["aluno_001"]["notas"]["matematica"])
print(escola["aluno_002"]["contato"]["email"])