from fastapi import FastAPI
app = FastAPI()



receitas = [
    {
        'nome': 'bolo de laranja',
        'ingredientes': [
            '2 xícaras de farinha de trigo',
            '1 xícara de suco de laranja ou refrigerante de laranja de boa qualidade',
            '4 ovos',
            '1 colher de chá de fermento em pó'
        ],
        'utensilios': ['tigela', 'forma', 'forno'],
        'modo_de_preparo': (
            "Bata as claras em neve, misture as gemas e o açúcar e torne a bater. "
            "Depois, misture a farinha e o suco de laranja. "
            "Por último acrescente o fermento. "
            "Leve ao forno para assar em forma untada e polvilhada por cerca de 40 minutos em 180°C."
        )
    },
    {
        'nome': 'brownie',
        'ingredientes': [
            '5 colheres de manteiga',
            '3 ovos',
            '3 xícaras de achocolatado',
            '6 colheres de açúcar',
            '12 colheres de farinha de trigo'
        ],
        'utensilios': ['tigela', 'forma', 'forno'],
        'modo_de_preparo': (
            "Derreta a manteiga e reserve. "
            "Enquanto derrete, misture os ovos e o açúcar. "
            "Acrescente a manteiga derretida, depois o achocolatado e o trigo. "
            "Unte a forma com manteiga e achocolatado e leve ao forno a 180°C por 30 minutos."
        )
    },
    {
        'nome': 'salada de frutas',
        'ingredientes': [
            '2 mamões papaia pequenos',
            '1 laranja média',
            '5 bananas',
            '2 maçãs',
            '5 morangos maduros',
            '1 pêssego',
            '10 uvas',
            '1 caixa leite condensado (opcional)',
            '10 cubos de gelo',
            '1/2 colher (sopa) canela em pó'
        ],
        'utensilios': ['faca', 'tigela', 'colher'],
        'modo_de_preparo': (
            "Pique todas as frutas. A laranja em pedaços menores para soltar caldo. "
            "Coloque tudo em um prato fundo, adicione leite condensado (se quiser), canela e gelo. "
            "Mexa e leve à geladeira por 30 minutos."
        )
    },
    {
        'nome': 'panqueca',
        'ingredientes': [
            '1 ovo',
            '1 xícara de farinha de trigo',
            '1 xícara de leite',
            '1 pitada de sal',
            '1 colher (sopa) de óleo'
        ],
        'utensilios': ['liquidificador', 'frigideira', 'colher'],
        'modo_de_preparo': (
            "Bata todos os ingredientes no liquidificador até ficar cremoso. "
            "Unte uma frigideira com óleo, despeje uma concha de massa e espalhe. "
            "Doure os dois lados, recheie a gosto, enrole e sirva."
        )
    },
    {
        'nome': 'pudim',
        'ingredientes': [
            '1 lata de leite condensado',
            '1 lata de leite (mesma medida da lata de leite condensado)',
            '3 ovos inteiros',
            '1 xícara (chá) de açúcar (para calda)',
            '1/2 xícara de água (para calda)'
        ],
        'utensilios': ['liquidificador', 'panela', 'forma redonda', 'forno'],
        'modo_de_preparo': (
            "Bata os ovos, leite condensado e leite no liquidificador. "
            "Calda: derreta o açúcar, acrescente a água e deixe engrossar. "
            "Coloque na forma, despeje o pudim e asse em banho-maria por 45 minutos. "
            "Deixe esfriar e desenforme."
        )
    },
    {
        'nome': 'vitamina de morango',
        'ingredientes': [
            '5 morangos lavados e sem cabinho',
            '1 copo de leite',
            '2 colheres de açúcar ou leite condensado'
        ],
        'utensilios': ['liquidificador', 'copo'],
        'modo_de_preparo': (
            "Bata todos os ingredientes no liquidificador até ficar homogêneo. "
            "Sirva gelado."
        )
    }
]

@app.get("/")
def hello():
    return{"title":"Livro de Receitas"}

def get_receita(nome: str):
    for receita in receitas:
        if receita["nome"].lower() == nome.lower():
            return receita